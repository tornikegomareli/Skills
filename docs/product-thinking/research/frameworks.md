# Layer: Core product frameworks and product sense

Checked on 2026-10-03 with web search, WebFetch, and `curl`.
"Verified: yes" means the page loaded and the content matched the claim.
No source below has an open license. All are "All rights reserved" or have no stated license.
Rule for the public repo: rewrite ideas in our own words, cite the URL, quote nothing longer than a short phrase.

## 1. Sources

| Source | URL | Access | License or terms | What to extract | Value | Verified |
|---|---|---|---|---|---|---|
| SVPG, Cagan, "The Four Big Risks" | https://www.svpg.com/four-big-risks/ | Free | "© 2026 SVPG. All Rights Reserved." | Value, usability, feasibility, viability risk. Tackle value and viability risk before building. | High | Yes |
| SVPG, "Product Discovery" | https://www.svpg.com/product-discovery/ | Free | Same as above | Discovery is iterative; requirements are not a fixed phase. | Med | Yes |
| SVPG, "The Most Important Thing" | https://www.svpg.com/the-most-important-thing/ | Free | Same as above | Give teams problems, not specs. Spec-only tickets are a signal. | Med | Yes |
| Product Talk, Torres, opportunity solution trees | https://www.producttalk.org/opportunity-solution-trees/ | Free | "Product Talk © 2026". No open license. | Outcome, then opportunities, then solutions, then assumption tests. | High | Yes |
| Product Talk, "Product Discovery Basics" | https://www.producttalk.org/2021/08/product-discovery/ | Free | Same as above | Continuous weekly customer contact. Test assumptions, not whole ideas. | High | Yes |
| Christensen Institute, Jobs to Be Done | https://www.christenseninstitute.org/theory/jobs-to-be-done/ | Free | All rights reserved. ToS says no reproduction without written permission; references must say it is the Institute's copyrighted material. | Customers "hire" a product for progress in a circumstance. Functional, social, emotional dimensions. | High | Yes |
| HBR, Christensen et al., "Know Your Customers' Jobs to Be Done" (2016) | https://hbr.org/2016/09/know-your-customers-jobs-to-be-done | Metered paywall | HBR copyright | Canonical JTBD citation. Cite only; do not depend on its text. | Med | Yes (page loads; body paywalled) |
| jtbd.info (Medium publication, Moesta / Klement circle) | https://jtbd.info/ | Unknown | Unknown | Switch interviews, forces of progress | Med | No. Timed out from `curl`; `medium.com/jtbd-info` returned 403. |
| April Dunford, "A Quickstart Guide to Positioning" | https://www.aprildunford.com/post/a-quickstart-guide-to-positioning | Free (book *Obviously Awesome* is paid) | No license stated; assume all rights reserved | Five components: competitive alternatives, unique attributes, value, target customers, market category. Start from alternatives. | High | Yes |
| Working Backwards (Bryar and Carr), PR/FAQ | https://workingbackwards.com/resources/working-backwards-pr-faq/ | Free article and template; $299 course | No license stated | Press release + external FAQ + internal FAQ. Start from the customer experience. | High | Yes |
| About Amazon, "An insider look at Amazon's culture and processes" | https://www.aboutamazon.com/news/workplace/an-insider-look-at-amazons-culture-and-processes | Free | Amazon copyright | First-party description of Working Backwards; says the process rejects most proposals. | High (primary source) | Yes |
| Shreyas Doshi, Substack | https://shreyasdoshi.substack.com/ | Free and paid posts mixed | Substack default; no license | Product sense, pre-mortems, LNO, anti-goals | Med | Partial. Home page returns 200; no single canonical essay on pre-mortems or LNO was confirmed. |
| Lenny's Podcast ep. 3, Shreyas Doshi | https://www.lennysnewsletter.com/p/episode-3-shreyas-doshi | Episode page free; transcript access not confirmed | Lenny's copyright | Pre-mortems, LNO, three levels of product work (impact, execution, optics) | Med | Yes (page and topic list) |
| Shreyas Doshi, "Improving Your Product Sense" course | https://maven.com/shreyas-doshi/product-sense | Paid | Commercial | Do not use. | Low | Search only |
| Lenny's official data repo | https://github.com/LennysNewsletter/lennys-newsletterpodcastdata | Partial: public starter of 10 posts + 50 transcripts; full archive for paid subscribers | LICENSE.md: "Copyright (c) 2019–2026 Lenny Rachitsky. All rights reserved." Starter: personal, non-commercial use; you may publish projects built with it; you may not redistribute raw files or use raw contents commercially. Paid: no redistribution of raw files or substantial portions. | Use for our own reading and research only. Never commit transcript text. Cite episode URLs. | Med | Yes (README and LICENSE.md read) |
| ChatPRD/lennys-podcast-transcripts (third party) | https://github.com/ChatPRD/lennys-podcast-transcripts | Free | No grant from Lenny. Repo says "personal and educational use" and "All content belongs to Lenny's Podcast and the respective guests." | Avoid. Use the official repo above instead. | Low | Yes |
| Paul Graham, "How to Get Startup Ideas" | https://www.paulgraham.com/startupideas.html | Free | No license stated; assume all rights reserved | Look for problems, ideally your own. Narrow-deep demand beats broad-shallow demand. | High | Yes |
| Paul Graham, "Do Things That Don't Scale" | https://www.paulgraham.com/ds.html | Free | Same | Manual recruiting and onboarding before automation. | Med | Yes |
| Paul Graham, "Be Good" | https://www.paulgraham.com/good.html | Free | Same | Make something people want; user benefit as a decision compass. | Med | Yes |
| YC Library, "YC's essential startup advice" | https://www.ycombinator.com/library/4D-yc-s-essential-startup-advice | Free | YC site terms (not read) | Launch now, build something people want, 90/10 solution, one problem at a time, talk to users. | High | Yes (headings extracted with `curl`) |
| Intercom on Product Management (book) | https://www.intercom.com/blog/product-management-book/ | Free (PDF, epub, mobi) | Intercom copyright; page asks readers to share it | Scope decisions, saying no to features, feature audits | Med | Partial. Page loads and says "free"; book file not downloaded. |
| Kano model, Folding Burritos guide | https://foldingburritos.com/blog/kano-model/ | Free | Blog copyright | Must-be, performance, attractive, indifferent. Cites Kano et al. 1984, "Attractive Quality and Must-be Quality". | Med | Yes (secondary source; 1984 paper not checked) |
| Gibson Biddle, DHM model (Medium) | https://gibsonbiddle.medium.com/2-the-dhm-model-6ea5dfd80792 | Free per search snippet; possibly metered by Medium | Author copyright | Delight customers in hard-to-copy, margin-enhancing ways. Netflix cases: personalization, device ecosystem, originals. | High | Partial. Found by search; direct fetch returned 403 (Medium blocks bots). |
| Gibson Biddle, strategy series summary | https://gibsonbiddle.medium.com/12-step-by-step-exercises-to-define-your-product-strategy-b27a81edc918 | Same | Same | Index of all his frameworks | Med | Partial (search only) |
| First Round Review, Superhuman PMF engine (Rahul Vohra) | https://review.firstround.com/how-superhuman-built-an-engine-to-find-product-market-fit/ | Free | First Round copyright | Sean Ellis question: "very disappointed" share; 40% as a leading indicator of PMF. | High | Yes (added source) |
| Reforge | https://www.reforge.com/blog | Blog free; courses, guides, artifacts paid (free trial) | Commercial | Use free blog posts only, case by case. | Low | Partial (blog returns 200; content not reviewed) |

