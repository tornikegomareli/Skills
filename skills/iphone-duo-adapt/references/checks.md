# Check catalog

Each check has an ID, a severity, a detection method, and a fix. `scripts/audit.py` runs every check marked **grep**. You must do the checks marked **manual** yourself by reading the app's screens.

Severity:

- **Blocker**: the app cannot use the Duo layout at all, or the App Store rejects it.
- **High**: visible breakage on Duo (clipped, hidden, or unreachable UI, wrong camera, crash risk).
- **Medium**: works, but looks wrong or ignores a Duo behavior that users will see.
- **Low**: polish, or an optional Duo feature.

A grep hit is a candidate. Read the context before you record it. Record false positives in `DUO_AUDIT.md` with one line of reason, so the next audit run can be compared.

---

## D: Build and configuration

### D01 Built with an SDK older than iOS 27.1 (Blocker, grep: preflight)
**Why:** An app built with the iOS 27 SDK runs on the inner display with space left of the status bar only. It gets no vertical bars and no reserved regions. The full Duo layout needs the iOS 27.1 SDK.
**Fix:** Build with Xcode 27.1. Keep the deployment target. Gate new APIs with `#available(iOS 27.1, *)`.

### D02 `UIRequiresFullScreen` is `YES` (High, grep)
**Why:** TN3192: when the app is built with the iOS 27 SDK and the key is `YES`, the key no longer opts the app out of resizing. The system resizes the scene *discretely* (the size changes once, at the end of a drag), unless `UIRequiresFullScreenIgnoredStartingWithVersion` is 27 or lower. Either way the app changes size on Duo, when it opens and closes and in split view. A key set to `NO` is not a finding.
**Fix:** Decision **Q1** in `decisions.md`. Never delete the key and never add `UIRequiresFullScreenIgnoredStartingWithVersion` without the user's answer. Whatever the answer, the layouts must handle resizing.

### D03 No launch screen (Blocker, grep)
**Why:** iOS 27 rejects the App Store upload with `ITMS-90870` (TN3208).
**Fix:** Add `UILaunchScreen` (an empty dictionary is valid) or `INFOPLIST_KEY_UILaunchScreen_Generation = YES`. Ask before you replace an existing launch storyboard.

### D04 Orientation lock (Medium, grep)
**Detect:** `UISupportedInterfaceOrientations` with portrait only, or a `supportedInterfaceOrientations` override.
**Why:** The inner display does not honor supported interface orientations. A portrait-only app still gets a wide window there. The lock is not a bug, but every layout in the app must work in a wide window.
**Fix:** Keep the key. Add every screen of the app to the manual review for F01 to F05 in a wide window.

---

## R: Resizability foundation

These checks match Apple's `app-resizability` skill. If preflight found Apple's task files, use them for the fix. They are more complete. Otherwise use `resizability.md`.

### R01 `UIScreen.main` / `[UIScreen mainScreen]` / `UIScreen.screens` (High, grep)
**Why:** Duo has two displays. "Main screen" is ambiguous and Apple will deprecate it. Values from it are wrong for the display the app is on.
**Fix:** Use the closest context: `traitCollection.displayScale` for scale, the view's or window scene's bounds for size, `view.window?.windowScene?.screen` when a screen object is really needed. Apple task file: `uiscreen-task`.

### R02 Orientation used for layout (High, grep)
**Detect:** `interfaceOrientation`, `statusBarOrientation`, `UIDevice.current.orientation`, `UIDeviceOrientationDidChangeNotification`, `isLandscape`, `isPortrait`.
**Why:** On the inner display, orientation does not describe the window shape. Split view and the fold give windows of any shape.
**Fix:** Use size classes, or compare the window's width and height. Keep orientation only where the physical orientation matters (camera, motion). Apple task file: `orientation-task`.

### R03 Idiom used for layout (Medium, grep)
**Detect:** `userInterfaceIdiom`, `UI_USER_INTERFACE_IDIOM`.
**Why:** Duo is `.phone`, but its inner display has regular × regular size classes like an iPad. Idiom checks give it the phone layout on a large display.
**Fix:** Use size classes. Keep idiom only for real device-type needs. Apple task file: `idiom-task`.

