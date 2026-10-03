---
id: wrong-early-metric
title: Tracking a number that does not show progress
thinkers: [Paul Graham, Joe Kraus, Y Combinator]
applies_to: [all]
---

**Claim.** An early project that tracks totals or vanity numbers will optimize the wrong thing, because teams improve what they measure.

## Why it is a problem
Paul Graham credits Joe Kraus with the idea that you make what you measure, so a team must choose the number carefully. In "Startup = Growth" he says the one number a founder must know is the growth rate. "A hundred new customers a month" is not a rate, and a fixed count each month means growth is slowing. YC measures growth weekly. Graham says 5 to 7% a week is good, 10% is exceptional, and 1% means the team has not found what works. The best base is revenue, and the next best is active users. He excludes tricks like counting inactive users as active. YC's essential advice says to pick one or two key metrics early and decide work by their effect on those metrics.

## How to detect
- Open the analytics or dashboard config. Flag it if the main charts are cumulative totals, page views, signups, or downloads.
- Check how "active user" is defined in code. If a login, an app open, or a page view counts as active, flag it.
- Check whether any report shows a week-over-week rate of revenue or active users.
- Read the spec or OKRs. If there is no named primary metric, or there are more than two, flag it.
- If metrics live outside the repo, ask intake questions 13 and 15.

## Fixes
- Pick one metric: revenue if the product charges, else users who did the core action this week.
- Define "active" as doing the core action, in code, in one place.
- Report the weekly growth rate of that metric. Set a target rate and review it every week.

## Cases
- `99dresses-fee-on-falling-value` (failure)
- `sonar-engagement-over-growth` (failure)
- `duolingo-curr-growth-model` (success)
- `superhuman-pmf-survey` (success)
- `google-plus-features-over-engagement` (failure)

## Sources
- https://www.paulgraham.com/13sentences.html
- https://www.paulgraham.com/growth.html
- https://www.ycombinator.com/library/4D-yc-s-essential-startup-advice
