# DUO_AUDIT.md template

Write this file to the project root in Phase 2. Update it in Phases 3 to 5. Keep it factual: file and line, what you saw, what you did.

```markdown
# iPhone Duo audit: <App name>

- Date: <YYYY-MM-DD>
- Xcode: <version (build)>, SDK: iOS <version>
- Targets: <app targets>; deployment target iOS <X>
- UI: SwiftUI | UIKit | both; lifecycle: SwiftUI App | scenes | app delegate only
- Camera capture: yes | no
- Baseline build before changes: succeeded | failed (<first error>)

## Summary

| Severity | Found | Fixed | Skipped | Needs user |
|---|---|---|---|---|
| Blocker | | | | |
| High | | | | |
| Medium | | | | |
| Low | | | | |

## Findings

| ID | Check | Severity | Location | Evidence | Fix | Status |
|---|---|---|---|---|---|---|
| 1 | R04 | Blocker | AppDelegate.swift:5 | no scene manifest, `var window` | adopt UIWindowSceneDelegate | fixed |
| 2 | B01 | High | CameraViewController.swift:8 | custom `UIToolbar()` | move items to `toolbarItems` | needs user (Q4) |

Status is one of: `open`, `fixed`, `skipped (<reason>)`, `false positive (<reason>)`, `needs user (<Q-id>)`.

## Decisions

| Question | Answer | Source |
|---|---|---|
| Q0 deployment target | keep iOS 16, gate APIs | user |

## Defaults applied

List every decision where you used the default because the user did not answer.

## Verification

| Step | Result | Evidence |
|---|---|---|
| Re-audit | 0 open findings | `audit.py` output |
| Build (iOS 27.1 SDK) | succeeded, 0 new warnings | |
| Closed, portrait | ok | screenshot path |
| Open, flat | ok / not verified | |
| Book (partially open) | | |
| Landscape (vertical bars) | | |
| Split view, left and right | | |
| Camera on device | not verified (simulator has no camera) | |

## Not done

Everything the user must still do or check, in one list.
```
