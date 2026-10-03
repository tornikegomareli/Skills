# Real product cases: sources for the product-thinking knowledge base

Checked on 2026-10-03 with web fetch, curl, and web search.
Rule for every source: summarize in our own words, link the original, copy no text.

## 1. Sources

| Source | URL | Access | Terms | Bulk collection method | Cases (approx) | Value | Verified |
|---|---|---|---|---|---|---|---|
| Hacker News via Algolia search API | https://hn.algolia.com/api/v1/search | Free, no key | HN posts belong to their authors. We store only links and our own summaries. | JSON API. Filter with `tags=story` and `numericFilters=points>100`. | 69 stories for "post-mortem" with >100 points; 203 for "shutting down" with >100 points | High (founder-written, primary) | Yes. API returned results. Rate limit not checked. |
| Killed by Google | https://killedbygoogle.com | Free | Repo is MIT license | `graveyard.json` in https://github.com/codyogden/killedbygoogle (name, dateOpen, dateClose, description, link, type) | 308 products | Medium (dates and links only, no "why") | Yes. JSON downloaded, 308 records. |
| Failory Cemetery | https://www.failory.com/cemetery | Free | No terms page found (`/terms` returns 404). robots.txt allows `/cemetery/`. Content is copyrighted by default. | `sitemap.xml` lists cemetery pages. Fetch each page, then write our own summary. | 120+ (135 cemetery URLs in sitemap) | High (each case lists failure causes) | Yes. Page and sitemap load. |
| CB Insights post-mortem list | https://www.cbinsights.com/research/startup-failure-post-mortem/ | Free to read. Full "book of post-mortems" needs a form. | Commercial publisher. Do not copy. | Manual only. Use it to find links to the original news or founder posts. | 483 | Medium (good index, secondary) | Yes |
| CB Insights failure reasons report | https://www.cbinsights.com/research/report/startup-failure-reasons-top/ | Summary free. Full report gated. | Commercial. Cite numbers, do not copy. | None. One report. | 431 shutdowns analyzed (385 with known reason) | Medium (good for base rates: 70% ran out of capital, 43% poor product-market fit) | Yes |
| Kaggle "Startup Failures" dataset | https://www.kaggle.com/datasets/dagloxkankwanda/startup-failures | Free, Kaggle account to download | CC BY-NC 4.0 | Kaggle API (`kaggle datasets download`) | 814 companies; 409 with 13 failure-cause flags | Medium (structured, but secondary and short text) | Yes. Metadata read from Kaggle API. Columns not checked. |
| First Round Review | https://review.firstround.com | Free | Copyrighted articles | No RSS found (`/feed.xml` is 404). Manual. | Dozens of deep company stories | High (successes with numbers, for example Superhuman) | Yes (Superhuman article loads) |
| Company and founder writing (Slack memo, Kite farewell, Linear Method) | e.g. https://linear.app/method | Free | Copyrighted | Manual. Some originals are gone (kite.com is parked; read via Wayback Machine). | Small, hand-picked | High (primary source of the decision) | Yes for the URLs in section 2 and Linear Method |
| Wikipedia | https://en.wikipedia.org | Free | CC BY-SA 4.0. We link and summarize. | MediaWiki API | Thousands of company pages | Medium (good for dates and numbers to check other sources) | Yes |
| Startups.RIP | https://startups.rip | Reports free. Specs, chat, CLI need Pro. | Says reports include AI-generated analysis | Sitemap. CLI is paid. | ~1,700 YC companies (claim from a third-party article, not counted) | Low to medium (AI text; use only its cited primary sources) | Partly. Site loads. Count not verified. |
| Indie Hackers | https://www.indiehackers.com | Free, some "IH+" paid posts | Terms page returns 403 to our fetcher. Not read. | Manual | Hundreds of founder stories with revenue | Medium (small products, self-reported numbers) | Partly. Home page loads. Terms not verified. |
| Lenny's Newsletter | https://www.lennysnewsletter.com | Free tier plus paid. Many deep posts are paid. | Copyrighted, paid content | RSS at `/feed` (20 latest items) | Many growth stories | Medium (paywall limits use) | Partly. RSS works. Exact paywall split not checked. |
| Product Hunt API v2 | https://api.producthunt.com/v2/docs | Free token | API "must not be used for commercial purposes" without permission | GraphQL API | Launches, not outcomes | Low (no failure or success outcome) | Yes |
| YC company directory | https://www.ycombinator.com/companies | Free | Not checked | Page is JS-rendered. An "Inactive" filter exists in the URL, but our fetcher saw no list. | Unknown | Low to medium (status only, no "why") | No. List content not seen. |
| autopsy.io | https://autopsy.io | None | n/a | n/a | 0 | None. Domain is parked and for sale. | Yes (dead) |
| SaaS Heaven, Deadstack | dev.to article; Product Hunt listings | Not checked | Not checked | Not checked | Unknown | Unknown | No. Found only in search results. |

