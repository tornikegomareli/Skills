# UX, intake questions, live evidence, checklists

Research for the `product-thinking` skill. Checked on 2026-10-03.

"Verified: yes" means I loaded the URL and confirmed the access and terms claims on the page itself, or called the endpoint and got data back.
"Partial" means the URL works but a claim (terms, limit) comes from a secondary source or was not stated on the page.
"No" means I could not load or confirm it.

Rule for the public repo: rewrite everything in our own words, cite the URL, and copy no text. Several sources below forbid derivatives (Laws of UX is CC BY-NC-ND). Short factual names (heuristic names, law names) are fine to list with a citation.

## 1. Sources

| Source | URL | Layer | Access | Terms | Value | Verified |
|---|---|---|---|---|---|---|
| NN/g, 10 Usability Heuristics (Jakob Nielsen) | https://www.nngroup.com/articles/ten-usability-heuristics/ | ux | Free article | Page says you may use the heuristics in your work if you credit Jakob Nielsen and link the page. Reprints of article text fall under https://www.nngroup.com/copyright-and-reprint-info/ | high | yes |
| NN/g, How to conduct a heuristic evaluation | https://www.nngroup.com/articles/how-to-conduct-a-heuristic-evaluation/ | ux | Free article | NN/g copyright. Paraphrase and cite | med | yes (URL 200, terms same as above) |
| NN/g article index | https://www.nngroup.com/articles/ | ux | Free articles. Reports and courses are paid | NN/g copyright | high | yes (URL 200) |
| Laws of UX (Jon Yablonski) | https://lawsofux.com/ and https://lawsofux.com/llms.txt | ux | Free. 30 named laws. Also a paid book | Site content is CC BY-NC-ND 4.0 (stated on https://lawsofux.com/info/). No derivatives, so cite law names and link; write our own explanation | high | yes |
| Baymard Institute research | https://baymard.com/research, https://baymard.com/blog | ux, checklist | Free: 450+ articles, benchmarks, page examples, a limited set of guidelines. Paid: full 700+ guidelines, plans from $200/month (Foundation, annual) per https://baymard.com/pricing | Copyrighted. Paraphrase findings, cite article URL | high (checkout, forms, e-commerce) | yes |
| Baymard cart abandonment stats | https://baymard.com/lists/cart-abandonment-rate | checklist | Free | Copyrighted. Cite numbers with URL | med | yes (URL 200) |
| Apple Human Interface Guidelines | https://developer.apple.com/design/human-interface-guidelines/ | ux, checklist | Free | Apple copyright. No reuse license found on the page. Paraphrase and cite | high (iOS, macOS apps) | partial (URL 200, terms not found) |
| Material Design 3 | https://m3.material.io/ | ux, checklist | Free | License for site text not confirmed. Treat as copyrighted, paraphrase and cite | med (Android, web) | partial (URL 200, terms not checked) |
| W3C WCAG 2.2 | https://www.w3.org/TR/WCAG22/ and https://www.w3.org/WAI/WCAG22/quickref/ | ux, checklist | Free | W3C document license allows reuse with attribution (from memory, not re-checked) | high (accessibility checks an agent can run) | partial |
| The Mom Test (Rob Fitzpatrick) | https://www.momtestbook.com/ | questions | Paid book (paperback, Kindle, PDF, audio). No free edition. Paid Udemy course | Copyrighted. Use the idea (ask about past behavior, not opinions), cite the book, quote nothing | high | yes |
| Jobs-to-be-Done switch interview (Bob Moesta) | https://jobstobedone.org/ | questions | Site returned 403 to my requests | Unknown | high (method), source unverified | no |
| Intercom on Jobs-to-be-Done | https://www.intercom.com/blog/jobs-to-be-done/ and https://www.intercom.com/resources/books/intercom-jobs-to-be-done | questions | Free blog; book page loads | Intercom copyright | med | partial (URL 200, content not read) |
| Andrew Chen essays | https://andrewchen.com/new-data-shows-why-losing-80-of-your-mobile-users-is-normal-and-that-the-best-apps-do-much-better/, https://andrewchen.com/how-to-solve-the-cold-start-problem-for-social-products/, https://andrewchen.com/this-is-the-product-death-cycle-why-it-happens-and-how-to-break-out-of-it/ | checklist | Free blog | Copyrighted. Paraphrase and cite | med (consumer retention, marketplaces, cold start) | partial (found by search, not fetched) |
| Lenny's Newsletter, activation benchmarks (Rachitsky and Timen, 2022-10-25) | https://www.lennysnewsletter.com/p/what-is-a-good-activation-rate | checklist | Free post | Copyrighted. Cite numbers only | high | yes |
| Lenny's Newsletter, retention benchmarks (2020-06-09) | https://www.lennysnewsletter.com/p/what-is-good-retention-issue-29 | checklist | Free post | Copyrighted. Cite numbers only | high | yes |
| ChartMogul, SaaS retention report (2025-12-10) | https://www.chartmogul.com/reports/saas-retention-the-ai-churn-wave/ | checklist | Free, no email gate seen | Copyrighted. Cite numbers only | high (AI and B2B SaaS retention) | yes |
| Apple customer reviews RSS | see section 4 | live-evidence | Free, no key | No published terms or docs from Apple. Undocumented endpoint | high | yes (endpoint works) |
| iTunes Search / Lookup API | see section 4 | live-evidence | Free, no key | Apple's Search API terms (not re-read) | med | yes (endpoint works) |
| Google Play Reply to Reviews API | https://developers.google.com/android-publisher/reply-to-reviews | live-evidence | Free, OAuth, own apps only | Only reviews with text, last 7 days, production builds. 200 GET/hour | low (only for the user's own app) | yes |
| Hacker News Algolia API | see section 4 | live-evidence | Free, no key | No ToS page found. Limit from secondary sources | high (dev tools, B2B SaaS) | partial (endpoint works, limit secondary) |
| Hacker News Firebase API | https://hacker-news.firebaseio.com/v0/ | live-evidence | Free, no key | MIT-licensed docs at github.com/HackerNews/API (from memory) | low (no search) | yes (endpoint works) |
| Reddit Data API | https://redditinc.com/policies/data-api-terms | live-evidence | Free tier needs OAuth app registration. Unauthenticated JSON returned 403 in my test | Terms (revised 2026-07-20): no commercial use without a separate agreement; no AI/ML training on user content without rightsholder permission. 100 QPM with OAuth (secondary source) | med (high signal, high setup cost) | partial |
| GitHub Search API (issues) | https://docs.github.com/en/rest/search/search | live-evidence | Free. Token optional | GitHub API terms | high (dev tools, open-source products) | yes |
| Stack Exchange API | https://api.stackexchange.com/docs/throttle | live-evidence | Free. Key optional | 10,000 requests/day default quota per key. Content is CC BY-SA (from memory) | med (dev tools) | yes (endpoint works, quota page read) |
| Product Hunt API v2 | https://api.producthunt.com/v2/docs | live-evidence | Free developer token, needs an account | Docs: must not be used for commercial purposes without contacting them. Fair-use rate limit | low | yes |
| G2 API | https://data.g2.com/api/docs | live-evidence | Token from G2 Partner Dashboard. Roles depend on paid subscription | Vendor or partner access. No public read of competitor reviews found | low (not usable at call time) | partial |
| G2 website | https://www.g2.com/ | live-evidence | Returned 403 to scripted requests | Do not scrape | low | yes (403) |

