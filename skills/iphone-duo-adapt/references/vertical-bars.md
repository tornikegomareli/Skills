# Vertical bars (checks B01 to B07)

On iPhone Duo in landscape, the navigation bar, toolbar, and tab bar share one vertical bar on the side of the window. The system does this for you when two things are true:

1. The app is built with the iOS 27.1 SDK.
2. The bar content lives in a system container: SwiftUI `.toolbar` inside `NavigationStack` / `NavigationSplitView`, `TabView`; UIKit `navigationItem` and `toolbarItems` in a `UINavigationController`, `UITabBarController`.

Content of a custom `UIToolbar`, `UINavigationBar`, `UITabBar`, or a bar built from an `HStack`, is ignored. It stays horizontal.

All code below compiles against the iOS 27.1 SDK. Blocks marked `// min: 17.0` also compile with an iOS 17 deployment target.

## B01: Move a custom bar into the system toolbar

SwiftUI, before: an `HStack` in `.safeAreaInset(edge: .bottom)`. After: `ToolbarItem(placement: .bottomBar)` items. Give every item a title and a symbol.

```swift
// min: 17.0
struct EditorScreen: View {
    @State private var text = ""

    var body: some View {
        NavigationStack {
            TextEditor(text: $text)
                .toolbar {
                    ToolbarItemGroup(placement: .bottomBar) {
                        Button("Bold", systemImage: "bold") {}
                        Button("Italic", systemImage: "italic") {}
                        Button("List", systemImage: "list.bullet") {}
                        Spacer()
                        Button("Photo", systemImage: "photo") {}
                    }
                }
        }
    }
}
```

UIKit, before: a `UIToolbar()` added as a subview. After: `toolbarItems` on a view controller inside a `UINavigationController`, with the toolbar shown.

```swift
// min: 17.0
final class CameraScreenViewController: UIViewController {
    override func viewDidLoad() {
        super.viewDidLoad()
        toolbarItems = [
            UIBarButtonItem(title: "Flip", image: UIImage(systemName: "arrow.triangle.2.circlepath.camera"), target: self, action: #selector(flip)),
            .flexibleSpace(),
            UIBarButtonItem(title: "Capture", image: UIImage(systemName: "circle.inset.filled"), target: self, action: #selector(capture)),
            .flexibleSpace(),
        ]
    }

    override func viewWillAppear(_ animated: Bool) {
        super.viewWillAppear(animated)
        navigationController?.setToolbarHidden(false, animated: animated)
    }

    @objc private func flip() {}
    @objc private func capture() {}
}
```

The view controller must be inside a `UINavigationController`. If it is not, wrap it where it is created: `UINavigationController(rootViewController: CameraScreenViewController())`. If the app hides the navigation bar to draw its own, show the system bar again or ask (Q4).

## Item order in the vertical bar (Apple)

Top: back and close. Middle: prominent actions (Done). Bottom: everything else. Use the right placement and the system orders them:

- Close / cancel: SwiftUI `.cancellationAction`. UIKit `navigationItem.leadingItemGroups` with `leftItemsSupplementBackButton = false`.
- Prominent action: SwiftUI `.topBarPinnedTrailing` (iOS 27). UIKit `navigationItem.pinnedTrailingGroup`.

```swift
struct ComposeSheet: View {
    @Environment(\.dismiss) private var dismiss

    var body: some View {
        NavigationStack {
            Form { Text("Draft") }
                .toolbar {
                    ToolbarItem(placement: .cancellationAction) {
                        Button("Cancel", systemImage: "xmark") { dismiss() }
                    }
                    ToolbarItem(placement: .topBarPinnedTrailing) {
                        Button("Send", systemImage: "paperplane") {}
                    }
                }
        }
    }
}
```

## B03: Title and symbol on every item

A vertical bar has a fixed width. Items with a symbol move to it. Text-only items stay horizontal. Give both, and the system picks what to show (symbol in bars, symbol and title in the overflow menu).

- SwiftUI: `Button("Edit", systemImage: "pencil") {}` or a `Label`.
- UIKit: `UIBarButtonItem(title:image:target:action:)`, or set both `title` and `image`.

Keep an item text-only only when the text is data the user needs (a price, a count that is not a badge).

## B04: Custom views in bars

Set the axis on purpose:

- `.horizontalOnly`: the view changes between a symbol and text (a Select/Done toggle), or it cannot draw in a narrow column. It stays in the horizontal bars. If no horizontal bar is present, it is **not shown**, so put its action somewhere else too.
- `.verticalPreferred`: the view can draw in the narrow column. Adapt it with the bar edge.

```swift
struct CompassItem: View {
    @Environment(\.toolbarVerticalEdge) private var verticalEdge

    var body: some View {
        if verticalEdge == nil {
            Label("North", systemImage: "location.north")
        } else {
            Image(systemName: "location.north")
        }
    }
}

struct MapScreen: View {
    var body: some View {
        NavigationStack {
            Color.green
                .toolbar {
                    ToolbarItem { CompassItem() }
                        .axisBehavior(.verticalPreferred)
                }
        }
    }
}
```

