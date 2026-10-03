---
id: launch-too-late
title: Launching too late
thinkers: [Paul Graham, Paul Buchheit, Y Combinator]
applies_to: [all]
---

**Claim.** A project that waits to launch until it feels complete loses months it could have spent learning what users need.

## Why it is a problem
Paul Graham says slow launches have killed about a hundred times more startups than early ones. He says software always feels 85% done, and most launch delays are procrastination in disguise. In "Startups in 13 Sentences" he argues that launching teaches you what you should have built, so the launch is mainly a way to start engaging users. YC's first piece of advice is to launch right away, with a product that has a "quantum of utility". Paul Buchheit's 90/10 rule supports this: find the version that gives 90% of the value for 10% of the work. Graham also warns against the big launch event. He cites Google Wave as a good idea hurt partly by an overdone launch.

## How to detect
- Check for a deployed URL, an app store link, a published package, or release tags. If none exist, compare that with the repo age from `git log`.
- Count commits since the first commit and the number of releases. Months of commits with zero releases is a flag.
- Read the roadmap or spec for a "v1" list. Flag it if the list has many features that must all be done before anyone can use the product.
- Search for a waitlist, a launch date far in the future, or a planned press launch with no users before it.
- Check whether features ship behind flags that are all off in production.
- If release history is not in the repo, ask intake question 10.

## Fixes
- Find the smallest subset that is useful on its own and can grow into the full product. Ship it to 5 to 10 real users this week.
- Cut the v1 list to what one user needs for one job. Move the rest to a post-launch list.
- Replace the big launch plan with a small, direct release to people you recruit by hand.

## Cases
- `college-conductor-stack-before-customer` (failure)
- `rethinkdb-wrong-quality-metrics` (failure)

## Sources
- https://www.paulgraham.com/startupmistakes.html
- https://www.paulgraham.com/13sentences.html
- https://www.paulgraham.com/ds.html
- https://www.ycombinator.com/library/4D-yc-s-essential-startup-advice
