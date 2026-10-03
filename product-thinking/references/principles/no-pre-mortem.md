---
id: no-pre-mortem
title: Launch planned with no list of ways it could fail
thinkers: [Shreyas Doshi]
applies_to: [all]
---

**Claim.** If a team never asks how a launch could fail before it ships, known risks stay unspoken and turn into post-launch fires.

## Why it is a problem
Shreyas Doshi ran pre-mortems at Stripe. The team meets one to three months before launch and lists the threats that could make it fail. His template sorts each threat into three labels. A tiger is a clear threat that will hurt if ignored. A paper tiger is a concern the speaker does not personally believe. An elephant is a problem the team avoids talking about. The labels make it safe to raise doubts. After the meeting the team picks the top 3 to 5 threats and gives each one a fix and an owner. Without this step, people keep silent concerns and the team learns them in a post-mortem.

## How to detect
- Spec or PRD: search for a risks, failure modes, or anti-goals section. Search for `risk`, `pre-mortem`, `what could go wrong`, `non-goals`, `rollback`.
- Check if each listed risk has an owner and a mitigation. A bare list of risks is a partial pass.
- Code and ops: check for a rollback path (feature flags, migration down scripts, kill switch). Search for `flag`, `rollout`, `down`, `kill`.
- Check for launch criteria: what metric or event would make the team pause or roll back.
- Intake question: "Imagine this launch failed six months from now. What are the three most likely reasons?"

## Fixes
- Run a one-hour pre-mortem before launch. Collect tigers, paper tigers, and elephants in silence first, then vote.
- Pick the top 3 to 5 tigers. Give each an owner and a mitigation.
- Add a rollback switch and one stop condition (for example, error rate above a set limit) to the launch plan.

## Cases
- `dinnr-survey-said-yes` (failure)

## Sources
- https://www.lennysnewsletter.com/p/episode-3-shreyas-doshi (Shreyas Doshi, Lenny's Podcast, 2022; page lists pre-mortems as a topic)
- https://docs.superhuman.com/@shreyas/pre-mortems-how-a-stripe-product-manager-predicts-prevents-probl (Shreyas Doshi's pre-mortem template; old Coda link redirects here)
