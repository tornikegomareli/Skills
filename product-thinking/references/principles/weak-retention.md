---
id: weak-retention
title: Users leave faster than new ones arrive
thinkers: [Jason Cohen, Mark Pincus, Jorge Mazal, Lenny Rachitsky]
applies_to: [all]
---

**Claim.** If the retention curve does not flatten, growth stops at a ceiling, and more acquisition only fills a leaking bucket.

## Why it is a problem
Jason Cohen (WP Engine founder) treats customer churn as the first question when growth slows. Churn is a percentage while new signups are a count, so the business stops growing when the two are equal. He also says the reason given on exit, such as price, is rarely the real reason. Mark Pincus says Zynga's core metric was retention, not virality, and calls viral products without retention sinking speedboats. At Duolingo, Jorge Mazal's team modeled user states and found that current-user retention (CURR) moved DAU 5 times more than the next lever. Raising CURR 21% helped grow DAU 4.5x over four years. Lenny's benchmarks put good 6-month user retention near 40% for consumer SaaS and 60% for SMB SaaS.

## How to detect
- Analytics: check for cohort retention (D1, D7, D30, or monthly by signup cohort). If the team only tracks totals such as total users, flag it.
- Check for a return trigger tied to a real event: email, push, or digest code and what fires it. Search for `cron`, `schedule`, `notification`, `digest`.
- Billing code: check for a cancel flow that asks why, and stores the answer. Search for `cancel`, `churn`, `reason`.
- Product: ask what brings a user back next week. If the spec has no recurring use case, flag it.
- If data exists, compute churn ceiling: monthly new customers divided by monthly churn rate. Compare with current customer count.
- Intake question: "What share of users who signed up three months ago still use the product each week?"

## Fixes
- Build a cohort retention chart. Find where the curve drops most and work on that stage first (often the first 30 days).
- Add one return mechanism tied to user value, such as a streak, a scheduled report, or an alert on new data.
- Interview churned users and ask follow-up "why" questions past the first answer.

## Cases
- `homejoy-growth-over-retention` (failure)
- `vinetrade-buying-was-the-fun` (failure)
- `duolingo-curr-growth-model` (success)

## Sources
- https://www.lennysnewsletter.com/p/why-your-product-stopped-growing (Jason Cohen, Lenny's Podcast, 2026)
- https://www.lennysnewsletter.com/p/the-common-pattern-behind-successful (Mark Pincus, Lenny's Podcast, 2026)
- https://www.lennysnewsletter.com/p/how-duolingo-reignited-user-growth (Jorge Mazal, guest post, 2023)
- https://www.lennysnewsletter.com/p/what-is-good-retention-issue-29 (Lenny Rachitsky, 2020)
- Ideas read in Lenny's official starter dataset: https://github.com/LennysNewsletter/lennys-newsletterpodcastdata
