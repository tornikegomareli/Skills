# Fold and layout (checks F01 to F06)

Pick the lightest tool that solves the finding. In order:

1. **System containers** adapt with no work: `NavigationStack`, `NavigationSplitView`, `TabView`, `List`, `ScrollView`, `UINavigationController`, `UISplitViewController`, `UITabBarController`, `UICollectionView` with compositional layout. System presentations (alerts, action sheets, menus, popovers) already avoid the fold.
2. **Arrangements** for two views that a container does not cover: `ArrangementView` / `UIArrangementViewController`.
3. **Reserved regions** for custom placement of single controls: `reservedRegions(kind:)`.
4. **Hinge data** never for layout. See `hinge.md`.

All code compiles against the iOS 27.1 SDK. Blocks marked `// min: 17.0` also compile with an iOS 17 deployment target.

## Reserved regions

| Kind | What it is | Active when |
|---|---|---|
| `.division` | the fold | the device is partially folded |
| `.occlusion` | the camera on the inner display | the camera is in use |

Each region has `frame` (in the view's coordinate space, margins included), `margins`, `isActive`, `kind`, and `id`.

Always query with `.includeInactive` and filter yourself. Then the code does not depend on the default filter, and you can make high-level choices (such as an even number of grid columns) from inactive regions too.

### SwiftUI

```swift
struct FoldAwareControls: View {
    var body: some View {
        GeometryReader { proxy in
            let folds = proxy.reservedRegions(kind: .division, options: .includeInactive)
            let activeFold = folds.first(where: \.isActive)
            ControlsRow()
                .frame(maxWidth: .infinity)
                .position(controlsPosition(in: proxy.size, avoiding: activeFold?.frame))
        }
    }

    /// Centered, unless an active fold runs through the center: then on the trailing half.
    private func controlsPosition(in size: CGSize, avoiding fold: CGRect?) -> CGPoint {
        let center = CGPoint(x: size.width / 2, y: size.height / 2)
        guard let fold, fold.height > fold.width, fold.minX < center.x, fold.maxX > center.x else {
            return center
        }
        return CGPoint(x: (fold.maxX + size.width) / 2, y: center.y)
    }
}

struct ControlsRow: View {
    var body: some View {
        HStack(spacing: 40) {
            Button("Back", systemImage: "backward.fill") {}
            Button("Play", systemImage: "play.fill") {}
            Button("Forward", systemImage: "forward.fill") {}
        }
        .labelStyle(.iconOnly)
        .font(.largeTitle)
    }
}
```

A division region taller than wide means the fold is vertical (book). Wider than tall means the fold is horizontal (propped on a table): put content to watch in the top region and controls in the bottom region.

`reservedRegions` has a `layoutDirectionBehavior:` parameter. The default `.mirrors` flips frames in right-to-left layouts, like the rest of SwiftUI.

### UIKit

```swift
final class PlayerViewController: UIViewController {
    private let controls = UIStackView()

    override func viewDidLayoutSubviews() {
        super.viewDidLayoutSubviews()
        let bounds = view.bounds.inset(by: view.safeAreaInsets)
        var target = bounds
        let fold = view.reservedRegions(kind: .division, options: .includeInactive).first(where: \.isActive)
        if let fold, fold.frame.height > fold.frame.width, fold.frame.intersects(CGRect(x: bounds.midX - 1, y: bounds.minY, width: 2, height: bounds.height)) {
            // Vertical fold through the middle: use the trailing half.
            target = CGRect(x: fold.frame.maxX, y: bounds.minY, width: bounds.maxX - fold.frame.maxX, height: bounds.height)
        }
        let size = controls.systemLayoutSizeFitting(UIView.layoutFittingCompressedSize)
        controls.frame = CGRect(x: target.midX - size.width / 2, y: target.midY - size.height / 2, width: size.width, height: size.height)
    }
}
```

Gate for older deployment targets:

```swift
// min: 17.0
extension UIView {
    /// The active fold frame in this view's coordinates, or nil.
    var activeFoldFrame: CGRect? {
        guard #available(iOS 27.1, *) else { return nil }
        return reservedRegions(kind: .division, options: .includeInactive).first(where: \.isActive)?.frame
    }
}
```

Unverified: Apple's material does not name a change callback for reserved regions. Read them during layout (`viewDidLayoutSubviews`, `layoutSubviews`, `GeometryReader`), then confirm in Device Hub that the layout updates when you fold. Record the result in `DUO_AUDIT.md`.

## Displacement rules (Apple)

- Move only what the fold blocks. Move controls that work together as one group.
- Do not move scrolling content (lists, feeds, articles, documents). It adapts by scrolling.
- Book pose: when several places fit, keep content in context (a search field stays near the keyboard). Alerts move to the trailing side.
- Table pose: top region for content to watch, bottom region for controls.
- Grids: keep the outer margins and add spacing around the fold.

## F02 / F03: Arrangements

An arrangement puts two views next to each other or on top of each other, and adapts to the size class, the aspect ratio, and the fold. It sits between the navigation container and the content.

Rules (Apple):
- Do not put a navigation container (`NavigationStack`, `NavigationSplitView`, `TabView`) inside an arrangement.
- Do not put an arrangement inside `List`, `ScrollView`, or another scrolling container.
- Split when the two views have a main/detail relationship and neither may be hidden (player + transcript). Overlay when there is a foreground and a background, and the background can be partly covered (map + panel).
- For master/detail with navigation, use `NavigationSplitView` instead.

### Split

```swift
struct LibraryScreen: View {
    var body: some View {
        NavigationStack {
            ArrangementView {
                NotesListPane()
            } secondary: {
                NoteDetailPane()
            }
            .arrangementViewStyle(.split)
        }
    }
}

struct NotesListPane: View {
    var body: some View { Text("List") }
}

struct NoteDetailPane: View {
    var body: some View { Text("Detail") }
}
```

The split style divides side by side when the view is wider than tall, and top to bottom when it is taller than wide. `.split.axes(.horizontal)` allows only side by side. When that is not possible, only the **primary** view is shown, so the primary must work alone.

Size a pane with modifiers on the pane itself, not on the `ArrangementView`: `splitArrangementLayoutRatio(_:)`, `splitArrangementLayoutSize(minWidth:idealWidth:maxWidth:...)`, `splitArrangementFixedLayoutSize(horizontal:vertical:)`.

```swift
struct SizedSplit: View {
    var body: some View {
        ArrangementView {
            Text("Sidebar")
                .splitArrangementLayoutSize(minWidth: 280, idealWidth: 320)
        } secondary: {
            Text("Content")
        }
        .arrangementViewStyle(.split.axes(.horizontal))
    }
}
```

Replace a GeometryReader split (`.frame(width: geo.size.width * 0.35)`) with a ratio or size on the pane. Remove the GeometryReader if nothing else uses it.

Gate for older deployment targets. Keep the old layout as the fallback:

```swift
// min: 17.0
struct GatedLibrary: View {
    var body: some View {
        if #available(iOS 27.1, *) {
            ArrangementView {
                Text("List")
            } secondary: {
                Text("Detail")
            }
            .arrangementViewStyle(.split)
        } else {
            GeometryReader { geo in
                HStack(spacing: 0) {
                    Text("List").frame(width: geo.size.width * 0.35)
                    Divider()
                    Text("Detail").frame(maxWidth: .infinity)
                }
            }
        }
    }
}
```

### Overlay

```swift
struct MapWithPanel: View {
    var body: some View {
        NavigationStack {
            ArrangementView {
                PanelPane()
            } secondary: {
                Color.green // the map
            }
            .arrangementViewStyle(.overlay)
        }
    }
}

struct PanelPane: View {
    @Environment(\.overlayArrangementZIndex) private var zIndex

    var body: some View {
        // Apple's sample: collapse the panel while it overlays the other view.
        List { Text(zIndex > 0 ? "Collapsed" : "Expanded") }
    }
}
```

`overlayArrangementEdge(_:)` on a pane chooses the edge it takes when the overlay moves to side by side (for example when folded).

Unverified: a community measurement reported `overlayArrangementZIndex` as 0 in both layouts. Do not make a pane unusable based on it. Check the value in Device Hub and record it.

### UIKit

```swift
final class PlayerContainerBuilder {
    @MainActor static func make() -> UIViewController {
        let arrangement = UIArrangementViewController()
        arrangement.setViewController(UIViewController(), for: .primary)
        arrangement.setViewController(UIViewController(), for: .secondary)
        arrangement.updateArrangement(.split.axes(.horizontal))
        return UINavigationController(rootViewController: arrangement)
    }
}

final class UpNextViewController: UIViewController {
    override func viewDidLayoutSubviews() {
        super.viewDidLayoutSubviews()
        let state = arrangementViewController?.state(for: .secondary)
        let collapsed = (state?.zIndex ?? 0) > 0 || state?.isHidden == true
        view.alpha = collapsed ? 0.9 : 1
    }
}
```

Size panes with `UISplitArrangement.ViewProperties`:

```swift
@MainActor func sidebarArrangement() -> UISplitArrangement {
    var split = UISplitArrangement.split.axes(.horizontal)
    var sidebar = split.defaultViewProperties
    sidebar.width.minimum = .absolute(280)
    sidebar.width.preferred = .fractional(0.35)
    split.setViewProperties(sidebar, for: .primary)
    return split
}
```

## F04: Grids

Derive the column count from the width. When a division region exists (active or not), prefer an even count so the fold falls between columns.

```swift
struct FoldAwareGrid: View {
    var body: some View {
        GeometryReader { proxy in
            let hasFold = !proxy.reservedRegions(kind: .division, options: .includeInactive).isEmpty
            let fit = max(2, Int(proxy.size.width / 120))
            let count = hasFold && fit % 2 == 1 ? fit - 1 : fit
            ScrollView {
                LazyVGrid(columns: Array(repeating: GridItem(.flexible()), count: count)) {
                    ForEach(0..<60, id: \.self) { _ in
                        RoundedRectangle(cornerRadius: 8).aspectRatio(1, contentMode: .fit)
                    }
                }
                .padding()
            }
        }
    }
}
```

`GridItem(.adaptive(minimum:))` is a simpler fix when an even count does not matter.

## F05: Foreground in the safe area

Only the background ignores the safe area:

```swift
// min: 17.0
struct PlayerBackground: View {
    var body: some View {
        VStack {
            Spacer()
            Button("Play", systemImage: "play.fill") {}
        }
        .frame(maxWidth: .infinity, maxHeight: .infinity)
        .background(Color.black.ignoresSafeArea())
    }
}
```

## F06: One adaptive container

Do not swap `NavigationStack` and `NavigationSplitView` on the size class. The size class changes each time the device opens or closes, and the swap destroys navigation state. `NavigationSplitView` already collapses to a stack in compact width:

```swift
// min: 17.0
struct AdaptiveRoot: View {
    @State private var selection: String?
    private let items = ["A", "B", "C"]

    var body: some View {
        NavigationSplitView {
            List(items, id: \.self, selection: $selection) { Text($0) }
        } detail: {
            Text(selection ?? "Select an item")
        }
    }
}
```

If the app needs different behavior in compact width, keep one container and change its content, not the container.
