# iPhone Duo: what the app sees

Each fact has a source. **Measured** means measured in the iPhone Duo simulator (Xcode 27.1 27A9269, iOS 27.1 runtime 24A94401). **Apple** means stated in Apple's Tech Talks or technotes. Do not hard-code any of these numbers in app code. They are here so you can predict and check layouts.

## Displays

| | Outer display | Inner display |
|---|---|---|
| Pixels | 1398 × 2034 (measured) | 2007 × 2853 (measured) |
| Scale | 3 (measured) | 3 (derived from the screenshot size; not measured in the app) |
| App window, closed, portrait | 386 × 678 pt (measured) | – |
| Size classes | portrait: compact width, regular height (measured and Apple). Landscape: compact × compact (Apple) | regular × regular (Apple) |
| Honors `UISupportedInterfaceOrientations` | yes (Apple) | **no** (Apple) |
| Status bar | a vertical strip on the right, 80 pt wide in closed portrait (measured) | – |
| New windows (scenes) | cannot be created (Apple) | can be created (Apple) |

The idiom is `.phone` on both displays. A phone app on the inner display gets regular × regular, like an iPad.

## Poses (Apple)

Code does not see a "pose". It sees size classes, window size, reserved regions, and hinge status.

- **Closed**: outer display. Behaves like a standard iPhone.
- **Open, flat**: inner display. The full display is available. The division region exists but is inactive.
- **Partially open (book)**: the fold crosses the inner display. The division region is active. Two usable regions, one on each side.
- **Propped on a table**: the fold is horizontal. Top region for content to watch, bottom region for controls.
- **Split view**: two apps side by side on the inner display. Your app can be on either side.

## Bars (Apple)

- Navigation bars, toolbars, and tab bars move to a **vertical bar** on the side of the window: on the outer display in landscape and on the inner display in landscape.
- They stay horizontal on the inner display in portrait (Apple).
- Outer display, closed portrait (measured, two apps):
  - `NavigationStack` with symbol toolbar items and no tab bar: the items stay horizontal, at the top and the bottom.
  - `TabView` with a `NavigationStack` inside: the tab bar **and** the symbol toolbar items move into a vertical bar on the right, below the vertical status bar. A text-only item ("Edit") stays horizontal at the top.
  - So do not assume portrait means horizontal bars. Check the screenshots.
- In a split view controller, only the detail column gets the vertical bar. Inspectors do not get their own.
- Only bars owned by system containers move. Custom `UIToolbar`, `UINavigationBar`, `UITabBar` views and custom SwiftUI bars do not.

## Reserved regions (Apple)

- **Division**: the fold. Active only when the device is folded. When flat, it is inactive.
- **Occlusion**: the FaceTime camera on the inner display. Active only while the camera is active.
- System presentations (alerts, action sheets, menus, popovers) and system containers (NavigationSplitView, List, ScrollView) already avoid them.

## SDK tiers (Apple)

| Built with | On the inner display |
|---|---|
| iOS 27 SDK | The app extends left of the status bar only. No vertical bars. |
| iOS 27.1 SDK | Edge to edge. Vertical bars. Reserved regions and the other new APIs. |

## Cameras (Apple)

- Two front cameras, both square ultra-wide sensors: outer (up to 4K, 120 fps) and inner, under the display (1080p, up to 60 fps).
- Front camera discovery by position returns a virtual front camera. It switches between inner and outer by itself, is limited to 1080p at 60 fps, and has no depth.
- The camera that faces the user changes when the device opens, closes, or flips.

## Other hardware

- Biometrics: Touch ID. The simulator profile lists `com.apple.touch-id` and no Face ID (measured, from the device profile).
