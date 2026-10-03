---
id: untested-value-risk
title: Building before testing whether anyone wants it
thinkers: [Marty Cagan, Teresa Torres, Rahul Vohra]
applies_to: [all]
---

**Claim.** A project that commits build effort before it tests value risk bets the whole build on an unchecked assumption.

## Why it is a problem
Cagan names four product risks: value, usability, feasibility, and business viability. He says strong teams tackle value and viability risk early, before they build. Engineers check feasibility by default, so value is the risk teams skip most often. Torres says teams should test assumptions with small, fast tests before they invest in full development. Superhuman measured value directly: it asked users how they would feel if they could no longer use the product. In 2017 only 22% said "very disappointed", below the 40% bar Sean Ellis used as a sign of fit. Superhuman raised that to 58% in three quarters.

## How to detect
- Search the spec, README, and `docs/` for target users, interviews, surveys, waitlists, or experiments. If none exist, flag the project.
- Check for an analytics or event library in the dependencies. Check whether any event tracks the core action, and not only page views.
- Compare the number of features with the evidence of use for each one. Many features with no usage data is a flag.
- Look for a feedback channel inside the product: a feedback form, a survey prompt, or a support link.
- If the repo has no evidence, ask intake questions 1, 3, and 6 (last real person with the problem, how many seen, who went back to the old way).

## Fixes
- Write the riskiest value assumption as one sentence. Design the smallest test for it before more build work.
- Add tracking for the one core action. Define "used" as a number.
- Run the "very disappointed" survey on current users. Repeat it after each major change.

## Cases
- `app-net-developer-chicken-and-egg` (failure)
- `humane-ai-pin-unfinished-launch` (failure)
- `dropbox-demo-video` (success)

## Sources
- https://www.svpg.com/four-big-risks/
- https://www.producttalk.org/2021/08/product-discovery/
- https://review.firstround.com/how-superhuman-built-an-engine-to-find-product-market-fit/
