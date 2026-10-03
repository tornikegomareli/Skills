# Hinge (check H01)

Use hinge data only for effects that respond to the physical act of folding: an instrument, a game control, an animation. Apple states the rule directly: layout belongs to size classes, reserved regions, and arrangements, never to the hinge.

The hinge has a discrete `status` (closed, partially open, fully open) and a continuous `angle`. The update rate and precision are system policy: do not depend on them. If you only need to know whether the device is folded, use `status`, not the angle. A `nil` hinge means the device has no hinge (every other iPhone), or the view left a hierarchy with hinge updates. Always handle `nil`.

All code compiles against the iOS 27.1 SDK. Blocks marked `// min: 17.0` also compile with an iOS 17 deployment target.

## SwiftUI

`DeviceHinge.Status` is a struct, not an enum. Compare with `==`. A `switch` needs a `default` case.

```swift
struct InstrumentView: View {
    /// 0 is no bend, 1 is the deepest bend.
    @State private var pitchBend = 0.0

    var body: some View {
        Text("Bend \(pitchBend, format: .number.precision(.fractionLength(2)))")
            .onHingeChange { _, context in
                if let hinge = context.hinge, hinge.status == .partiallyOpen {
                    pitchBend = bend(for: hinge.angle)
                } else {
                    pitchBend = 0
                }
            }
    }

    /// Map the angle to 0...1. The range of angles is not documented: clamp.
    private func bend(for angle: Angle) -> Double {
        min(max(1 - angle.degrees / 180, 0), 1)
    }
}
```

## UIKit

The angle is a `CGFloat` in **radians**. `UIHinge.Status` has an `.unknown` case. The handler runs with the initial state and on each update. It escapes: capture `self` weakly.

```swift
final class InstrumentViewController: UIViewController {
    private var pitchBend: CGFloat = 0

    override func viewDidLoad() {
        super.viewDidLoad()
        let interaction = UIHingeInteraction { [weak self] _, update in
            guard let self else { return }
            guard let hinge = update.hinge, hinge.status == .partiallyOpen else {
                self.pitchBend = 0
                return
            }
            self.pitchBend = min(max(1 - hinge.angle / .pi, 0), 1)
        }
        view.addInteraction(interaction)
    }
}
```

Set `interaction.isEnabled = false` while the effect is not on screen. When enabled again, the handler gets the current state.

## Gating

```swift
// min: 17.0
struct GatedInstrument: View {
    @State private var bend = 0.0

    var body: some View {
        if #available(iOS 27.1, *) {
            Text("Bend \(bend)")
                .onHingeChange { _, context in
                    bend = context.hinge?.status == .partiallyOpen ? 0.5 : 0
                }
        } else {
            Text("Bend \(bend)")
        }
    }
}
```

The feature must have another way in (a slider, a gesture) on devices with no hinge.
