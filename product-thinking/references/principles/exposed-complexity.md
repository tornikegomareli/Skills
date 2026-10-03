---
id: exposed-complexity
title: Internal complexity pushed onto the user
thinkers: [Steve Jobs, Jason Fried, David Heinemeier Hansson, Kathy Sierra]
applies_to: [all]
---

**Claim.** When the product shows its internal parts, settings, and choices to the user, the user spends effort on the tool instead of the goal.

## Why it is a problem
Jobs said the LaserWriter could be sold because the buyer did not need to know what was in the box. The Mac team aimed for a computer that was simple to use at a time when computers were hard to use. Kathy Sierra calls each small friction a cognitive leak. Mental effort is limited, so effort spent on the tool is taken from the user's real task. She compares a theme picker with many choices to a product that ships good defaults. 37signals reaches the same result in "Avoid Preferences" and "Zero Training": make the call for the user, and put help at the point of confusion.

## How to detect
- Count settings, flags, and config keys. Flag required config before first use, and settings with no clear default.
- Search UI strings and error messages for internal terms: table names, status codes, enum values, stack traces, "null", "undefined".
- Walk the main flow in the UI or CLI. Flag steps where the user must pick an option that the product could pick for them.
- Check onboarding docs. Flag setup that needs more than one screen of instructions for the main use case.
- Check whether the product uses internal names (service, job, worker) where the user would use a task name.

## Fixes
- Choose a default for every setting. Remove settings that almost nobody changes.
- Rewrite user-facing text in the user's words. Map every error to a plain cause and a next step.
- Hide advanced options behind one "Advanced" entry. Keep the main flow free of them.

## Cases
- `apple-1997-product-grid` (success)
- `linear-opinionated-workflow` (success)

## Sources
- https://www.youtube.com/watch?v=yQ16_YxLbB8 (WWDC 1997 closing Q&A, third-party upload; read via auto-captions)
- https://stevejobsarchive.com/stories/40-years-of-macintosh
- https://businessofsoftware.org/2014/05/building-the-minimum-badass-user-pt-2-unfinished-business-kathy-sierra/
- https://basecamp.com/gettingreal/06.4-avoid-preferences
- https://basecamp.com/gettingreal/14.2-zero-training
