---
id: no-distribution-plan
title: No plan for how users will find the product
thinkers: [Evan Spiegel, Mark Pincus, Andrew Chen]
applies_to: [all]
---

**Claim.** A team that builds the product first and hopes users arrive later has no growth engine, and a good product alone does not get discovered.

## Why it is a problem
Evan Spiegel (Snap CEO) argues that consumer teams spend most of their effort on product-market fit and too little on distribution. In the same episode, he and Lenny agree that AI makes building cheaper but does not help a product get noticed, so distribution is now the main moat. Mark Pincus (Zynga founder) calls the build-it-and-they-will-come approach a hope strategy. He says distribution must be part of the product and proven from the start, and that the average user now installs zero new apps per month. Andrew Chen adds that a broad, unfocused launch spreads users too thin. A dense small network (Facebook at Harvard, Snapchat in high schools) retains better than a large scattered one.

## How to detect
- README, spec, or pitch: look for a section that names the first channel (SEO, app store, marketplace listing, integration, sales, community, referral). If no channel is named, flag it.
- Code: search for built-in distribution surfaces. Examples are share links, public pages indexed by search engines, invite flows, embeds, badges ("made with X"), and integration listings. Search for `share`, `invite`, `og:`, `sitemap`, `embed`, `referral`.
- Check for `robots.txt`, `sitemap.xml`, and Open Graph tags on public pages. Their absence on a content product is a flag.
- Analytics: check that signups record a source (`utm_*`, `referrer`, `source`). If the team cannot say where users come from, it has no distribution data.
- If unclear, ask the intake question: "Where will your first 100 users come from, and how will user 1,000 hear about you?"

## Fixes
- Pick one primary channel for the first 100 users. Write it in the spec with a number to hit and a date.
- Build one distribution surface into the product, such as a public shareable output or an invite that the core action creates.
- Launch into one dense community (one school, one company, one niche forum) before a broad launch.

## Cases
- `kozmos-chrome-store-dependency` (failure)
- `app-net-developer-chicken-and-egg` (failure)
- `everpix-product-without-distribution` (failure)
- `marginalia-launch-without-audience` (failure)

## Sources
- https://www.lennysnewsletter.com/p/snapchat-ceo-why-distribution-is (Evan Spiegel, Lenny's Podcast, 2026)
- https://www.lennysnewsletter.com/p/the-common-pattern-behind-successful (Mark Pincus, Lenny's Podcast, 2026)
- https://andrewchen.com/how-to-solve-the-cold-start-problem-for-social-products/ (Andrew Chen)
- Ideas read in Lenny's official starter dataset: https://github.com/LennysNewsletter/lennys-newsletterpodcastdata
