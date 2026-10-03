# Duo API surface (iOS 27.1 SDK, Xcode 27.1 27A9269)

Every name below was read from the SDK's `.swiftinterface` files and headers, and used in code that type-checks. If you need a name that is not here, run `scripts/find-api.sh <name>`. If it is not found, it does not exist. Do not use it.

The SDK writes SwiftUI availability as `anyAppleOS 27.1`. In app code, write `iOS 27.1`.

## Swift names that differ from ObjC or from talk transcripts

| Wrong (ObjC name or transcript) | Swift |
|---|---|
| `UIWindowSceneActivationAction` | `UIWindowScene.ActivationAction` |
| `UIWindowSceneSessionRoleCameraCaptureAccessory` | `UISceneSession.Role.windowCameraCaptureAccessory` |
| `UIHingeStatus` | `UIHinge.Status` |
| `UIHingeInteractionUpdate` | `UIHingeInteraction.Update` |
| `UIViewReservedRegion` | `UIView.ReservedRegion` |
| `UIViewLayoutRegion` | `UIView.LayoutRegion` |
| `toolbarCompressionBehavior` | `toolbarVerticalCompressionBehavior` (SwiftUI), `verticalBarCompressionBehavior` (UIKit) |
| "toolbarVerticalEdge trait" | `traitCollection.verticalBarEdge` (UIKit); `toolbarVerticalEdge` is the SwiftUI environment value |

## Reserved regions (iOS 27.1)

| SwiftUI | UIKit |
|---|---|
| `GeometryProxy.reservedRegions(kind:options:layoutDirectionBehavior:) -> [ReservedRegion]` | `UIView.reservedRegions(kind:options:) -> [UIView.ReservedRegion]` |
| `ReservedRegion.Kind.division`, `.occlusion` | `UIView.ReservedRegion.Kind.division`, `.occlusion` |
| `ReservedRegion.QueryOptions.includeInactive` | `UIView.ReservedRegion.QueryOptions.includeInactive` |
| `region.frame: CGRect`, `.margins: EdgeInsets`, `.isActive`, `.kind`, `.id` | `region.frame: CGRect`, `.margins: UIEdgeInsets`, `.isActive`, `.kind`, `.id` |

The old SPI `_boundaryLayoutRegions` is deprecated in favor of `reservedRegions(kind: .division)`.

## Layout regions

- `UIView.LayoutRegion.bar(onEdge:extent:)` (iOS 27.1), with `UIRectEdge` or `NSDirectionalRectEdge`.
- `UIView.layoutGuide(for:)`, `edgeInsets(for:)`, `directionalEdgeInsets(for:)` (iOS 26).
- SwiftUI `ContentMarginGuide.container`, `.contentMargins(for:edges:alignment:)`, `GeometryProxy.contentMargins(for:edges:)` (iOS 27.1).

## Arrangements (iOS 27.1)

| SwiftUI | UIKit |
|---|---|
| `ArrangementView(primary:secondary:)` | `UIArrangementViewController()` |
| `.arrangementViewStyle(.automatic / .split / .overlay)` | `updateArrangement(_:animated:)` with `.split` / `.overlay` |
| `.split.axes(_: Axis.Set)`, `.overlay.axes(_:)` | `UISplitArrangement.axes(_: UIAxis)`, `UIOverlayArrangement.axes(_:)` |
| pane: `splitArrangementLayoutRatio(_:)`, `splitArrangementLayoutRatio(minHorizontal:idealHorizontal:maxHorizontal:minVertical:idealVertical:maxVertical:)` | `UISplitArrangement.ViewProperties` (`width`, `height`: `DimensionRange` of `.automatic`, `.intrinsic`, `.fractional(_:)`, `.absolute(_:)`; `layoutPriority`) |
| pane: `splitArrangementLayoutSize(minWidth:idealWidth:maxWidth:minHeight:idealHeight:maxHeight:)`, `splitArrangementFixedLayoutSize(horizontal:vertical:)` | `setViewProperties(_:for:)` |
| pane: `overlayArrangementEdge(_: VerticalEdge?)` / `(_: HorizontalEdge?)` | `UIOverlayArrangement.ViewProperties.edge` |
| env: `splitArrangementAxis: Axis?`, `overlayArrangementZIndex: Int` | `state(for:) -> ViewState?` (`zIndex`, `splitAxis`, `isHidden`) |
| – | `setViewController(_:for:animated:)`, `viewController(for:)`, `placement(for:)`, `UIViewController.arrangementViewController` |

