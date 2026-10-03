---
id: high-friction-onboarding
title: Onboarding steps that block value without helping the user
thinkers: [Jason Cohen, Amol Avasare, Andrew Chen]
applies_to: [all]
---

**Claim.** If onboarding asks for effort that does not help the user reach value, many new users leave in the first session, and early losses cost the most.

## Why it is a problem
Jason Cohen says most cancellations happen in the first days or months, and small onboarding gains there compound into large revenue gains. He advises that onboarding is the safe bet when a team does not know what to fix. Amol Avasare (Anthropic, before that Mercury) gives the key nuance. At Mercury, one quarter spent only on onboarding quality was his highest-impact quarter, from fixing confusing fields and back-and-forth steps. At Anthropic, MasterClass, and Calm, extra questions that tailor the product to the user raised conversion. His rule: cut friction that adds nothing, and keep steps that show the user why the product is for them. Andrew Chen's data shows users decide to stop using an app in the first 3 to 7 days.

## How to detect
- Signup flow: count screens and required fields from landing page to first value. Search routes and components for `signup`, `register`, `onboarding`, `welcome`, `step`.
- For each required field, check if the product uses it later (personalization, recommendations) or only stores it. Fields that are never read are bad friction.
- Check for gates before value: email verification, credit card, team invite, or long setup before the user sees any result. Flag each one that is not legally required.
- Check for an empty state. A new account with no sample data, template, or guided first task is a flag.
- Analytics: check for a step-by-step onboarding funnel (one event per step). Without it, drop-off points are unknown.
- Intake question: "How many minutes and steps does a new user need before they first get value?"

## Fixes
- Map every onboarding step. Delete or defer each step that the product does not use to help the user.
- Keep or add one or two questions that tailor the first screen to the user. A/B test them against the shorter flow.
- Add sample data or a template so the first session ends with a real result.

## Cases
- `slack-sell-the-outcome` (success)
- `stripe-collison-installation` (success)
- `superhuman-human-onboarding` (success)

## Sources
- https://www.lennysnewsletter.com/p/why-your-product-stopped-growing (Jason Cohen, Lenny's Podcast, 2026)
- https://www.lennysnewsletter.com/p/anthropics-1b-to-19b-growth-run (Amol Avasare, Lenny's Podcast, 2026)
- https://andrewchen.com/new-data-shows-why-losing-80-of-your-mobile-users-is-normal-and-that-the-best-apps-do-much-better/ (Andrew Chen)
- Ideas read in Lenny's official starter dataset: https://github.com/LennysNewsletter/lennys-newsletterpodcastdata
