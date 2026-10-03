---
id: no-growth-loop
title: New users do not bring in more new users
thinkers: [Brian Balfour, Casey Winters, Kevin Kwok, Andrew Chen, Elena Verna, Jorge Mazal]
applies_to: [all]
---

**Claim.** If each new cohort of users does not produce the next one, growth depends on constant paid or manual input and stops when that input stops.

## Why it is a problem
Reforge's essay by Balfour, Winters, Kwok, and Chen says funnels run one way and need fresh input forever. A growth loop is a closed system where the output of one cohort becomes input for the next. Pinterest is their example: saved pins get indexed by search engines and bring new users. The fastest-growing products usually run one or two strong loops. Elena Verna says Lovable's word-of-mouth loop only works if the product amazes users, and that giving the product away beat paid ads. Jorge Mazal shows a copied loop can fail. Duolingo's Uber-style referral offered a free premium month, but its best users already paid, and new users rose only 3%.

## How to detect
- Trace the core action. Check if it creates something visible to non-users: a shared link, a public page, an invite, a collaborator seat, an exported file with attribution. Search for `share`, `invite`, `public`, `collaborator`, `powered by`.
- Check if shared outputs have a signup path back to the product (link, call to action, Open Graph preview).
- Referral code: if it exists, check that the reward is something active users can still use.
- Analytics: check for an attribution field on signup that records which user, share, or page brought the new user (`referrer_id`, `invited_by`, `utm_source`).
- Spec: check if it names how one cohort of users leads to the next. "Word of mouth" with no mechanism is a flag.
- Intake question: "When a user gets value, what in the product causes someone else to sign up?"

## Fixes
- Write the loop as a sentence: user does X, which creates Y, which new people see in Z, which brings them to sign up. Build the missing step.
- Add attribution to signups so the loop's output can be measured per cohort.
- Before copying another company's loop, check why it works there and whether the incentive fits your best users.

## Cases
- `everpix-product-without-distribution` (failure)
- `quibi-short-form-mobile-only` (failure)
- `sonar-engagement-over-growth` (failure)
- `plancast-social-event-sharing` (failure)

## Sources
- https://www.reforge.com/blog/growth-loops (Balfour, Winters, Kwok, Chen, Reforge)
- https://www.lennysnewsletter.com/p/the-new-ai-growth-playbook-for-2026-elena-verna (Elena Verna, Lenny's Podcast, 2025)
- https://www.lennysnewsletter.com/p/how-duolingo-reignited-user-growth (Jorge Mazal, guest post, 2023)
- Ideas read in Lenny's official starter dataset: https://github.com/LennysNewsletter/lennys-newsletterpodcastdata