### R04 No scene lifecycle, or global window access (Blocker / High, grep)
**Detect:** no `UIApplicationSceneManifest` and a `window` property on the app delegate; `UIApplication.shared.windows`, `.keyWindow`, `connectedScenes.first`.
**Why:** As of iOS 27, the scene lifecycle is required: a UIKit app built with the iOS 27 SDK that has not adopted it crashes at launch (Blocker). Measured: the `Snap` fixture crashes on the iPhone Duo simulator with `EXC_BREAKPOINT` in `_UIApplicationEvaluateRuntimeIssueForNoSceneLifecycleAdoption_block_invoke` (UIKitCore). Global window lookups return the wrong window when more than one exists (High).
**Fix:** Adopt `UIWindowSceneDelegate` (UIKit) or confirm the SwiftUI `App` lifecycle. Pass the scene or window from the call site. Apple task file: `scene-lifecycle-task`.

### R05 Symmetric or hard-coded safe area (High, grep)
**Detect:** `safeAreaInsets.left * 2`, `.leading * 2`, `insets.left + insets.left`, fixed insets such as `44`, `34`, `47`, `59` added to frames, `topLayoutGuide`, `bottomLayoutGuide`.
**Why:** Vertical bars and the vertical status bar add an inset on one side only. On the outer display the status bar is a vertical strip on the right side (measured: the app window is 386 pt wide on a 466 pt display).
**Fix:** Handle each side on its own: `view.bounds.inset(by: view.safeAreaInsets)`. Foreground content in the safe area. Only backgrounds extend past it. Apple task file: `safe-area-task`.

### R06 Hard-coded screen sizes or device detection (Medium, grep)
**Detect:** screen-size literals (`320`, `375`, `390`, `393`, `402`, `414`, `428`, `430`, `440`, `667`, `812`, `844`, `852`, `874`, `896`, `926`, `932`, `956`) in comparisons or frames, `UIDevice.current.model`, `utsname`, `hw.machine`.
**Why:** Duo windows are 386 pt wide closed and much wider open. They also change size while the app runs.
**Fix:** Derive sizes from the container (GeometryReader, `containerRelativeFrame`, view bounds, size classes). Never map device model to layout.

### R07 Hard-coded display corner radius (Low, grep)
**Detect:** `_displayCornerRadius`, corner radius literals `39`, `44`, `47`, `55` used to match the screen.
**Why:** Duo displays have different corner shapes.
**Fix:** `ConcentricRectangle()` in SwiftUI, `UICornerConfiguration` in UIKit.

### R08 Keyboard frame used in screen coordinates (Medium, grep)
**Detect:** `keyboardFrameEndUserInfoKey`, `UIKeyboardFrameEndUserInfoKey`.
**Why:** The frame is in screen coordinates. With split view, a vertical status bar, or a window that is not full screen, screen and window coordinates differ.
**Fix:** Convert the frame with `view.convert(frame, from: view.window?.windowScene?.screen.coordinateSpace)`, or use `keyboardLayoutGuide` (UIKit) and the keyboard safe area (SwiftUI).

### R09 Face ID assumptions (Low, grep)
**Detect:** `"Face ID"` in user-facing strings, `biometryType == .faceID` with no Touch ID branch.
**Why:** The iPhone Duo simulator profile lists Touch ID (`com.apple.touch-id`) and no Face ID.
**Fix:** Read `LAContext().biometryType` and show the matching name. Keep `NSFaceIDUsageDescription`; it is harmless.

---

## B: Bars

Details and code: `vertical-bars.md`.

### B01 Custom bars (High, grep + manual)
**Detect:** `UIToolbar(`, `UINavigationBar(`, `UITabBar(` created in code; `<toolbar`, `<navigationBar`, `<tabBar` in a storyboard or XIB outside a navigation or tab controller; SwiftUI bars made from `HStack` in `.safeAreaInset(edge: .bottom)`, `.safeAreaInset(edge: .top)`, `.overlay(alignment: .bottom)`, or a custom tab bar.
**Why:** Only system bars move to the vertical bar. In landscape on Duo, a custom bar stays horizontal and takes vertical space from content while the system bars of other apps move aside.
**Fix:** Move the items into `.toolbar` on a `NavigationStack` / `NavigationSplitView`, or into `navigationItem` / `toolbarItems` in a `UINavigationController`, or into `TabView` / `UITabBarController`. If a custom bar must stay (for example a drawing palette), ask (**Q4**) and position it with reserved regions and `UIView.LayoutRegion.bar(onEdge:extent:)`.