## 2. Sample cases

---
id: quibi-short-form-mobile-only
product: Quibi
type: failure
category: consumer app
decision: Spent about $1.75B on premium short shows before testing demand. Launched phone-only. At launch, users could not take screenshots to share clips or cast to a TV.
outcome: Launched on 6 April 2020. Fell out of the top 50 free iPhone apps within a week. Had about 500,000 subscribers at the October 2020 shutdown notice, against a first-year target of 7.4M. Shut down on 1 December 2020.
lesson: A large budget does not replace a small test of real demand, and removing sharing removed the main way new users find the product (no-validated-problem).
principles: [no-validated-problem, missing-growth-loop, ignored-user-context]
sources: https://en.wikipedia.org/wiki/Quibi, https://www.failory.com/cemetery/quibi
---

---
id: kite-ai-code-completion
product: Kite
type: failure
category: dev tool
decision: Built in this order: team, product, distribution, then monetization. Sold to individual developers first.
outcome: Reached 500,000 monthly active developers with almost no marketing. Those users would not pay. Managers did not pay for "18% faster coding". Reached product-market fit only in 2019, five years in. Stopped work in 2021 and announced the shutdown on 16 November 2022.
lesson: Users who love a free tool are not proof that someone will pay, so test who pays early (no-validated-willingness-to-pay).
principles: [no-validated-willingness-to-pay, wrong-buyer, late-monetization]
sources: https://web.archive.org/web/20250330044400/https://www.kite.com/blog/product/kite-is-saying-farewell/, https://devclass.com/2022/11/21/kite-ai-coding-pulled-down-to-earth-because-our-500k-developers-would-not-pay-to-use-it-now-open-source/
---

---
id: superhuman-pmf-engine
product: Superhuman
type: success
category: B2B SaaS
decision: Asked users how they would feel if they could no longer use the product. Used the share of "very disappointed" answers as the main metric, with 40% as the target. Focused on the users who loved it most. Split the roadmap half on what those users loved and half on what blocked the near-fans.
outcome: The score rose from 22% (summer 2017) to 33% after segmenting, then to 58% after three quarters of work.
lesson: Measure product-market fit with one repeatable metric and build for the segment that already loves the product (measurable-pmf).
principles: [measurable-pmf, focus-on-best-segment, feedback-driven-roadmap]
sources: https://review.firstround.com/how-superhuman-built-an-engine-to-find-product-market-fit/
---

---
id: slack-sell-the-outcome
product: Slack
type: success
category: B2B SaaS
decision: Before the 2013 preview launch, the CEO told the team to sell the outcome for a team (less communication cost, searchable team knowledge) and not "a group chat app". He also asked for high polish, because new users meet the product with no context.
outcome: The tool came from the failed game Glitch. After the August 2013 public preview, 8,000 customers signed up in 24 hours. It passed 1M daily active users in late 2015 and 10M by April 2019. Salesforce bought it for about $27.7B in 2021.
lesson: Position the product by the change it makes for the customer and not by its feature category (weak-positioning).
principles: [weak-positioning, sell-the-outcome, first-run-experience]
sources: https://medium.com/@stewart/we-dont-sell-saddles-here-4c59524d650d, https://en.wikipedia.org/wiki/Slack_(software)
---

Note: the Medium URL is confirmed by its Hacker News submission (item 8317497). Medium blocked our fetcher. The memo text was read from a copy at alexanderjarvis.com.

## 3. Collection plan: mine these 3 first

1. **Hacker News (Algolia API).** Query stories with terms like "post-mortem", "shutting down", "lessons from failing", "we're closing" and `points>100`. Keep only posts written by the founder. Store the link, write a summary in our own words, and tag principles. This gives primary, product-specific failures, many of them dev tools and SaaS.
2. **Failory Cemetery.** Read the cemetery URLs from `sitemap.xml` (135 pages). Use each page's failure-cause tags to map to principle ids. Then follow each page to an original source (founder post, Wikipedia, news) and cite that source next to Failory. Crawl slowly; robots.txt allows it.
3. **First Round Review plus company writing, for successes.** Failure sources outnumber success sources, so pick successes by hand. Target 20 to 30 articles where a company explains one product decision with numbers (Superhuman, Slack, Linear Method, and similar). Write one case per decision, not per company.

Use Killed by Google `graveyard.json` and the Kaggle dataset as checklists and for dates, not as case text. Skip autopsy.io (dead) and the Product Hunt API (non-commercial terms, no outcomes).
