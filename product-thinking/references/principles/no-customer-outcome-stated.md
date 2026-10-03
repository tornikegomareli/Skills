---
id: no-customer-outcome-stated
title: Features without a stated customer outcome
thinkers: [Amazon Working Backwards (Colin Bryar, Bill Carr), Teresa Torres]
applies_to: [all]
---

**Claim.** If a spec lists features but never says what changes for the customer, nobody can judge whether a feature is worth building.

## Why it is a problem
Amazon's Working Backwards process starts with a press release written before any build. The release must name the customer, the problem in their words, and why the solution is better than what exists. Amazon's own account says most PR/FAQs never became products, and it calls that a feature, because weak ideas die before they cost engineering time. Torres puts one desired outcome at the root of the opportunity solution tree. Every solution must connect to a customer opportunity under that outcome. Without that root, teams compare features by opinion, and scope grows with no limit.

## How to detect
- Read the spec, PRD, or README intro. Check that it names the customer, their problem, and the change they get, in one or two sentences.
- For each listed feature, try to trace it to a stated problem. Count the features that do not trace.
- Read the issue tracker or `TODO` list. Flag tickets that describe UI or implementation with no user problem.
- Check whether a success metric exists for the product or for each feature.
- If the spec is silent, ask intake questions 1 and 13 (last real person with the problem, the action that shows first value).

## Fixes
- Write a one-page press release from the customer's view. Add an FAQ with the hard questions.
- Build a small opportunity tree: one outcome, 3 to 5 customer problems, then existing features under them. Park what does not fit.
- Add a "Problem" and a "Success measure" section to the spec template.

## Cases
- `slack-sell-the-outcome` (success)

## Sources
- https://workingbackwards.com/resources/working-backwards-pr-faq/
- https://www.aboutamazon.com/news/workplace/an-insider-look-at-amazons-culture-and-processes
- https://www.producttalk.org/opportunity-solution-trees/