## 2. Draft `questions.md`

The skill asks these only when the codebase or spec does not answer them. It asks at most 3 to 5 at a time, in priority order. Each question asks about something that already happened. Opinions about the future ("would you use", "would you pay") are weak evidence, so the skill does not ask for them.

Idea source: Rob Fitzpatrick, *The Mom Test* (https://www.momtestbook.com/). Timeline idea in questions 4 to 6 comes from Bob Moesta's switch interview (unverified source, see table). Wording below is our own.

```markdown
# Intake questions

Ask only what the code and docs do not answer. Ask about facts that already happened.
If the user does not know, record "unknown" and lower the confidence of related findings.

## User and problem
1. Who was the last real person who had this problem? What was their role, and what were they trying to get done that day?
2. When did that person last hit the problem? What did it cost them in time, money, or risk?
3. How many people have you seen with this problem in the last month? How did you find them?

## Current alternatives
4. What does that person use today to handle it? A tool, a spreadsheet, a person, or nothing?
5. What made them start looking for something better? Describe the moment, if you know it.
6. Has anyone tried your product and then gone back to their old way? What did they say or do?

## Value and pricing
7. Has anyone paid for this, or for the tool it replaces? How much, and who approved the spend?
8. What did the last customer give up to use this: money, setup time, data migration, or a habit?
9. If nobody has paid yet, what is the most concrete commitment you got (pilot, letter, deposit, intro to a buyer)?

## Distribution
10. Where did your first 10 users come from? Name the channel for each, if you can.
11. When a user recommended the product, what did they say, and to whom?
12. How do people in this market usually find and buy tools like this today?

## Success metrics
13. What action shows that a new user got value for the first time? How many new users reached it last week?
14. Of users who signed up 30 days ago, how many came back in the last 7 days?
15. What number did you look at last time you made a product decision? What did you decide?
```

## 3. Checklists by product type

Each item is checkable in a codebase or spec. The check describes what the agent looks for.

### Consumer app
1. First-run flow reaches the core action without a forced sign-up wall. Check: onboarding screens, auth gating on first route.
2. Every async action shows loading, success, and error states. Check: network calls in views; look for missing error UI (NN/g heuristics 1 and 9).
3. Permissions (notifications, location, camera) are asked in context, not at launch. Check: where permission prompts fire (Apple HIG onboarding and privacy pages).
4. There is a trigger that brings users back (notification, email, widget) tied to a real event. Check: push or email code and what fires it. Andrew Chen's essays put most churn in the first 3 to 7 days.
5. Accessibility basics hold: labels on icon buttons, dynamic type or scalable text, contrast. Check: accessibility labels, hard-coded font sizes (WCAG 2.2).

### B2B SaaS
1. An activation event is defined and tracked. Check: analytics calls for a named "first value" event. Benchmark: average activation is 34%, median 25% (Lenny's Newsletter, 2022).
2. A new account can invite teammates and assign roles. Check: invite flow, role model, permission checks on the server.
3. There is a way in for buyers' IT: SSO/SAML, audit log, data export. Check: auth providers, audit tables, export endpoints.
4. Billing handles plan limits, trial end, failed payment, and downgrade. Check: billing webhooks and states for `past_due` and cancel.
5. Empty states teach the next step. Check: list views with zero items; is there a call to action or sample data?

### Dev tool
1. Time to first success is short: install and a working example in a few commands. Check: README quick start; count steps; run it if possible.
2. Error messages say what failed and how to fix it. Check: thrown errors and CLI output strings (NN/g heuristic 9).
3. Docs match the code. Check: documented flags, endpoints, and config keys against the actual parser or routes.
4. Versioning and breaking changes are visible: semver, changelog, deprecation warnings. Check: `CHANGELOG`, release tags, deprecation code paths.
5. Users can report issues and see them handled. Check: issue templates, response activity via GitHub Search API (section 4).

### Marketplace
1. Both sides have a reason to join before the other side is large (cold start). Check: supply-side tools or single-user value in the spec (Andrew Chen, cold start essay).
2. Search and filters return useful results with little inventory. Check: empty search result handling, fallback suggestions.
3. Trust signals exist: reviews, verification, dispute or refund flow. Check: review model, identity checks, dispute states.
4. The transaction happens on-platform, so it is hard to bypass. Check: messaging rules, payment flow, contact-info filtering.
5. Activation is measured as the first completed transaction, not sign-up. Check: analytics events. Lenny's data shows B2C marketplaces have the lowest activation rates.

### AI product
1. The product sets expectations about what the AI can and cannot do. Check: onboarding copy, empty prompt state, example prompts.
2. Users can correct, retry, or undo AI output. Check: edit, regenerate, and undo actions (NN/g heuristic 3, user control).
3. Failure and latency are handled: streaming or progress, timeouts, model errors. Check: API error handling and loading UI (Laws of UX, Doherty Threshold).
4. Output quality is measured: evals, feedback buttons, logged ratings. Check: eval scripts, thumbs up/down events.
5. Unit cost fits the price. Check: tokens per request against plan price. ChartMogul (2025-12) reports AI-native products under $50/month at 23% GRR and 32% NRR.

## 4. Live evidence endpoints

All tested on 2026-10-03 with `curl` unless marked otherwise. The skill uses these to show real user complaints about the product or its competitors. It must cite each item by URL and must not store bulk content in the public repo.

### Apple App Store reviews (RSS, JSON)
- Endpoint: `https://itunes.apple.com/{country}/rss/customerreviews/page={1-10}/id={appId}/sortby=mostrecent/json`
- No key. Returns rating, title, text, app version, date.
- Limit: pages 1 to 10 only. Page 11 returned HTTP 400 in my test. That is about 500 recent reviews per country (secondary sources agree).
- Terms: Apple publishes no docs or terms for this feed. It can disappear without notice. Mark as unofficial.
- Find the `appId` with the Search API below.

### iTunes Search and Lookup API
- Search: `https://itunes.apple.com/search?term={name}&entity=software&limit=5`
- Lookup: `https://itunes.apple.com/lookup?id={appId}`
- No key. Returns app metadata, average rating, rating count, release notes.
- Limit: not re-checked. Apple's docs state about 20 calls per minute (from memory, unverified).

### Hacker News (Algolia)
- Search by relevance: `https://hn.algolia.com/api/v1/search?query={q}&tags=comment&hitsPerPage=50`
- Search by date: `https://hn.algolia.com/api/v1/search_by_date?query={q}&tags=story`
- Item tree: `https://hn.algolia.com/api/v1/items/{id}`
- No key. All three tested and returned data.
- Limit: 10,000 requests per hour per IP. Source: third-party client code, not an official page. The docs page at https://hn.algolia.com/api renders by JavaScript and I could not read the limit there.

### GitHub issue search
- Endpoint: `https://api.github.com/search/issues?q={terms}+repo:{owner}/{repo}+is:issue`
- Limit: 10 requests per minute without a token (confirmed by `x-ratelimit-limit: 10` header). 30 per minute with a token. A query returns at most 1,000 results. Both from https://docs.github.com/en/rest/search/search.
- Use: complaints and feature requests for open-source products or competitors.

### Stack Exchange
- Endpoint: `https://api.stackexchange.com/2.3/search/advanced?q={q}&site=stackoverflow&pagesize=20`
- Tested, returned data without a key.
- Limit: default quota 10,000 requests per day per app key (https://api.stackexchange.com/docs/throttle). Without a key, the quota is shared per IP. The exact no-key number is not verified.

### Reddit (only if the user sets up OAuth)
- Unauthenticated `search.json` returned HTTP 403 in my test. The skill cannot use Reddit without credentials.
- Free tier: 100 queries per minute per OAuth client id (secondary source). Without OAuth, 10 per minute (secondary source).
- Terms (https://redditinc.com/policies/data-api-terms, revised 2026-07-20): commercial use needs a separate agreement. No ML or AI training on user content without rightsholder permission. Display only, no modification.
- Recommendation: optional, off by default. Ask the user for their own token.

### Google Play reviews
- No public API for other developers' apps exists that I could find.
- The Reply to Reviews API works only for the user's own app, with OAuth. It returns reviews with text, from the last 7 days, production builds only. Quota: 200 GET per hour.
- Recommendation: use only when the user owns the app and provides credentials.

### Not usable at call time
- G2: website blocks scripts (403). API needs a paid partner token.
- Product Hunt: needs an account token. Commercial use is not allowed without contacting them.
