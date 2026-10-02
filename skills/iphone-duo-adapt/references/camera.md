# Camera (checks C01 to C06)

Only for apps that use `AVCaptureSession`. The simulator has no camera, so nothing here can be verified in the simulator. Say so in the report and ask the user to test on a device.

All code compiles against the iOS 27.1 SDK. Blocks marked `// min: 17.0` also compile with an iOS 17 deployment target.

## What changes (Apple)

- Two front cameras, both square ultra-wide sensors. Outer: up to 4K, 120 fps. Inner (under the display): 1080p, up to 60 fps.
- Front discovery by position (`AVCaptureDevice.default(..., position: .front)`, or a discovery session with `.front`) returns a **virtual front camera**. It switches between inner and outer when the device opens and closes. It is limited to what both support: 1080p, 60 fps. No depth.
- "Front" no longer means "facing the user". Closed: the outer cameras face the user. Open: the inner camera faces the user. Open and flipped around: the rear and outer cameras face the user.
- The app can move between displays, which changes the rotation of the preview and of captured media.

## C01: Choose the front camera strategy (decision Q6)

**Option 1, virtual camera (default).** Keep position-based discovery. Fix C02, C03, and C06. Nothing else is needed.

**Option 2, individual cameras.** Discover `.builtInOuterUltraWideCamera` and `.builtInInnerUltraWideCamera` and switch with `AVCaptureDeviceDirectionCoordinator` (AVKit). The coordinator reports which cameras face forward and backward relative to a view. Its handler runs on the main queue. Pass the descriptors (Sendable) to your capture queue or actor, and create the device there.

```swift
@MainActor
final class DirectionAwareCamera {
    private var coordinator: AVCaptureDeviceDirectionCoordinator?
    private let capture = CaptureController()

    func start(in view: UIView) {
        // Keep a strong reference: the coordinator stops when released.
        coordinator = AVCaptureDeviceDirectionCoordinator(
            view: view,
            deviceTypes: [.builtInOuterUltraWideCamera, .builtInInnerUltraWideCamera, .builtInDualWideCamera]
        ) { [capture] map in
            guard let forward = map.forwardFacingDeviceDescriptors.first else { return }
            Task { await capture.use(uniqueID: forward.uniqueID, isRearCamera: forward.position == .back) }
        }
    }
}

actor CaptureController {
    private let session = AVCaptureSession()

    func use(uniqueID: String, isRearCamera: Bool) {
        guard let device = AVCaptureDevice(uniqueID: uniqueID),
              let input = try? AVCaptureDeviceInput(device: device) else { return }
        session.beginConfiguration()
        session.inputs.forEach { session.removeInput($0) }
        if session.canAddInput(input) { session.addInput(input) }
        session.commitConfiguration()
        // Mirror the preview when a rear camera faces the user (see C02).
    }
}
```

Rules (Apple): do not call AVFoundation from the change handler directly; use one coordinator per view (for example one per display when you show UI on both); the map is empty until the first callback. Depth is available only from the individual cameras.

Gate the whole type with `@available(iOS 27.1, *)` when the deployment target is lower, and keep the existing discovery code as the fallback.

## C02: Mirror by direction, not by position

Old logic: `isVideoMirrored = device.position == .front`. On Duo that is wrong when the device is open and flipped. Rule (Apple): mirror when the camera faces the user. With the virtual camera, the front camera faces the user; with option 2, use the forward-facing descriptor.

```swift
// min: 17.0
func applyMirroring(to connection: AVCaptureConnection, cameraFacesUser: Bool) {
    guard connection.isVideoMirroringSupported else { return }
    connection.automaticallyAdjustsVideoMirroring = false
    connection.isVideoMirrored = cameraFacesUser
}
```

Set both outcomes (true and false) every time the camera changes. Never set it only in one branch.

## C03: Rotation with the rotation coordinator

Replace `videoOrientation` and `UIDevice.current.orientation` in capture code with `AVCaptureDevice.RotationCoordinator` (iOS 17). On Duo it also updates when the app moves between displays.

```swift
// min: 17.0
@MainActor
final class PreviewRotation {
    private var coordinator: AVCaptureDevice.RotationCoordinator?
    private var observation: NSKeyValueObservation?

    func attach(device: AVCaptureDevice, previewLayer: AVCaptureVideoPreviewLayer) {
        let coordinator = AVCaptureDevice.RotationCoordinator(device: device, previewLayer: previewLayer)
        self.coordinator = coordinator
        previewLayer.connection?.videoRotationAngle = coordinator.videoRotationAngleForHorizonLevelPreview
        observation = coordinator.observe(\.videoRotationAngleForHorizonLevelPreview, options: .new) { [weak previewLayer] coordinator, _ in
            let angle = coordinator.videoRotationAngleForHorizonLevelPreview
            Task { @MainActor in previewLayer?.connection?.videoRotationAngle = angle }
        }
    }

    /// Use this angle on the photo or movie output connection before each capture.
    var captureAngle: CGFloat? { coordinator?.videoRotationAngleForHorizonLevelCapture }
}
```

Create a new coordinator each time the device changes. After adopting it, Apple recommends turning off sensor orientation compensation on the photo output (it is on by default for the Duo front cameras). Check a captured photo is upright before and after:

```swift
func disableCompensation(on output: AVCapturePhotoOutput) {
    output.isCameraSensorOrientationCompensationEnabled = false
}
```

## C04: Preview layout

On the inner display the preview has more room. Either offset the preview and group controls in the free space, or fill the display. The front sensors are square: `device.dynamicAspectRatio` can select a landscape aspect ratio to fill the inner display. Changing the aspect ratio during a movie recording stops the recording, so change it only while idle.

## C05: Camera capture accessory (decision Q7)

Shows extra UI on the outer display while the camera UI stays on the inner display. Available only while the app is full screen on the inner display and has a running capture session. The system decides when to show it. The app must work without it.

```swift
struct CameraRoot: View {
    @State private var showTeleprompter = true
    @State private var accessoryAvailable = false

    var body: some View {
        Color.black // camera preview
            .sceneAccessory {
                CameraCaptureAccessory(isEnabled: $showTeleprompter) {
                    Text("Smile!").font(.largeTitle)
                }
                .onAvailabilityChange { accessoryAvailable = $0 }
            }
            .toolbar {
                Toggle("Teleprompter", systemImage: "text.alignleft", isOn: $showTeleprompter)
                    .disabled(!accessoryAvailable)
            }
    }
}
```

UIKit: `registerSceneAccessory(.cameraCapture(sceneConfiguration:))` on the camera view controller, with a scene delegate for the accessory scene. Its session role is `UISceneSession.Role.windowCameraCaptureAccessory`.

Unverified: Apple Tech Talks do not name an entitlement for this accessory. If registration has no effect on a device, check the current documentation before you add workarounds.

## C06: Flash

The front cameras have no flash, and the camera in use changes when the device opens. Check support every time you build settings:

```swift
// min: 17.0
func photoSettings(for output: AVCapturePhotoOutput, preferred: AVCaptureDevice.FlashMode) -> AVCapturePhotoSettings {
    let settings = AVCapturePhotoSettings()
    settings.flashMode = output.supportedFlashModes.contains(preferred) ? preferred : .off
    return settings
}
```
