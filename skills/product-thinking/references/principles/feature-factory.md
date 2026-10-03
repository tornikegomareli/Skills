---
id: feature-factory
title: Shipping features is the goal instead of outcomes
thinkers: [John Cutler, Marty Cagan, Teresa Torres]
applies_to: [all]
---

**Claim.** A team that measures progress by features shipped keeps adding scope without knowing whether any of it helped users or the business.

## Why it is a problem
In a 2016 post, John Cutler listed 12 signs of a "feature factory". Among them: no measurement of impact, celebrating launches instead of results, roadmaps that are only feature lists, and moving on without iterating on data. Cagan makes the same split between feature teams and product teams. Feature teams get a roadmap of features and dates and are judged on output. Product teams get problems to solve and are judged on outcomes. Torres puts an outcome at the root of discovery so each solution has a test it can fail.

## How to detect
- Roadmap or tracker: read `ROADMAP.md`, milestones, or project boards. Flag items that are only feature names with no problem or metric.
- Changelog: read `CHANGELOG.md` or release notes. If entries list features but never results or follow-ups, note it.
- Iteration: check git history for features that got follow-up changes after launch. Most features with one launch commit and no later tuning is a sign.
- Measurement: check whether shipped features have analytics events. Count features with no event.
- Removal: search history for removed or reverted features. A product that never removes anything may not measure.
- Feature flags: check for experiments or flags with a success metric. Flags used only for rollout, never for comparison, are a weak sign.
- Ask intake question 15 (the number used for the last product decision).

## Fixes
- Rewrite the top 5 roadmap items as problems with a target metric.
- Add a post-launch check to each feature: the metric, the date to review, and the keep, change, or remove decision.
- Remove or hide one feature with no usage. Record the result.

## Cases
- `evernote-feature-sprawl` (failure)
- `google-plus-features-over-engagement` (failure)

## Sources
- https://cutle.fish/blog/12-signs-youre-working-in-a-feature-factory
- https://www.svpg.com/product-vs-feature-teams/
- https://www.producttalk.org/opportunity-solution-trees/
