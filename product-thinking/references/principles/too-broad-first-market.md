---
id: too-broad-first-market
title: First market too broad to win
thinkers: [Paul Graham, Paul Buchheit, Y Combinator]
applies_to: [all]
---

**Claim.** A product that tries to serve everyone at launch satisfies nobody fully, so it gets no group of users who need it badly.

## Why it is a problem
Paul Graham says a new product must choose between many people who want it a little and few people who want it a lot, and he says to pick the few. He calls this shape a well: narrow and deep. Microsoft's first product, Altair Basic, served only a couple thousand Altair owners. Facebook started only at Harvard, and Zuckerberg built course lists for each school so students felt the site was made for them. Graham credits Paul Buchheit with the rule that it is better to make a few users very happy than many users mildly happy. YC repeats it: 10 customers with a burning problem beat 1000 with a mild annoyance. YC also says Twitch took off only after it focused on video game streamers.

## How to detect
- Read the README, landing copy, and spec. Count the target user types. More than one primary persona at launch is a flag.
- Check for "for everyone", "for any team", or "for businesses of all sizes" in the positioning.
- Count integrations, locales, platforms, and pricing tiers planned for v1. Many of each before the first users is a flag.
- Check whether onboarding or settings branch by user type or industry. Many branches suggest no chosen first market.
- If the repo does not say who the first users are, ask intake questions 1 and 10.

## Fixes
- Pick one group that feels the problem most and is easy to reach. Rewrite the README first paragraph for that group only.
- Cut or hide features, integrations, and locales that only other groups need.
- Name the next group you will expand to, and the reason the first group leads to it.

## Cases
- `pebble-time-repositioning` (failure)
- `superhuman-pmf-survey` (success)

## Sources
- https://www.paulgraham.com/startupideas.html
- https://www.paulgraham.com/13sentences.html
- https://www.paulgraham.com/ds.html
- https://www.ycombinator.com/library/4D-yc-s-essential-startup-advice