```swift
final class MapViewController: UIViewController {
    override func viewDidLoad() {
        super.viewDidLoad()
        let compass = UIBarButtonItem(customView: UIImageView(image: UIImage(systemName: "location.north")))
        compass.axisBehavior = .verticalPreferred
        navigationItem.rightBarButtonItem = compass

        registerForTraitChanges(UITraitCollection.systemTraitsAffectingVerticalBarEdge) { (self: Self, _) in
            self.updateCompass()
        }
    }

    private func updateCompass() {
        switch traitCollection.verticalBarEdge {
        case .leading, .trailing: break // narrow layout
        default: break // horizontal layout
        }
    }
}
```

`toolbarVerticalEdge` (SwiftUI) and `traitCollection.verticalBarEdge` (UIKit) give the edge where the system would put the vertical bar. They are `nil` / `.unspecified` where the system never uses a vertical bar. Measured: `nil` on the outer display in closed portrait.

Gate for older deployment targets:

```swift
// min: 17.0
struct GatedToolbar: View {
    var body: some View {
        NavigationStack {
            Text("Map")
                .toolbar {
                    if #available(iOS 27.1, *) {
                        ToolbarItem { Image(systemName: "location.north") }
                            .axisBehavior(.verticalPreferred)
                    } else {
                        ToolbarItem { Image(systemName: "location.north") }
                    }
                }
        }
    }
}
```

## B05: Counts become badges

```swift
struct InboxToolbar: View {
    let unread: Int

    var body: some View {
        NavigationStack {
            List { Text("Message") }
                .navigationTitle("Inbox")
                .toolbar {
                    ToolbarItem {
                        Button("Inbox", systemImage: "tray") {}
                            .badge(unread)
                    }
                }
        }
    }
}
```

UIKit: `item.badge = .count(unread)`.

## B06: One overflow menu

The system shows an ellipsis menu when items overflow. Do not add a second ellipsis menu. Put extra actions in the system menu:

```swift
struct ListWithOverflow: View {
    var body: some View {
        NavigationStack {
            List { Text("Row") }
                .toolbar {
                    ToolbarOverflowMenu {
                        Button("Sort by Date", systemImage: "calendar") {}
                        Button("Sort by Title", systemImage: "textformat") {}
                    }
                }
        }
    }
}
```

```swift
final class ListViewController: UIViewController {
    override func viewDidLoad() {
        super.viewDidLoad()
        navigationItem.additionalOverflowItems = UIDeferredMenuElement { provide in
            provide([
                UIAction(title: "Sort by Date", image: UIImage(systemName: "calendar")) { _ in },
                UIAction(title: "Sort by Title", image: UIImage(systemName: "textformat")) { _ in },
            ])
        }
    }
}
```

If the menu must stay separate, give it a different symbol (for example `line.3.horizontal.decrease`).

## B07: Priority, compression, and opt-out

Which items overflow last: `.visibilityPriority(.high)` (SwiftUI, on the `ToolbarItem`) / `item.visibilityPriority = .high` (UIKit). Use it for the most used action (Compose, New Note) and for items with a badge.

Tab bar and toolbar together (decision Q3):

```swift
struct TaskFirstTab: View {
    var body: some View {
        TabView {
            Tab("Recents", systemImage: "clock") {
                NavigationStack {
                    Text("Recents")
                        .toolbarVerticalCompressionBehavior(.prefersToolbarItems)
                }
            }
        }
    }
}
```

UIKit: `navigationItem.verticalBarCompressionBehavior = .prefersBarItems`. The default (`.automatic`) prefers the tab bar.

Opt out on one screen (decision Q2):

```swift
struct CalculatorScreen: View {
    var body: some View {
        NavigationStack {
            Text("0")
                .toolbarVerticalBehavior(.disabled)
        }
    }
}

final class CalculatorViewController: UIViewController {
    override var preferredVerticalBarBehavior: UIVerticalBarBehavior { .disabled }
}
```

After a change that affects the UIKit value, call `setNeedsUpdateOfVerticalBarConfiguration()`. Container view controllers forward the preference to their visible child (`childForPreferredVerticalBarBehavior`).

## Custom bars that stay custom (Q4)

Place them with a bar layout region so the content inset matches the bar:

```swift
final class PaletteViewController: UIViewController {
    private let palette = UIView()

    override func viewDidLoad() {
        super.viewDidLoad()
        view.addSubview(palette)
        palette.translatesAutoresizingMaskIntoConstraints = false
        let guide = view.layoutGuide(for: .bar(onEdge: NSDirectionalRectEdge.bottom, extent: 56))
        NSLayoutConstraint.activate([
            palette.leadingAnchor.constraint(equalTo: guide.leadingAnchor),
            palette.trailingAnchor.constraint(equalTo: guide.trailingAnchor),
            palette.topAnchor.constraint(equalTo: guide.topAnchor),
            palette.bottomAnchor.constraint(equalTo: guide.bottomAnchor),
        ])
    }
}
```

Then check it against the division region in `fold-and-layout.md`.
