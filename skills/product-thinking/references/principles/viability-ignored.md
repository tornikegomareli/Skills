---
id: viability-ignored
title: The product does not work for the business
thinkers: [Marty Cagan, Amazon Working Backwards (Colin Bryar, Bill Carr)]
applies_to: [all]
---

**Claim.** A product that users love can still fail if it cannot be sold, priced, supported, or run at a profit.

## Why it is a problem
Cagan lists business viability as one of four big risks, owned by the product manager and tackled early. He says viability covers fit with the sales channel, partner contracts and legal compliance, affordable customer acquisition, monetization, and the brand promise. His point is that customer love is not enough on its own. Amazon's PR/FAQ forces the same check: the internal FAQ must answer per-unit economics, gross profit, upfront investment, and the path to profit. A spec with no cost or pricing section skips this test.

## How to detect
- Search the spec and `docs/` for pricing, unit cost, margin, or a business model. Flag the project if none exist.
- Check for billing code: payment provider SDK, plans, trial logic, failed-payment handling. A paid product with no billing path is a flag.
- For `ai-product`: estimate model cost per request (tokens, calls per user action) and compare it with plan price. Flag heavy calls on free tiers with no limits.
- Check for usage limits, rate limits, or quotas on expensive operations.
- Check for legal and compliance basics the market needs: privacy policy, terms, data deletion, and SSO or audit logs for b2b-saas.
- Ask intake questions 7 and 9 (who has paid and how much, the most concrete commitment).

## Fixes
- Write an internal FAQ: cost per active user, price, gross margin, and how customers will be acquired.
- Add metering for the most expensive operation. Set a limit per plan.
- Test willingness to pay with a real price before building more features.

## Cases
- `99dresses-fee-on-falling-value` (failure)
- `juicero-hardware-cost` (failure)
- `kite-ai-code-completion` (failure)
- `notion-rebuild-kyoto` (success)

## Sources
- https://www.svpg.com/four-big-risks/
- https://workingbackwards.com/resources/working-backwards-pr-faq/
