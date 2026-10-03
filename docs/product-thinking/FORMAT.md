# Entry format for the product-thinking knowledge base

## Rules for every entry

- Write in your own words. Never paste text from a source. No quotes longer than 10 words.
- Every factual claim (numbers, dates, what a company did) must come from a page you opened. Put that URL in `sources`.
- If you could not open a source, do not use it.
- Short, plain sentences. One idea per sentence.
- One file per entry: `skills/product-thinking/references/principles/<id>.md` or `skills/product-thinking/references/cases/<id>.md`.

## Principle file

```markdown
---
id: <kebab-case, same as file name>
title: <problem stated as a short phrase>
thinkers: [Paul Graham, ...]
applies_to: [all]   # or any of: consumer, b2b-saas, dev-tool, marketplace, ai-product
---

**Claim.** One sentence: what goes wrong and why.

## Why it is a problem
2 to 5 sentences of logic. Name the thinker and the idea. Add a real example if the source gives one.

## How to detect
- Concrete checks an agent can run on a codebase, README, spec, tracker, or analytics setup.
- If the check needs the user, say which intake question answers it.

## Fixes
- 1 to 3 options. Each is a concrete action.

## Cases
- <case ids, filled in later>

## Sources
- URLs you opened.
```

## Case file

```markdown
---
id: <kebab-case, same as file name>
product: <name>
type: failure | success
category: consumer | b2b-saas | dev-tool | marketplace | ai-product | hardware | other
year: <year of the key event>
principles: [<ids from the registry below>]
---

**Decision.** What they did.

**Outcome.** What happened. Numbers if the source gives them.

**Lesson.** One sentence.

## Sources
- URLs you opened. Prefer the founder's own post.
```

## Principle id registry

Use only these ids in `principles:`. If a case fits none, add `other-<short-name>` and say so in your report.

Group A, Paul Graham, YC, Andreessen:
`no-validated-problem`, `premature-scaling`, `too-broad-first-market`, `schlep-avoidance`, `launch-too-late`, `no-user-contact`, `no-pmf-signal`, `wrong-early-metric`, `tarpit-idea`

Group B, Steve Jobs, 37signals, Shape Up, Kathy Sierra:
`technology-first`, `no-focus`, `exposed-complexity`, `broken-end-to-end-experience`, `unbounded-scope`, `no-opinion`, `user-not-made-better`, `neglected-details`

Group C, SVPG, Torres, JTBD, Dunford, Amazon, Helmer, Norman, NN/g, Kano:
`untested-value-risk`, `no-customer-outcome-stated`, `no-job-defined`, `positioning-missing-alternative`, `must-be-gaps`, `no-defensibility`, `viability-ignored`, `usability-heuristic-violations`, `poor-feedback-and-errors`, `feature-factory`

Group D, Lenny's Podcast and Newsletter:
`no-distribution-plan`, `no-activation-metric`, `weak-retention`, `untested-willingness-to-pay`, `wrong-buyer`, `no-pre-mortem`, `high-friction-onboarding`, `no-growth-loop`