## Vertical bars

| SwiftUI | UIKit | Since |
|---|---|---|
| `ToolbarContent.axisBehavior(_:)`: `.automatic`, `.horizontalOnly`, `.verticalPreferred` | `UIBarButtonItem.axisBehavior` | 27.1 |
| `@Environment(\.toolbarVerticalEdge) HorizontalEdge?` | `traitCollection.verticalBarEdge` (`.unspecified`, `.leading`, `.trailing`), `UITraitCollection.systemTraitsAffectingVerticalBarEdge` | 27.1 |
| `.toolbarVerticalBehavior(.automatic / .disabled)` | `preferredVerticalBarBehavior`, `childForPreferredVerticalBarBehavior`, `setNeedsUpdateOfVerticalBarConfiguration()` | 27.1 |
| `.toolbarVerticalCompressionBehavior(.automatic / .prefersToolbarItems / .prefersTabBar)` | `navigationItem.verticalBarCompressionBehavior` (`.automatic`, `.prefersBarItems`, `.prefersTabBar`) | 27.1 |
| `ToolbarItem.visibilityPriority(_:)` | `UIBarButtonItem.visibilityPriority` | 27.0 |
| `ToolbarOverflowMenu { }` | `navigationItem.additionalOverflowItems` | 27.0 / 16.0 |
| `ToolbarItemPlacement.topBarPinnedTrailing` | `navigationItem.pinnedTrailingGroup` | 27.0 / 16.0 |
| `.badge(_:)` | `UIBarButtonItem.badge = .count(_:)` | 26.0 |

## Hinge (iOS 27.1)

| SwiftUI | UIKit |
|---|---|
| `.onHingeChange(isEnabled:_:)` with `(oldContext, newContext: DeviceHingeContext)` | `UIHingeInteraction(updateHandler:)`, `isEnabled` |
| `DeviceHingeContext.hinge: DeviceHinge?` | `UIHingeInteraction.Update.hinge: UIHinge?` |
| `DeviceHinge.status: DeviceHinge.Status` (struct: `.closed`, `.partiallyOpen`, `.fullyOpen`) | `UIHinge.status: UIHinge.Status` (enum: `.unknown`, `.closed`, `.partiallyOpen`, `.fullyOpen`) |
| `DeviceHinge.angle: Angle` | `UIHinge.angle: CGFloat` (radians) |

## Scenes and accessories

- `UIWindowScene.ActivationAction`, `UIApplication.activateSceneSession(for:errorHandler:)`.
- `UISceneAccessory.externalNonInteractive(sceneConfiguration:)` (iOS 27.0), `.cameraCapture(sceneConfiguration:)` (iOS 27.1), `UIViewController.registerSceneAccessory(_:)`.
- SwiftUI `.sceneAccessory { }` (iOS 27.0), `CameraCaptureAccessory(isEnabled:content:)` and `.onAvailabilityChange(_:)` (iOS 27.1).

## Camera (iOS 27.1 unless noted)

- `AVCaptureDevice.DeviceType.builtInOuterUltraWideCamera`, `.builtInInnerUltraWideCamera`.
- AVKit: `AVCaptureDeviceDirectionCoordinator(view:deviceTypes:changeHandler:)`, `.deviceDirections`; `AVCaptureDeviceDirectionMap.forwardFacingDeviceDescriptors`, `.backwardFacingDeviceDescriptors`; `AVCaptureDeviceDescriptor` (`uniqueID`, `deviceType`, `position`, `localizedName`, `mediaTypes`). Create the device with `AVCaptureDevice(uniqueID:)`.
- `AVCaptureDevice.RotationCoordinator` (iOS 17), `AVCapturePhotoOutput.isCameraSensorOrientationCompensationEnabled`, `AVCaptureDevice.dynamicAspectRatio` (iOS 26).

## Other

- `ConcentricRectangle`, `UICornerConfiguration` (iOS 26).
- `TabView.defaultTabBarPlacement(.sidebar)`, `UITabBarController.sidebar.preferredPlacement` (iOS 27.0).