Sources I did not add: Bob Moesta's own site (no verified URL), Christensen's milkshake case (not on any verified page; the HBR text is paywalled).

## 2. Sample principle entries

---
id: untested-value-risk
title: Building before testing whether anyone wants it
claim: A project that commits to build effort before it has tested value risk is betting the whole build on an unchecked assumption.
why_it_is_a_problem: Cagan names four risks and says teams should tackle value and viability risk early, before building. Feasibility is the risk engineers check by default, so value is the one most often skipped. If no one wants the product, good code does not help. Superhuman made this measurable: it asked users how they would feel if they could no longer use the product, and treated a 40% "very disappointed" share as the signal of fit.
how_to_detect:
  - Search the spec, README, and `docs/` for target users, interviews, surveys, waitlists, or experiments. Flag the project if none exist.
  - Check whether analytics or an event library is installed. Check whether any event tracks the core action, not only page views.
  - Compare the number of features against evidence of use for each one. Many features with no usage data is a flag.
  - Look for a feedback channel inside the product (feedback form, survey prompt, support link).
fixes:
  - Write the riskiest value assumption as one sentence. Design the smallest test for it before more build work.
  - Add tracking for the one core action. Define what "used" means as a number.
  - Run the "very disappointed" survey on current users. Repeat it after each major change.
