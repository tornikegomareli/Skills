---
id: untested-willingness-to-pay
title: Price set by guess, never tested with buyers
thinkers: [Jason Cohen, Jen Abel]
applies_to: [all]
---

**Claim.** If nobody has tested what customers will pay, the price is usually too low, and a low price attracts buyers who get little value and churn.

## Why it is a problem
Jason Cohen says early companies often guess a price and never change it, and the guess is usually too low. When they raise it, signups often stay flat or go up. His reason is that price selects the market. A large company sees a very cheap tool as not serious, and low-budget buyers were never getting much value anyway. He also says price includes structure (per seat, per usage) and positioning, and that framing the same product around what the buyer values can raise revenue many times. Jen Abel describes two enterprise buying modes: buy the cheapest option for a low-stakes task, or pay a large contract to remove a high risk. ChartMogul's 2025 data shows AI-native products under $50 per month at 23% gross revenue retention, against 70% for those over $250.

## How to detect
- Pricing page or config: find the plans (search for `price`, `plan`, `tier`, Stripe price IDs). Flag if there is one flat low price with no tier for larger buyers.
- Check the git history of pricing files. If the price has not changed since launch, flag it.
- Spec: check for a stated value metric (what the price scales with) and a reason for the number. "Competitors charge X" alone is weak.
- Check for evidence of a payment test before build: pre-orders, paid pilots, a waitlist with a price shown, or a fake-door checkout.
- AI products: compare cost per request (tokens, GPU time) against plan price. Flag plans where heavy users cost more than they pay.
- Intake question: "Has anyone paid, or agreed in writing to pay, this price? How did you choose the number?"

## Fixes
- Ask 5 to 10 target buyers to pay or sign a letter of intent at the planned price before more build.
- Add a higher tier aimed at a larger buyer. Measure if signups drop when the entry price goes up.
- Write the price around the outcome the buyer cares about (more revenue, less risk), not around the feature.

## Cases
- `dinnr-survey-said-yes` (failure)
- `juicero-hardware-cost` (failure)
- `kite-ai-code-completion` (failure)
- `marginalia-launch-without-audience` (failure)
- `tract-ai-planning-editor` (failure)

## Sources
- https://www.lennysnewsletter.com/p/why-your-product-stopped-growing (Jason Cohen, Lenny's Podcast, 2026)
- https://www.lennysnewsletter.com/p/how-to-close-100k-1m-deals-step-by (Jen Abel, Lenny's Podcast, 2026)
- https://www.chartmogul.com/reports/saas-retention-the-ai-churn-wave/ (ChartMogul, 2025-12-10)
- Ideas read in Lenny's official starter dataset: https://github.com/LennysNewsletter/lennys-newsletterpodcastdata
