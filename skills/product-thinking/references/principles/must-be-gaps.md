---
id: must-be-gaps
title: Basic expected features missing while extras get built
thinkers: [Noriaki Kano]
applies_to: [all]
---

**Claim.** If a product lacks features users take for granted, users judge it as broken, and no amount of delight elsewhere makes up for it.

## Why it is a problem
The Kano model sorts features into must-be, performance, attractive, and indifferent. Must-be features only prevent dissatisfaction. Their absence makes people angry, but their presence adds no satisfaction, the way a hotel room must have a bed and running water. Attractive features delight only after the basics are there. Categories also decay over time: the iPhone touchscreen delighted people in 2007 and is a baseline today. Teams like to build attractive features because they demo well, so must-be gaps such as password reset or data export often ship late.

## How to detect
- Auth: check for password reset, email change, session expiry handling, and account deletion. Search routes and screens for `reset`, `forgot`, `delete account`.
- Data: check for export, import, and backup of user data. Search for `export`, `csv`, `download`.
- Safety: check for undo, confirm on destructive actions, and autosave or draft recovery.
- Basics by type: search, sort, and filter on list views; pagination on large lists; notification settings; billing receipts and cancel flow (b2b-saas); offline or retry handling (mobile).
- Compare against the top competitor's feature list or app store page. Must-be features there and missing here are flags.
- Count recent work on new or novel features against open issues for these basics.

## Fixes
- List the must-be features for this product type. Mark each as present, partial, or missing. Fix missing items before new attractive features.
- Run a short Kano survey (functional and dysfunctional question per feature) on 10 to 20 users to confirm which items are must-be.
- Re-check the list each year. Last year's delighters may be today's baseline.

## Cases
- `humane-ai-pin-unfinished-launch` (failure)

## Sources
- https://foldingburritos.com/blog/kano-model/ (secondary source; cites Kano et al. 1984, original paper not checked)
