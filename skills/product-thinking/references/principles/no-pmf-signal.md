---
id: no-pmf-signal
title: No signal that users would miss the product
thinkers: [Marc Andreessen, Rahul Vohra, Sean Ellis, Michael Seibel]
applies_to: [all]
---

**Claim.** Without a measured signal of product/market fit, a team cannot tell whether to keep iterating or start scaling, and it usually guesses wrong.

## Why it is a problem
Marc Andreessen argues that getting to product/market fit is the only thing that matters for a startup, and that most startups fail because they never reach it. He says the absence is easy to feel: usage grows slowly, word of mouth does not spread, and deals do not close. Rahul Vohra of Superhuman found Andreessen's signs useful but lagging. He adopted Sean Ellis's survey: ask users how they would feel if they could no longer use the product. Ellis found that companies above 40% "very disappointed" usually had strong traction. Superhuman scored 22% in 2017 and reached 58% within three quarters by focusing on that number. Michael Seibel warns that headcount and funding are not signs of fit.

## How to detect
- Search `docs/`, analytics config, and the codebase for a fit survey, a retention cohort, or an NPS-style prompt. If none exist, flag it.
- Check what the README, pitch, or status docs cite as proof of success. Signups, downloads, funding, or press are not fit signals.
- Check whether analytics can answer "how many users came back after 30 days". If it cannot, the team cannot see fit.
- Check whether users are segmented, for example by role or use case, so the team can see which group responds most.
- If the repo has no data, ask intake questions 6 and 14.

## Fixes
- Send the "very disappointed" survey to users who used the core feature at least twice in the last two weeks. About 40 responses give a direction.
- Add the three follow-up questions: who benefits most, the main benefit, and what to improve. Use them to pick the next work.
- Track the score over time. Hold off on scaling work until it is near or above 40%.

## Cases
- `ondsel-hobbyists-not-buyers` (failure)
- `instagram-burbn-pivot` (success)
- `superhuman-pmf-survey` (success)

## Sources
- https://pmarchive.com/guide_to_startups_part4.html
- https://review.firstround.com/how-superhuman-built-an-engine-to-find-product-market-fit/
- https://www.michaelseibel.com/blog/the-real-product-market-fit