### B02 `NavigationView` (Medium, grep)
**Why:** Soft-deprecated. Apple's vertical-bar guidance names `NavigationStack` and `NavigationSplitView` as the containers that take part.
**Fix:** `NavigationStack` for one column, `NavigationSplitView` for more.

### B03 Bar items with text only (Medium, grep + manual)
**Detect:** `Button("...") {` inside `ToolbarItem`, `UIBarButtonItem(title:` with no image.
**Why:** A vertical bar has a fixed width. Items with a symbol move to it. Text-only items stay horizontal.
**Fix:** Give every item a title and a symbol: `Button("Share", systemImage: "square.and.arrow.up")`, `UIBarButtonItem(title:image:...)`. The system picks the form. Keep text-only only when the text carries data (a price).

### B04 Custom views in bars (Medium, grep)
**Detect:** `UIBarButtonItem(customView:`, custom views in `ToolbarItem`.
**Fix:** Decide the axis. Views that change between a symbol and text (Select/Done) get `.axisBehavior(.horizontalOnly)`. Views that can draw vertically get `.verticalPreferred` and adapt with `@Environment(\.toolbarVerticalEdge)` / `traitCollection.verticalBarEdge`.

### B05 Counts inside item titles (Low, manual)
**Detect:** titles like `"Inbox (\(count))"` in bars.
**Fix:** Use `.badge(count)` / `item.badge = .count(n)` so the item can be symbol-only.

### B06 Custom "more" menu with an ellipsis (Low, grep)
**Detect:** `"ellipsis"`, `"ellipsis.circle"` symbols in bar items.
**Why:** The system overflow menu uses the ellipsis. Two ellipsis menus confuse users when the vertical bar overflows.
**Fix:** Move the items into `ToolbarOverflowMenu` / `navigationItem.additionalOverflowItems`, or give the custom menu a different symbol.

### B07 Priority, compression, and opt-out (Low, manual)
**When:** the app has a `TabView` / `UITabBarController` and toolbar items on the same screen, many bar items, a bottom-heavy single-screen layout (calculator style), or sheets with only a close button.
**Fix:** Decisions **Q2** and **Q3**. APIs: `.visibilityPriority`, `.toolbarVerticalCompressionBehavior`, `.toolbarVerticalBehavior(.disabled)`, `preferredVerticalBarBehavior`.

---

## F: Fold and layout

Details and code: `fold-and-layout.md`.

### F01 Controls in the middle of the screen (High, manual + grep)
**Detect (grep hints):** `.position(x:`, `size.width / 2`, `bounds.midX`, `.center =`, full-screen `ZStack` roots with buttons, `UIStackView` or buttons centered with `centerXAnchor` on the root view.
**Why:** When the device is partially folded, a division region runs through the center of the inner display. Controls on it are hard to see and to tap.
**Fix:** Use `reservedRegions(kind: .division)` to move controls off the fold. When propped on a table, put content to watch in the top region and controls in the bottom region. Do not move scrolling content (lists, feeds, articles).

### F02 Custom two-pane layouts (Medium, manual + grep)
**Detect:** `HStack` / `VStack` of two main panes sized by GeometryReader, two child view controllers laid out side by side, custom split containers.
**Fix:** Master/detail navigation → `NavigationSplitView` / `UISplitViewController`. Two views that must both stay visible → `ArrangementView` with `.split` / `UIArrangementViewController` with `.split`.

### F03 Foreground over background layouts (Medium, manual)
**Detect:** `ZStack` or overlays with a card, sheet, or panel over a map, player, or canvas.
**Fix:** `ArrangementView` with `.overlay`. Read `overlayArrangementZIndex` to collapse the foreground view when it overlays.

### F04 Fixed grid columns (Low, grep)
**Detect:** `Array(repeating: GridItem(`, fixed column counts, fixed `itemSize` in `UICollectionViewFlowLayout`.
**Fix:** Derive columns from width. When a division region exists (use `.includeInactive`), prefer an even column count so the fold falls between columns. Keep the outer margins and add spacing around the fold.

