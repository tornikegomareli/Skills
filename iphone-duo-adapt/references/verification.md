# Verification (Phase 5)

Do the steps in order. Record each result in the Verification table of `DUO_AUDIT.md`, with evidence (command output, screenshot path). If a step cannot run, write "not verified" and why.

## 1. Re-audit

```sh
python3 scripts/audit.py <project-dir>
```

Compare with the first run. Every remaining candidate must be marked in `DUO_AUDIT.md` as a false positive or a documented skip.

## 2. Build

```sh
scripts/build.sh <project-dir>
```

The build must succeed with the iOS 27.1 SDK. Compare warnings with the baseline build from Phase 1: your changes must add none. If the deployment target is below 27.1, a missing `#available` shows up here as an error.

## 3. Screenshots in the iPhone Duo simulator

```sh
scripts/sim-capture.sh <project-dir> [label]
```

It builds, installs, and launches the app on the iPhone Duo simulator, then saves one screenshot per display to `duo-captures/<label>-<display>.png`. Only the display in use shows the app; the other is black. Read the screenshot with the image tool and check it against the table below.

The command line cannot fold the simulator. For every other pose, ask the user (decision Q11) to set the pose in Xcode 27.1's Device Hub, one pose at a time, then run:

```sh
scripts/sim-capture.sh --no-install <project-dir> <pose-label>
```

## 4. Pose table

| Pose | How | Check |
|---|---|---|
| Closed, portrait | default after boot | nothing under the vertical status bar on the right; with a tab bar, the tab bar and symbol items sit in a vertical bar on the right; no text-only item left alone at the top |
| Closed, landscape | rotate | bars moved to a vertical bar; content not squeezed by a custom bar |
| Open, portrait | Device Hub: open | layout uses the width (regular × regular): sidebars or two panes where planned; bars horizontal |
| Open, landscape | Device Hub: open, rotate | vertical bar on the side; custom views in bars readable |
| Book (partially open) | Device Hub: fold | no control or text on the fold; split views keep both columns |
| Split view, left and right | drag the app by the home indicator | app works at both widths; the vertical bar is on the outer edge |
| Open → closed → open | Device Hub | navigation state, scroll position, text input, and sheets survive |

For the last row, open a detail screen and a sheet, type text, then close and open the device. Nothing may reset.

## 5. What the simulator cannot verify

- Camera capture, camera direction, mirroring, and the camera capture accessory. Ask the user to test on a device and list the exact steps (open and close while recording; flip the open device).
- Hinge angle feel for H01 features.
- Performance of the resize animation on a device.

List these under "Not done" in `DUO_AUDIT.md`.
