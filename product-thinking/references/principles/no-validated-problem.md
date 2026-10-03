---
id: no-validated-problem
title: Solving a problem nobody has confirmed they have
thinkers: [Paul Graham, Michael Seibel]
applies_to: [all]
---

**Claim.** A project built on an imagined problem fails because no specific person needs it badly enough to use a rough first version.

## Why it is a problem
Paul Graham says the most common startup mistake is to solve a problem no one has. In 1995 he spent 6 months building a way to put art galleries online, and the galleries did not want it. He calls ideas that come from brainstorming "made-up" or "sitcom" ideas. They sound plausible, so friends say they might use them, but nobody wants them now. Graham's test is to name who wants the product so much that they will use a buggy version from an unknown team. Michael Seibel uses a Sequoia phrase for the same bar: users whose hair is on fire. Their problem is so urgent that they accept a half-built fix.

## How to detect
- Read the README intro and spec. Check whether they name a specific user role and a specific situation in which the problem happens. "Teams", "businesses", or "anyone who" is a flag.
- Search `docs/`, the wiki, and the tracker for interview notes, support emails, or quotes from real users. If the only evidence is the founder's reasoning, flag it.
- Check whether the problem statement says how people handle the problem today. If no current workaround is named, the problem may not be real.
- Check whether the project started from a technology or an idea ("an app for X") and not from an observed pain.
- If the repo has no evidence, ask intake questions 1, 2, and 3.

## Fixes
- Name 5 real people who had the problem in the last month. If you cannot, stop feature work and find them first.
- Write the problem as one sentence: who, in what situation, what it costs them today.
- Ask each person what they did the last time the problem happened. Keep the problem only if they spent time or money on it.

## Cases
- `dinnr-survey-said-yes` (failure)
- `marginalia-launch-without-audience` (failure)
- `quibi-short-form-mobile-only` (failure)
- `wattage-prototype-before-demand` (failure)
- `dropbox-demo-video` (success)
- `notion-rebuild-kyoto` (success)

## Sources
- https://www.paulgraham.com/startupideas.html
- https://www.paulgraham.com/startupmistakes.html
- https://www.michaelseibel.com/blog/the-real-product-market-fit