sources:
  - https://www.svpg.com/four-big-risks/
  - https://www.producttalk.org/2021/08/product-discovery/
  - https://review.firstround.com/how-superhuman-built-an-engine-to-find-product-market-fit/
---

---
id: no-customer-outcome-stated
title: Features without a stated customer outcome
claim: If a spec lists features but never says what the customer can do afterward, nobody can judge whether a feature is worth building.
why_it_is_a_problem: Amazon's Working Backwards process starts from the customer experience and writes the press release first. Amazon says the process rejects most proposals, which saves resources for the strongest ideas. Torres places a desired outcome at the root of the opportunity solution tree, and every solution must connect to it. Without that root, features are compared by opinion, and scope grows with no limit.
how_to_detect:
  - Read the spec, PRD, or README intro. Check whether it names the customer, their problem, and the change they get in one or two sentences.
  - For each listed feature, try to trace it to a stated problem. Count the features that do not trace.
  - Check the issue tracker or TODO list. Flag tickets that describe UI or implementation with no user problem.
  - Check whether a success metric exists for the product or for each feature.
fixes:
  - Write a one-page press release from the customer's view. Write an FAQ with the hard questions.
  - Build a small opportunity tree: one outcome, 3 to 5 customer problems, then the existing features under them. Cut or park what does not fit.
  - Add a "Problem" and "Success measure" section to the spec template.
sources:
  - https://workingbackwards.com/resources/working-backwards-pr-faq/
  - https://www.aboutamazon.com/news/workplace/an-insider-look-at-amazons-culture-and-processes
  - https://www.producttalk.org/opportunity-solution-trees/
---

---
id: positioning-missing-alternative
title: No named alternative, so no clear reason to switch
claim: If a product does not say what customers use today instead of it, it cannot say why it is better, and users will not know when to choose it.
why_it_is_a_problem: Dunford defines positioning as five linked parts and starts with competitive alternatives, meaning what customers would do if the product did not exist. Unique attributes and value only make sense when compared to that alternative. The alternative is often a spreadsheet, a manual process, or doing nothing, and not a direct competitor. A README or landing page that lists features without this comparison makes the reader do the positioning work, and most readers will not do it.
how_to_detect:
  - Read the README first screen, landing page copy, and app store text. Check for a named alternative ("instead of X", "unlike X", "without X").
  - Check whether the target customer is stated narrowly (role, situation) or as "everyone" or "teams".
  - Check whether the feature list says what each feature lets the user do that the alternative does not.
  - Check whether the product claims a market category. If it claims none, readers will guess one.
fixes:
  - List the top 2 or 3 real alternatives, including "do nothing" and "spreadsheet". Rewrite the first paragraph to compare against them.
  - Name one narrow target customer for whom the difference matters most.
  - Map each key feature to the value it gives over the alternative. Drop features from the pitch that do not map.
sources:
  - https://www.aprildunford.com/post/a-quickstart-guide-to-positioning
  - https://www.paulgraham.com/startupideas.html
---

## 3. Extraction priorities (write these first)

1. `untested-value-risk`: four risks, value risk first (Cagan; Superhuman survey).
2. `no-customer-outcome-stated`: outcome before features (Working Backwards; Torres).
3. `no-job-defined`: no customer job or circumstance stated (Christensen Institute JTBD).
4. `positioning-missing-alternative`: no named alternative or target customer (Dunford).
5. `too-many-problems-at-once`: product tries to solve several problems (YC: one problem at a time; PG: narrow and deep beats broad and shallow).
6. `must-be-gaps`: basic expected features missing while delighters get built, such as auth recovery, export, undo (Kano).
7. `no-pmf-signal`: no metric that shows users would miss the product (Superhuman / Sean Ellis survey).
8. `premature-scaling`: automation, infra, or growth work before 10 to 100 users love it (YC advice; PG "Do Things That Don't Scale").
9. `no-defensibility-or-margin`: feature delights but is easy to copy or costs more than it earns (Biddle DHM). Verify the Medium pages in a browser first.
10. `no-pre-mortem`: spec has no failure modes or anti-goals (Doshi via Lenny ep. 3). Find a primary Doshi text first; today the support is only a podcast page.
