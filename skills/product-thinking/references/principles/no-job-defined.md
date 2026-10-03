---
id: no-job-defined
title: No customer job or circumstance defined
thinkers: [Clayton Christensen]
applies_to: [all]
---

**Claim.** If a product describes its users by demographics or features and never by the progress they want in a specific situation, it cannot tell which features matter.

## Why it is a problem
Jobs to Be Done theory, from the Christensen Institute, says people "hire" a product to make progress toward a goal in a given circumstance. The circumstance decides the job, and the same person can have different jobs at different times. Every job has functional, social, and emotional sides. The Institute's milkshake example shows this: morning buyers hired a milkshake to fill a dull commute and stay full, while afternoon buyers hired it as a treat for children. One product, two jobs, two different sets of features. A spec built on personas like "busy professionals, 25 to 40" gives no such guidance.

## How to detect
- Search the spec, README, and `docs/` for a situation statement: when the user hits the problem, what they try to get done, and what "done" looks like. Flag the project if users are described only by role, age, or "everyone".
- Check whether the spec names the moment that triggers use (an event, a deadline, a handoff). If no trigger exists, flag it.
- Check whether any requirement covers social or emotional needs (confidence, looking competent to a boss, less anxiety). If all are functional, note it.
- Look at onboarding copy and empty states. Check whether they speak to a situation or only list features.
- If the docs are silent, ask intake questions 1, 2, and 5 (last real person, when they hit it, what made them look for something better).

## Fixes
- Write one job statement: "When [situation], I want to [progress], so I can [outcome]." Test every feature against it.
- Interview 3 to 5 recent users about the day they started using the product. Record the trigger and what they used before.
- If two different jobs appear, pick one for the next release and cut the features that only serve the other.

## Cases
- `rethinkdb-wrong-quality-metrics` (failure)
- `vinetrade-buying-was-the-fun` (failure)
- `figma-multiplayer-browser` (success)

## Sources
- https://www.christenseninstitute.org/theory/jobs-to-be-done/ (Christensen Institute copyrighted material, paraphrased)
