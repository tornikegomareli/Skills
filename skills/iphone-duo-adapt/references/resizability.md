# Resizability foundation (checks R01 to R09)

Xcode 27.1 ships Apple's `app-resizability` skill. It has full decision trees for R01 to R05. `scripts/preflight.sh` prints the paths of its task files when Xcode 27.1 is installed. **Use Apple's file when it exists.** This file is the short version for machines without it.

Rules for every R fix:

- Use the value closest to the code: the view's trait collection, then the view's window scene. Never replace one global with another (`UIApplication.shared.connectedScenes.first` is as wrong as `UIScreen.main`).
- If no local object is available, add a parameter and pass it from the caller.
- When the value can change while the app runs (display scale, size), also react to the change: `registerForTraitChanges`, `viewWillTransition(to:with:)`, `layoutSubviews`, or SwiftUI environment values.
- Keep control flow and existing guards. Change only the deprecated reference.

All code compiles against the iOS 27.1 SDK. Blocks marked `// min: 17.0` also compile with an iOS 17 deployment target.

## R01: `UIScreen.main`

| Old | New |
|---|---|
| `UIScreen.main.scale` in a view or view controller | `traitCollection.displayScale` |
| `UIScreen.main.bounds` for layout | the container's bounds: `view.bounds`, `window.bounds`, `windowScene.effectiveGeometry.coordinateSpace.bounds`; SwiftUI `GeometryReader` or `containerRelativeFrame` |
| `UIWindow(frame: UIScreen.main.bounds)` | `UIWindow(windowScene:)` in the scene delegate |
| a screen object really needed | `view.window?.windowScene?.screen` |

```swift
// min: 17.0
final class ThumbnailView: UIView {
    override func layoutSubviews() {
        super.layoutSubviews()
        let scale = traitCollection.displayScale // was UIScreen.main.scale
        layer.contentsScale = scale
    }
}

struct Artwork: View {
    var body: some View {
        Image(systemName: "waveform")
            .resizable()
            .scaledToFit()
            .containerRelativeFrame(.horizontal) { width, _ in width * 0.8 } // was UIScreen.main.bounds.width * 0.8
    }
}
```

## R02: Orientation

Replace layout decisions based on orientation with size classes or the window's shape:

```swift
// min: 17.0
final class GalleryViewController: UIViewController {
    override func viewWillTransition(to size: CGSize, with coordinator: UIViewControllerTransitionCoordinator) {
        super.viewWillTransition(to: size, with: coordinator)
        let isWide = size.width > size.height // was interfaceOrientation.isLandscape
        coordinator.animate { _ in self.applyLayout(wide: isWide) }
    }

    private func applyLayout(wide: Bool) {}
}
```

Keep orientation where the physical orientation matters: camera capture (use `AVCaptureDevice.RotationCoordinator`, see `camera.md`), motion, AR.

## R03: Idiom

Replace `userInterfaceIdiom == .pad` layout checks with size classes. Duo is `.phone` but gets regular × regular on the inner display.

```swift
// min: 17.0
struct Columns: View {
    @Environment(\.horizontalSizeClass) private var horizontalSizeClass

    var body: some View {
        let count = horizontalSizeClass == .regular ? 5 : 3 // was userInterfaceIdiom == .pad
        LazyVGrid(columns: Array(repeating: GridItem(.flexible()), count: count)) {
            ForEach(0..<30, id: \.self) { Text("\($0)") }
        }
    }
}
```

## R04: Scene lifecycle and global windows

Scene lifecycle migration: see `scenes.md`. Global window lookups:

| Old | New |
|---|---|
| `UIApplication.shared.keyWindow`, `.windows.first` | `view.window`, or the scene passed to the function |
| `connectedScenes.first as? UIWindowScene` | the scene of the view that triggered the code |
| app delegate lifecycle methods for UI work | scene delegate methods |

## R05: Asymmetric safe areas

Handle each side on its own. The vertical bar and the vertical status bar inset one side only.

```swift
// min: 17.0
final class CardViewController: UIViewController {
    private let card = UIView()

    override func viewDidLayoutSubviews() {
        super.viewDidLayoutSubviews()
        let safe = view.bounds.inset(by: view.safeAreaInsets) // was width - safeAreaInsets.left * 2
        card.frame = CGRect(x: safe.minX, y: safe.minY + 16, width: safe.width, height: 200)
    }
}
```

Prefer Auto Layout against `view.safeAreaLayoutGuide` or `view.layoutMarginsGuide` over frame math. Replace `topLayoutGuide` / `bottomLayoutGuide` with `safeAreaLayoutGuide.topAnchor` / `.bottomAnchor`. Never add fixed insets (20, 44, 34, 47, 59): read the safe area.

## R06: Sizes and device models

Replace comparisons with screen-size numbers (`width <= 375`) with size classes or with thresholds derived from content ("does the text fit"). Remove device-model tables. Duo windows are 386 pt wide closed and change size at run time.

## R07: Display corners

```swift
struct CornerCard: View {
    var body: some View {
        ConcentricRectangle()
            .fill(.green)
            .padding(8)
            .ignoresSafeArea()
    }
}
```

UIKit: `UICornerConfiguration` on the view.

## R08: Keyboard frame

```swift
// min: 17.0
final class ComposerViewController: UIViewController {
    private let composer = UIView()

    override func viewDidLoad() {
        super.viewDidLoad()
        view.addSubview(composer)
        composer.translatesAutoresizingMaskIntoConstraints = false
        NSLayoutConstraint.activate([
            composer.leadingAnchor.constraint(equalTo: view.safeAreaLayoutGuide.leadingAnchor),
            composer.trailingAnchor.constraint(equalTo: view.safeAreaLayoutGuide.trailingAnchor),
            composer.bottomAnchor.constraint(equalTo: view.keyboardLayoutGuide.topAnchor, constant: -16), // was keyboard frame math
        ])
    }
}
```

If you must read the frame from the notification, convert it: `view.convert(frame, from: view.window?.windowScene?.screen.coordinateSpace)`.

## R09: Biometrics

```swift
// min: 17.0
func biometryName() -> String {
    let context = LAContext()
    _ = context.canEvaluatePolicy(.deviceOwnerAuthenticationWithBiometrics, error: nil)
    switch context.biometryType {
    case .faceID: return "Face ID"
    case .touchID: return "Touch ID"
    case .opticID: return "Optic ID"
    default: return "Passcode"
    }
}
```
