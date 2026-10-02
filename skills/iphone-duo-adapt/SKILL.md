---
name: iphone-duo-adapt
description: Audits an existing SwiftUI or UIKit iOS app for iPhone Duo (Apple's foldable iPhone, iOS 27.1) and then fixes every problem it finds. Use when the user asks to get an app ready for iPhone Duo or the foldable iPhone, to check or audit Duo support, or to fix layouts that break when the device opens, closes, folds, or runs in split view. Also use for vertical bars, reserved regions, the fold or hinge, ArrangementView, UIArrangementViewController, onHingeChange, UIHingeInteraction, camera direction on Duo, and CameraCaptureAccessory.
---

# iPhone Duo Adapt

This skill takes an existing app from "unknown" to "supports iPhone Duo". It runs in five phases: preflight, audit, decisions, fix, verify. Do not skip a phase. Do not start fixing before the audit report exists.

Every API in this skill was checked against the iOS 27.1 SDK in Xcode 27.1 (build 27A9269). Every code sample in `references/` compiles against that SDK. If you need an API that is not in `references/api-surface.md`, run `scripts/find-api.sh <name>` before you use it. Do not use an API from memory: most Duo APIs did not exist before September 2026.

## What changes on iPhone Duo

Read `references/device.md` before the audit. In short:

- The app moves between an outer display (closed, iPhone-like, 386×678 pt window) and a larger inner display (open, regular × regular size classes).
- The inner display ignores `UISupportedInterfaceOrientations`. Any aspect ratio can happen.
- In landscape, system navigation bars, toolbars, and tab bars move to a vertical bar on the leading or trailing side. Custom bars do not move.
- When the device is partially folded, a division reserved region crosses the screen. Interactive content must not sit on it.
- All apps join split view multitasking on the inner display.
- The front camera changes direction when the device opens and closes.

## Phase 1: Preflight (read only)

1. Run `scripts/preflight.sh <project-dir>`. It finds an Xcode with the iOS 27.1 SDK, the targets, the deployment target, the UI frameworks, the Info.plist keys, and the iPhone Duo simulator. It also finds Apple's `app-resizability` reference files inside Xcode 27.1.
2. If no Xcode with the iOS 27.1 SDK exists, stop. Tell the user that Duo layouts (full-screen inner display, vertical bars, reserved regions) need an app built with the iOS 27.1 SDK, and that Xcode 27.1 is required.
3. Build the app once, unchanged, with `scripts/build.sh <project-dir>`. Record whether it built. If it does not build before your changes, tell the user and ask whether to continue. You must be able to tell your own breakage apart from existing breakage.

## Phase 2: Audit

1. Run `python3 scripts/audit.py <project-dir>`. It prints one candidate per line: `CHECK-ID<TAB>file:line<TAB>code`, and a count per check on stderr. It parses plists (a key set to `NO` is not a finding) and matches multi-line toolbar items.
2. Grep finds candidates. It does not prove a problem. Open every flagged line, read the context, and decide: real problem, false positive, or needs a decision.
3. Some checks cannot be found with grep: custom layouts that put controls in the center of the screen, custom split layouts, and custom bars built from stacks. For these, read every top-level screen of the app (root views, view controllers that a navigation or tab container shows). The checks marked "manual" in `references/checks.md` tell you what to look for.
4. Write `DUO_AUDIT.md` in the project root. Use the template in `references/report-template.md`. Every finding has a check ID, a severity, a location, the evidence, and a planned fix.
5. Show the user a short summary: the number of findings per severity and the top 5 problems. Give the path to `DUO_AUDIT.md`.

The check catalog is `references/checks.md`. It is the source of truth for detection, severity, and the fix for each check.

## Phase 3: Decisions

Some fixes change product behavior. You must not guess them. `references/decisions.md` lists every decision point, when it applies, the default, and the question to ask.

- Collect all the decision points that apply to this app first. Then ask them together in one round, with your recommended option first. Use the AskUserQuestion tool when you have it. Ask at most 4 questions per round.
- For each question, say what you found in the code that raises it (file and line).
- If the user says "use your judgment" or the session is non-interactive, apply the default from `references/decisions.md` and list each default you applied in `DUO_AUDIT.md`.
- If you find a new ambiguity during the fix phase, stop and ask. Do not pick silently.

## Phase 4: Fix

Fix in this order. Each step builds on the one before it.

1. **Build settings and Info.plist** (checks D01 to D04). → `references/checks.md`
2. **Resizability foundation** (checks R01 to R05): `UIScreen.main`, orientation, idiom, scene lifecycle, asymmetric safe areas. If preflight found Apple's `app-resizability` files, read the matching Apple task file and follow it. It has the most complete decision trees. Otherwise use `references/resizability.md`.
3. **Bars** (checks B01 to B07): move custom bars into system containers and prepare items for vertical bars. → `references/vertical-bars.md`
4. **Fold and layout** (checks F01 to F05): reserved regions, arrangements, centered layouts. → `references/fold-and-layout.md`
5. **Scenes and multitasking** (checks S01 to S03). → `references/scenes.md`
6. **Camera** (checks C01 to C05), only if the app uses AVFoundation capture. → `references/camera.md`
7. **Hinge** (check H01), only if a hinge feature was agreed in Phase 3. → `references/hinge.md`

Rules for every fix:

- Keep the user's deployment target. If it is below iOS 27.1, wrap each new API in `if #available(iOS 27.1, *)` or `@available(iOS 27.1, *)`. Each reference shows the gated form.
- Change only what a finding needs. Do not reformat or refactor nearby code.
- Never replace a dynamic value with a literal. Never replace one global (`UIScreen.main`) with another (`UIApplication.shared.connectedScenes.first`).
- Prefer system containers (NavigationStack, NavigationSplitView, TabView, List, UINavigationController, UISplitViewController, UITabBarController) over custom code. They adapt to Duo with no extra work.
- Do not use hinge data (`onHingeChange`, `UIHingeInteraction`) for layout. Use size classes, reserved regions, and arrangements. Apple states this rule directly.
- Track progress in `DUO_AUDIT.md`: mark each finding `fixed`, `skipped (reason)`, or `needs user`. A finding with no status at the end is a failure.
- Build after each step with `scripts/build.sh`. If the build fails, fix it before you go to the next step.

## Phase 5: Verify

Follow `references/verification.md`. In short:

1. Run `python3 scripts/audit.py` again. Every remaining candidate must be a documented false positive or skip.
2. Build with the iOS 27.1 SDK. No new warnings from your changes.
3. Run `scripts/sim-capture.sh <project-dir>`. It installs the app on the iPhone Duo simulator, launches it, and saves a screenshot of each display to `<project-dir>/duo-captures/`. Do not commit that folder: add it to `.gitignore` if the project is a git repo. Look at the screenshots. Check for clipped content, content under the vertical status bar, and bars that stayed horizontal.
4. The simulator cannot be folded from the command line. Ask the user to change the pose in Xcode's Device Hub (open, partially open, landscape, split view), then run `scripts/sim-capture.sh --no-install` again for each pose. Check each result against the pose table in `references/verification.md`.
5. Update `DUO_AUDIT.md` with what you verified and how. Say plainly what you did not verify (for example, camera behavior needs a real device).

## Final report

Tell the user, in this order: what you changed (per phase), what you did not change and why, what needs their action (decisions, device testing), and the path to `DUO_AUDIT.md`. Do not call the app "Duo ready" unless Phase 5 passed.
