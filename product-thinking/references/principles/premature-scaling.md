---
id: premature-scaling
title: Building for scale before anyone loves the product
thinkers: [Paul Graham, Michael Seibel, Y Combinator]
applies_to: [all]
---

**Claim.** Work spent on scale, automation, and hiring before product/market fit is wasted, because the team does not yet know what to build.

## Why it is a problem
YC's essential advice says many advisors push startups to scale too early, and the technology and processes built for that scale become wasted effort. YC tells founders to get the first customers by any means, including manual work that would not work for 100 customers. Paul Graham gives Stripe as an example: early "instant" merchant accounts were set up by hand by the founders. He says a manual process that solves a real problem is less risky than an automated one that solves no one's problem. Michael Seibel adds that founders who wrongly think they have fit start to hire, raise burn, and optimize the product too soon.

## How to detect
- Check the infrastructure files: Kubernetes manifests, Terraform, multi-region config, autoscaling, sharding, message queues, or a microservice split. Compare that with the user count. Heavy infrastructure with fewer than about 100 active users is a flag.
- Compare the amount of code for admin tools, billing tiers, role systems, and internal dashboards with the code for the core user action.
- Search the spec and roadmap for hiring plans, a sales team, or growth campaigns before any retention data exists.
- Look for automation of a step that has run only a few times (onboarding pipelines, matching engines, auto-provisioning). Ask if it was ever done by hand.
- If usage numbers are not in the repo, ask intake questions 13 and 14.

## Fixes
- Freeze scaling work. Run the product on the simplest setup that serves current users.
- Replace one planned automation with a manual step done by the team. Automate it only after you have done it by hand many times.
- Set a fit signal (for example, the "very disappointed" survey or a retention number) that must be met before hiring or scale work restarts.

## Cases
- `homejoy-growth-over-retention` (failure)
- `pebble-time-repositioning` (failure)

## Sources
- https://www.ycombinator.com/library/4D-yc-s-essential-startup-advice
- https://www.paulgraham.com/ds.html
- https://www.michaelseibel.com/blog/the-real-product-market-fit
