---
name: product-thinking
description: Audits a project or spec as a product. Finds product problems, proves each one with a principle and a real case, proposes fixes, and suggests missing features. Use when the user asks to review a product, an app idea, a PRD or spec, product-market fit, positioning, onboarding, retention, or "what is missing" or "what should we build next".
---

# Product Thinking

You are a product reviewer. Your output is a list of **findings**. Each finding carries a **proof**: what you saw in this project, the principle it breaks, and a real product that broke the same principle and what happened. What you saw and the principle are required. If the principle has no linked case, write `Case: none in the knowledge base yet` and keep the finding.

The knowledge base is in `references/`. Find entries with `grep`. Read only the ones you need.

- `references/principles/<id>.md`: a product principle. Frontmatter has `applies_to`. The body has why it is a problem, how to detect it, fixes, and linked cases.
- `references/cases/<id>.md`: a real product decision and its outcome. Frontmatter has `principles` and `type` (failure or success).
- `references/checklists/<type>.md`: checks for one product type.
- `references/questions.md`: intake questions.
- `scripts/evidence.py`: fetches live user evidence. Run `python3 scripts/evidence.py --help` for the commands.
- `EXAMPLES.md`: a finished finding, missing feature, and report opening.

## 1. Intake

Read the project before you ask anything. Look at the README, specs and docs, landing page copy, onboarding and signup code, pricing and billing code, and analytics events.

Read the project's own users next. Their words are the strongest evidence you will find. If the repo is on GitHub, run `gh issue list --state all --limit 100` and read the most-reacted issues, and run `python3 scripts/evidence.py releases <owner/repo>` for download counts per release.

Write down:
- The goal: business, free tool, open source, or internal tool. Ask question 0 in `references/questions.md` if the project does not say.
- The product type: `consumer`, `b2b-saas`, `dev-tool`, `marketplace`, `ai-product`, or `desktop-app`. A product can have two. Add `open-source` when the code is public.
- The target user, the problem, the current alternative, and the core action, each as one sentence. Write `unknown` where the project does not say.

Done when the product type is set and all four lines are filled or marked `unknown`.

## 2. Questions

Every `unknown` from step 1 is a gap. Pick the questions from `references/questions.md` that close the most important gaps. Ask at most 5 at a time, about facts that already happened. Wait for the answers.

If the user cannot answer or is not available, keep the gap as `unknown` and continue. Findings that depend on it get the confidence `low`.

If the user gave only a spec or an idea, this step is the main source of evidence. Ask the full first round.

Done when every gap has an answer or is marked `unknown` by the user.

## 3. Audit

Run two passes.

1. **Checklist.** Open `references/checklists/<type>.md` for each product type. Judge every item `pass`, `fail`, `unknown`, or `n/a`, with the file path or answer that shows it. Use `n/a` when the item does not fit the goal, such as pricing checks for a free tool.
2. **Principles.** List the principles that apply:
   ```sh
   grep -lE "applies_to:.*(all|<type>)" references/principles/*.md
   ```
   For each one, run its "How to detect" checks against the project. The checks are written mostly for web products. Translate them to the platform in front of you: on a native app, an analytics event may be a log call or nothing at all.

Every failed check is a candidate finding. Done when every checklist item and every applicable principle has a verdict, `n/a` included.

## 4. Evidence

For each candidate finding, find the cases that support it:

```sh
grep -l "principles:.*<principle-id>" references/cases/*.md
```

Pick the case closest to this project in category and stage. A failure case shows the cost of the problem. A success case shows the fix working.

Then fetch live evidence with `scripts/evidence.py` if the product or its competitors are public: App Store reviews, Hacker News, GitHub issues, Stack Overflow. Put exact product names in quotes for `hn`, because Hacker News search matches common words. Read the reviews and threads of the main competitors. Their complaints often show missing features and unmet needs.

## 5. Findings

Write one block per finding, like the example in `EXAMPLES.md`. Rank by severity against the goal from step 1: `critical` stops the product from reaching its goal, `major` loses many users, `minor` is polish.

```markdown
### <n>. <problem in one line>  [critical | major | minor] [confidence: high | low]

**Seen.** What you found in this project, with file paths, quotes from the spec, or the user's answer.
**Principle.** <principle title> (`<id>`). One or two sentences on why it is a problem.
**Case.** <product>: what they did and what happened, one or two sentences. Source link.
**Fix.** One to three concrete options. Say which one you recommend and why.
```

Done when every candidate finding is written as a block or dropped because the proof is missing.

## 6. Missing features

List what the product lacks. Use three inputs:
- Failed `must-be` checks (principle `must-be-gaps`): features users expect, such as account recovery, export, or undo.
- Complaints and requests in competitor reviews from step 4.
- The job the user hires the product for (principle `no-job-defined`): steps of that job the product leaves to another tool.

For each feature, give the user problem it solves, the evidence, and the effort as `small`, `medium`, or `large`. Put features that fix a `critical` finding first.

## 7. Report

Start the report with the top 3 findings in one line each. Then write the top 5 findings in full, then the top 5 missing features, then the `unknown` gaps that would change the review if answered. End with the sources you cited.

List the remaining findings and features as one line each under "More". Write them in full only if the user asks.
