---
id: no-defensibility
title: Nothing stops a competitor from copying the product
thinkers: [Hamilton Helmer]
applies_to: [all]
---

**Claim.** If a product's advantage is only a feature set, a competitor can copy it, and margins fall to zero once the market sees it works.

## Why it is a problem
Helmer defines Power as two things at once: a benefit (higher prices or lower costs) and a barrier that stops rivals from copying it. A benefit alone is common and does not last. He names seven sources of Power: scale economies, network economies, counter-positioning, switching costs, branding, cornered resource, and process power. Only some are open to a young company. Counter-positioning and cornered resources fit the start, while network economies, scale, and switching costs come during takeoff. Vanguard is his counter-positioning example: low-fee index funds that active managers could not copy without hurting their own fee business.

## How to detect
- Read the README, pitch, or spec for a "why us" or "why now" section. If the only answer is features or "better UX", flag it.
- Check whether value grows with users: shared workspaces, invites, public profiles, marketplace listings. If each user gets the same value alone, network economies are absent.
- Check for switching costs the user would lose by leaving: stored history, integrations, custom config, team workflows. Note that export tools reduce lock-in, which is fine for trust but must be weighed.
- Check for a proprietary asset: unique data, exclusive licence, a model trained on data others lack. If the core is a thin wrapper over a public API (common in `ai-product`), flag it.
- Check whether incumbents could copy the model without harming their own business. If yes, there is no counter-positioning.
- If the docs are silent, ask the user which of the seven powers they expect to have in two years.

## Fixes
- Name the one power the product will build first. Write how the barrier forms and when.
- Design features that compound with use: shared data, team history, integrations. Track whether they get used.
- If the product is a thin wrapper, find a cornered resource (data, distribution, domain workflow) before scaling spend.

## Cases
- `homejoy-growth-over-retention` (failure)
- `vinetrade-buying-was-the-fun` (failure)

## Sources
- https://thetriumgroup.substack.com/p/strategic-power-a-conversation-with (interview with Helmer; benefit plus barrier)
- https://evansamek.substack.com/p/summary-7-powers (secondary summary; seven powers, stages, Vanguard)
