# Decision points

These fixes change product behavior, so the user decides. Collect every question that applies after the audit, then ask them in one round (at most 4 per round, recommended option first). For each question, name the file and line that raised it.

If the user says "use your judgment", or the run is non-interactive, apply the **Default** and list it under "Defaults applied" in `DUO_AUDIT.md`.

## Always ask (once per project)

### Q0 Deployment target
**When:** the deployment target is below iOS 27.1 (almost always).
**Ask:** "Your app supports iOS <X>. Should I keep that and gate the Duo APIs with `#available(iOS 27.1, *)`, or raise the minimum to iOS 27.1?"
**Default:** keep the deployment target and gate. Raising it drops users.

### Q8 Scope
**When:** the app has more than about 10 screens, or has screens you cannot reach without an account or data.
**Ask:** which screens matter most, and whether any screens are out of scope (admin, debug, legacy).
**Default:** all screens reachable from the root; skip debug-only code.

## Ask when the check fires

### Q1 `UIRequiresFullScreen` (D02)
**Options:**
1. Remove the key after the layouts are fixed (recommended). The app then resizes smoothly.
2. Keep it. With the iOS 27 SDK the system still resizes the app, in discrete steps.
3. Keep it and add `UIRequiresFullScreenIgnoredStartingWithVersion` with a version the user picks, to keep full screen on older iOS versions.
**Default:** option 2 (change nothing in the plist), and fix the layouts anyway.

### Q2 Vertical bar opt-out (B07)
**When:** a single-screen, bottom-heavy layout (calculator, keypad, recorder), or a sheet with one close button.
**Options:** keep vertical bars (recommended for most screens) / disable them on the named screens with `.toolbarVerticalBehavior(.disabled)` or `preferredVerticalBarBehavior`.
**Default:** keep vertical bars. Disable only for sheets whose toolbar has one close button.

### Q3 Tab bar or toolbar first (B07)
**When:** a screen shows a tab bar and toolbar items together.
**Options:** navigation-first, where the toolbar compresses first (system default) / task-first, where the tab bar compresses first (`.prefersToolbarItems`).
**Default:** system default.

### Q4 Custom bar that must stay custom (B01)
**When:** a bar cannot become a system toolbar without losing its function (drawing palette, media scrubber, keyboard accessory).
**Options:** convert to system toolbar items (recommended when possible) / keep it custom and place it with reserved regions and a bar layout region.
**Default:** convert when every control is a plain button or menu. Otherwise keep it and position it around reserved regions.

### Q5 Multiple windows (S02)
**When:** the app has documents, conversations, or items that users could compare side by side, and multiple scenes are off.
**Options:** leave it off (split view with other apps still works) / enable `UIApplicationSupportsMultipleScenes` and handle scene state restoration.
**Default:** leave it off. Enabling multiple scenes needs state work the audit cannot size.

### Q6 Front camera strategy (C01)
**Options:**
1. Keep the virtual front camera (least work). It switches cameras by itself. Limited to 1080p at 60 fps, no depth.
2. Use the individual cameras with `AVCaptureDeviceDirectionCoordinator` (full quality, depth, more code).
**Default:** option 1, plus fixes for mirroring (C02) and rotation (C03).

### Q7 Camera capture accessory (C05)
**When:** the app photographs or records people.
**Ask:** whether to show content on the outer display during capture (preview for the subject, countdown, teleprompter), and what to show.
**Default:** do not add it. It is a new feature.

### Q9 Layout pattern for a custom two-pane or overlay screen (F02, F03)
**Options:** `NavigationSplitView` (master/detail with navigation) / `ArrangementView` split (both views must stay visible) / `ArrangementView` overlay (foreground over background) / leave it.
**Default:** the option that matches the current layout: HStack of panes → split, ZStack with a panel → overlay.

### Q10 Hinge feature (H01)
Only ask when the user mentions a fold-driven feature. Never offer the hinge as a layout fix.

### Q11 Verification help
**When:** you reach Phase 5 and cannot drive Xcode's Device Hub yourself.
**Ask:** "Please set the iPhone Duo simulator to <pose> in Device Hub and tell me when it's done." Ask for one pose at a time.