### F05 Controls outside the safe area (Medium, grep + manual)
**Detect:** `.ignoresSafeArea()` / `.edgesIgnoringSafeArea(` on views that contain controls or text.
**Fix:** Only the background ignores the safe area. Put the controls in an inner view that respects it.

### F06 Navigation container swapped on size class (High, grep + manual)
**Detect:** `if horizontalSizeClass == .regular` (or `.compact`) that returns a different navigation container (`NavigationStack` in one branch, `NavigationSplitView` in the other), or UIKit code that replaces the root view controller on a trait change.
**Why:** Opening and closing the device changes the size class. Swapping the container destroys the navigation state and closes sheets. The user loses their place every time they open the phone.
**Fix:** Use one container that adapts: `NavigationSplitView` collapses to a stack in compact width, and `UISplitViewController` does the same. State must survive open and close.

---

## S: Scenes and multitasking

Details and code: `scenes.md`.

### S01 Scene activation without error handling (Medium, grep)
**Detect:** `requestSceneSessionActivation`, `openWindow`.
**Why:** The outer display cannot create new windows. Requests there fail.
**Fix:** Prefer `UIWindowScene.ActivationAction`, which hides itself when new windows are not available. Handle the error handler of `requestSceneSessionActivation`.

### S02 Multiple windows (Low, decision)
**When:** the app has document or detail content that users could want side by side, and `UIApplicationSupportsMultipleScenes` is false or missing.
**Fix:** Decision **Q5**. Not required for split view multitasking.

### S03 External display through `UIScreen` (Low, grep)
**Detect:** `UIScreen.didConnectNotification`, `UIScreenDidConnectNotification`, `UIScreen.screens.count`.
**Fix:** Use a scene with the external display session role, or `UISceneAccessory.externalNonInteractive(sceneConfiguration:)` (iOS 27).

---

## C: Camera

Only when the app uses `AVCaptureSession`. Details and code: `camera.md`.

### C01 Front camera found by position (Medium, grep)
**Detect:** `position: .front`, `.builtInTrueDepthCamera`, `AVCaptureDevice.default(` with front position.
**Why:** On Duo, front discovery returns a virtual front camera. It switches between the inner and outer camera by itself and is limited to 1080p at 60 fps. It has no depth.
**Fix:** Decision **Q6**: keep the virtual camera (least work) or use `.builtInOuterUltraWideCamera` / `.builtInInnerUltraWideCamera` with `AVCaptureDeviceDirectionCoordinator`.

### C02 Logic that assumes front means "facing the user" (High, grep)
**Detect:** `position == .front` used for mirroring, UI labels, or selfie logic.
**Why:** On Duo the displays face opposite ways. When the device is open and flipped, the rear and outer cameras face the user.
**Fix:** Use `AVCaptureDeviceDirectionCoordinator` and mirror when the forward-facing device is a rear camera.

### C03 Capture rotation from device orientation (High, grep)
**Detect:** `videoOrientation`, `UIDevice.current.orientation` near capture code, manual rotation of preview layers.
**Fix:** `AVCaptureDevice.RotationCoordinator`. After you adopt it, set `isCameraSensorOrientationCompensationEnabled = false` on the photo output.

### C04 Fixed preview layout (Low, manual)
**Fix:** Let the preview adapt on the inner display. Consider `dynamicAspectRatio` for the square front sensors.

### C06 Flash on a front camera (Medium, grep)
**Detect:** `flashMode =` without a check of `supportedFlashModes`.
**Why:** The front cameras have no flash. On Duo the forward-facing camera changes when the device opens, so a flash mode that was valid can become invalid.
**Fix:** Check `photoOutput.supportedFlashModes.contains(mode)` each time you build `AVCapturePhotoSettings`.

### C05 Camera capture accessory (Low, decision)
**When:** the app records or photographs people (selfie, video, teleprompter, kids' camera).
**Fix:** Decision **Q7**. `CameraCaptureAccessory` shows extra UI on the outer display while the camera UI stays on the inner display.

---

## H: Hinge

### H01 Hinge feature (Low, decision)
**When:** only when the user asks for a feature driven by the fold (an instrument, a game control, an effect). Never add it for layout.
**Fix:** `hinge.md`.
