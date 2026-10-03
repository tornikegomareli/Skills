---
id: poor-feedback-and-errors
title: Users cannot tell what happened or how to recover
thinkers: [Don Norman, Jakob Nielsen]
applies_to: [all]
---

**Claim.** If the product does not show what it is doing and does not explain failures, users repeat actions, lose work, and stop trusting it.

## Why it is a problem
Don Norman described two gulfs in 1986. The gulf of execution is the gap between what users want to do and how to do it. The gulf of evaluation is the gap between what happened and whether users can tell. Feedback closes the second gulf, and Norman lists it as a core principle of interaction. Nielsen's first heuristic asks the system to keep users informed with timely feedback. His ninth asks for errors in plain language that name the problem and suggest a fix. NN/g's error guidelines add: show the error next to its cause, do not blame the user, and keep the user's input.

## How to detect
- Async calls: for each network or long-running call in UI code, check for a loading state, a success state, and an error state. Flag calls with a `catch` that only logs (`console.error`, `print`) or swallows the error.
- Buttons that start work: check that they disable or show progress while the request runs. Missing this leads to double submits.
- Error strings: grep for generic text ("Something went wrong", "Error", "An error occurred", raw `error.message`, status codes). Flag messages with no cause and no next step.
- Forms: check that validation errors appear next to the field and that input is kept after a failed submit.
- CLI and dev tools: check that errors name the failing input and suggest a fix. Flag stack traces shown as the only output.
- Long tasks: check for progress indicators on uploads, exports, AI generation, and builds.
- Silent success: check that saves, sends, and deletes confirm the result (toast, state change, or message).

## Fixes
- Add a shared pattern for async state (loading, success, error) and use it on every network call.
- Rewrite generic errors: say what failed, why if known, and what to do next. Keep the user's input.
- Add progress or streaming for any action that takes more than a moment.

## Cases
- `hawaii-missile-alert-same-prompt` (failure)
- `therac-25-cryptic-malfunction` (failure)

## Sources
- https://www.nngroup.com/articles/two-ux-gulfs-evaluation-execution/
- https://www.nngroup.com/articles/ten-usability-heuristics/ (heuristics by Jakob Nielsen; credited and linked as the page asks)
- https://www.nngroup.com/articles/visibility-system-status/
- https://www.nngroup.com/articles/error-message-guidelines/
- https://jnd.org/books/the-design-of-everyday-things-revised-and-expanded-edition/
