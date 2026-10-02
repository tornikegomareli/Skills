# Scenes and multitasking (checks S01 to S03)

- Every app takes part in split view multitasking on the inner display, next to another app, on either side. No opt-in. An app that resizes well on iPad or in iPhone Mirroring is ready (Apple).
- Folding is a size change, not a lifecycle change. Do not wait for `scenePhase` or `sceneDidBecomeActive` to re-layout.
- New windows (scenes) can be created on the inner display only. Requests on the outer display fail (Apple).

All code compiles against the iOS 27.1 SDK. Blocks marked `// min: 17.0` also compile with an iOS 17 deployment target.

## S01: Request new windows safely

Prefer `UIWindowScene.ActivationAction`. It hides itself when a new window is not available. (The ObjC name is `UIWindowSceneActivationAction`; that name does not exist in Swift.)

```swift
// min: 17.0
final class FeedViewController: UIViewController {
    override func viewDidLoad() {
        super.viewDidLoad()
        let openInNewWindow = UIWindowScene.ActivationAction { _ in
            UIWindowScene.ActivationConfiguration(userActivity: NSUserActivity(activityType: "com.example.feed"))
        }
        navigationItem.rightBarButtonItem = UIBarButtonItem(primaryAction: openInNewWindow)
    }
}
```

When you keep `requestSceneSessionActivation`, always pass an error handler and tell the user when it fails:

```swift
// min: 17.0
@MainActor func openFeedWindow(from scene: UIWindowScene) {
    let request = UISceneSessionActivationRequest(role: .windowApplication, userActivity: NSUserActivity(activityType: "com.example.feed"))
    UIApplication.shared.activateSceneSession(for: request) { error in
        print("New window not available: \(error.localizedDescription)")
    }
}
```

SwiftUI `openWindow` needs `UIApplicationSupportsMultipleScenes = YES`. Without it, show the content in the current window instead.

## S02: Multiple windows (decision Q5)

Not needed for split view. Enable only after the user agrees: set `UIApplicationSupportsMultipleScenes` to `YES`, make sure no state is global per app (a single "current document" singleton breaks with two windows), and restore scene state from `NSUserActivity`.

## S03: External displays

Replace `UIScreen.didConnectNotification` and `UIScreen.screens` with scene-based code: a scene configuration for the external display role, or a scene accessory (iOS 27):

```swift
final class PresenterViewController: UIViewController {
    override func viewDidLoad() {
        super.viewDidLoad()
        let config = UISceneConfiguration(name: "External", sessionRole: .windowExternalDisplayNonInteractive)
        registerSceneAccessory(.externalNonInteractive(sceneConfiguration: config))
    }
}
```

## Scene lifecycle (R04)

A UIKit app built with the iOS 27 SDK must use the scene lifecycle or it crashes at launch. If preflight found Apple's `scene-lifecycle-task` file, follow it. It asks the user before splitting `didFinishLaunchingWithOptions`. The minimum:

1. Add `UIApplicationSceneManifest` with a `UISceneConfigurations` entry for `UIWindowSceneSessionRoleApplication` that names the scene delegate class.
2. Move window creation from the app delegate into `scene(_:willConnectTo:options:)`.
3. Move per-app lifecycle callbacks (`applicationDidBecomeActive`, ...) to the scene delegate equivalents (`sceneDidBecomeActive`, ...).

```swift
// min: 17.0
final class SceneDelegate: UIResponder, UIWindowSceneDelegate {
    var window: UIWindow?

    func scene(_ scene: UIScene, willConnectTo session: UISceneSession, options connectionOptions: UIScene.ConnectionOptions) {
        guard let windowScene = scene as? UIWindowScene else { return }
        let window = UIWindow(windowScene: windowScene)
        window.rootViewController = UIViewController()
        window.makeKeyAndVisible()
        self.window = window
    }

    func sceneDidBecomeActive(_ scene: UIScene) {}
}
```

Info.plist entry:

```xml
<key>UIApplicationSceneManifest</key>
<dict>
	<key>UIApplicationSupportsMultipleScenes</key>
	<false/>
	<key>UISceneConfigurations</key>
	<dict>
		<key>UIWindowSceneSessionRoleApplication</key>
		<array>
			<dict>
				<key>UISceneConfigurationName</key>
				<string>Default Configuration</string>
				<key>UISceneDelegateClassName</key>
				<string>$(PRODUCT_MODULE_NAME).SceneDelegate</string>
			</dict>
		</array>
	</dict>
</dict>
```
