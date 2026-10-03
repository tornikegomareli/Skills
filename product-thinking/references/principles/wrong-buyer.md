---
id: wrong-buyer
title: Product sold to people who cannot or will not buy it
thinkers: [Jeanne DeWitt Grosser, Jen Abel, Jason Cohen]
applies_to: [b2b-saas, dev-tool, ai-product]
---

**Claim.** If the team designs and sells for the user but never reaches the person who owns the budget, deals stall and get blamed on price.

## Why it is a problem
Jeanne DeWitt Grosser (COO, Vercel) describes a quarter where sales reps blamed lost deals on price. An analysis of the calls and emails showed the real cause: the team never reached the economic buyer and never proved the value. She also notes that buying differs by segment. A small company often has one decision maker, while a large company buys by committee. She says most customers buy to avoid pain, not to gain upside. Jen Abel advises selling to an executive who owns the budget and to the level just below, with a champion who carries the deal inside. Jason Cohen adds that the price itself picks which buyer shows up.

## How to detect
- Spec or README: check if it names both the user (who uses it daily) and the buyer (who approves the spend). If only the user is named, flag it.
- Check if the stated value is something the buyer cares about (cost, risk, revenue, compliance), not only user convenience.
- B2B code: check for buyer-facing features. Examples are admin console, seat management, SSO, audit log, usage reports, and invoice billing. Search for `admin`, `sso`, `saml`, `audit`, `invoice`, `seats`.
- Check if the signup flow captures company and role. If every account is personal, a team buyer has nothing to approve.
- CRM or sales notes: count lost deals marked "price". If most are, check if the buyer was ever in the deal.
- Intake question: "Who signs the contract or enters the card, and what do they need to see to say yes?"

## Fixes
- Name the buyer in the spec. Write one sentence of value in the buyer's terms, tied to a pain they want to avoid.
- Add the minimum buyer features for the target segment, such as a usage report the champion can forward.
- Pick one segment (single decision maker or committee) and match the sales motion to it.

## Cases
- `exambuff-built-before-asking` (failure)
- `kite-ai-code-completion` (failure)
- `ondsel-hobbyists-not-buyers` (failure)

## Sources
- https://www.lennysnewsletter.com/p/what-the-best-gtm-teams-do-differently (Jeanne DeWitt Grosser, Lenny's Podcast, 2025)
- https://www.lennysnewsletter.com/p/how-to-close-100k-1m-deals-step-by (Jen Abel, Lenny's Podcast, 2026)
- https://www.lennysnewsletter.com/p/why-your-product-stopped-growing (Jason Cohen, Lenny's Podcast, 2026)
- Ideas read in Lenny's official starter dataset: https://github.com/LennysNewsletter/lennys-newsletterpodcastdata
