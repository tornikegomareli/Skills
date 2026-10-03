---
id: usability-heuristic-violations
title: Interface breaks basic usability heuristics
thinkers: [Jakob Nielsen, Don Norman]
applies_to: [consumer, b2b-saas, dev-tool, marketplace, ai-product]
---

**Claim.** If an interface breaks well-known usability rules, users make errors, get lost, and give up, even when the feature itself has value.

## Why it is a problem
Jakob Nielsen's 10 usability heuristics (1994, updated 2024) are general rules for interface design. They include visibility of system status, match with the real world, user control and freedom, consistency, error prevention, recognition over recall, flexibility, minimalist design, error recovery, and help. Cagan calls this usability risk, one of the four big risks, owned by the designer. Don Norman's work on everyday things makes the same case from another angle: when people fail with a product, the cause is usually the design, not the user.

## How to detect
- User control (heuristic 3): search destructive actions (`delete`, `remove`, `archive`) for undo or confirm. Check that modals and flows have a cancel or back path.
- Consistency (heuristic 4): grep for button labels and terms. Flag the same action with different names ("Save", "Submit", "Apply") or the same name for different actions.
- Error prevention (heuristic 5): check form inputs for type, format constraints, and defaults. Check that invalid actions are disabled, and not only rejected after submit.
- Recognition over recall (heuristic 6): flag flows that need users to type IDs, codes, or names that the UI could offer as a list.
- Match with real world (heuristic 2): grep UI strings for internal names, enum values, or stack terms shown to users (`null`, `undefined`, `ERR_`, DB field names).
- Help (heuristic 10): check for empty-state guidance, tooltips on icon-only buttons, and a docs link.
- Run a heuristic review: walk the main flow and log each violation with its heuristic number and severity.

## Fixes
- Run a heuristic evaluation of the core flow. Fix high-severity items first.
- Add undo or confirm to every destructive action.
- Write a short glossary of UI terms. Use one word per action across the app.

## Cases
- `windows-8-start-menu-removal` (failure)
- `snapchat-2018-redesign` (failure)
- `hawaii-missile-alert-same-prompt` (failure)
- `therac-25-cryptic-malfunction` (failure)

## Sources
- https://www.nngroup.com/articles/ten-usability-heuristics/ (heuristics by Jakob Nielsen; credited and linked as the page asks)
- https://www.svpg.com/four-big-risks/
- https://jnd.org/books/the-design-of-everyday-things-revised-and-expanded-edition/
