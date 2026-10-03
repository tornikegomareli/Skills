---
id: no-activation-metric
title: No defined moment when a new user gets value
thinkers: [Lenny Rachitsky, Amol Avasare, Elena Verna, Andrew Chen]
applies_to: [all]
---

**Claim.** If a team has not defined and tracked the first moment a user gets core value, it cannot tell why new users leave or improve the stage that moves retention most.

## Why it is a problem
Lenny Rachitsky defines activation as the share of new users who reach a milestone where they first feel the product's core value. His 2022 survey found an average activation rate of 34% and a median of 25%. He warns against a milestone set too early (signup done) or too late (several purchases), and says it must predict retention. Growth leader Amol Avasare calls day-zero and day-one activation one of the biggest levers on long-term retention. Growth advisor Elena Verna describes the path as setup, then aha moment, then habit. Andrew Chen's data shows the average app loses 77% of daily users in the first 3 days, so the curve bends at activation, not later.

## How to detect
- Analytics code: search for tracking calls (`track(`, `logEvent`, `capture(`, `analytics.`). List the event names. Flag if the only events are `signup`, `login`, or `page_view`.
- Look for one named event for first value, such as `first_project_created`, `first_message_sent`, `first_payment`. If none exists, flag it.
- Spec or metrics doc: check that the activation milestone is written down with a time window (for example, within 7 days of signup).
- Check that the milestone is a user outcome, not a setup step. "Connected account" is setup. "Got first report" is value.
- If unclear, ask the intake question: "What is the first thing a new user does that shows they got value, and what share of signups do it?"

## Fixes
- Write one activation milestone with a time window. Add a tracking event for it.
- Compare retention of users who hit the milestone against users who did not. If the gap is small (Lenny suggests about 2x), pick a different milestone.
- Measure activation rate per weekly signup cohort and compare it with the category benchmark.

## Cases
- `superhuman-human-onboarding` (success)

## Sources
- https://www.lennysnewsletter.com/p/what-is-a-good-activation-rate (Lenny Rachitsky, 2022)
- https://www.lennysnewsletter.com/p/anthropics-1b-to-19b-growth-run (Amol Avasare, Lenny's Podcast, 2026)
- https://www.lennysnewsletter.com/p/the-new-ai-growth-playbook-for-2026-elena-verna (Elena Verna, Lenny's Podcast, 2025)
- https://andrewchen.com/new-data-shows-why-losing-80-of-your-mobile-users-is-normal-and-that-the-best-apps-do-much-better/ (Andrew Chen)
- Ideas read in Lenny's official starter dataset: https://github.com/LennysNewsletter/lennys-newsletterpodcastdata
