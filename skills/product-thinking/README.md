# product-thinking

An agent skill that reviews your project as a product. It finds product problems, proves each one, gives fixes, and suggests missing features. It works on a codebase, a spec, or an idea. If it lacks information, it asks you questions first.

Every finding has a proof in three parts:

1. **Seen:** what the agent found in your project, with file paths, spec quotes, or your answers.
2. **Principle:** the product principle it breaks, from Paul Graham, Steve Jobs, Marty Cagan, Lenny's guests, and others.
3. **Case:** a real product that made the same mistake or got it right, with a source link.

A bare agent gives opinions. This skill gives findings you can check.

## Install

Install only this skill with the [`skills`](https://github.com/vercel-labs/skills) CLI:

```sh
npx skills add tornikegomareli/Skills --skill product-thinking -g
```

Or copy it into Claude Code, Codex, or pi without any tool:

```sh
for dir in ~/.claude/skills ~/.codex/skills ~/.pi/skills; do
  mkdir -p "$dir"
  curl -sL https://github.com/tornikegomareli/Skills/archive/refs/heads/main.tar.gz \
    | tar -xz -C "$dir" --strip-components=2 Skills-main/skills/product-thinking
done
```

## Use

Ask your agent in plain words, inside the project:

```
Review this project as a product.
What is missing from this app?
Check this PRD before we build it.
```

In Claude Code, you can also type `/product-thinking`.

## How it works

The agent follows seven steps from `SKILL.md`:

1. **Intake.** Reads the README, specs, landing page, onboarding, pricing, analytics, and the project's GitHub issues. Sets the goal (business, free tool, open source, internal tool) and the product type.
2. **Questions.** Asks up to 5 questions at a time about gaps it could not fill. The questions ask about things that already happened, in the style of *The Mom Test*.
3. **Audit.** Runs the checklist for the product type, then the "How to detect" checks of every principle that applies.
4. **Evidence.** Finds matching cases in the knowledge base. Fetches live user evidence: App Store reviews, Hacker News, GitHub issues and releases, Stack Overflow.
5. **Findings.** Writes each problem with its proof, severity, confidence, and fixes.
6. **Missing features.** Lists features users expect, features competitors' users ask for, and steps of the user's job the product skips.
7. **Report.** Top 3 findings first, then the top 5 findings and top 5 features in full, then open questions.

See [`EXAMPLES.md`](EXAMPLES.md) for a finished finding.

## What is inside

| Path | Content |
|---|---|
| `SKILL.md` | The steps the agent follows |
| `references/principles/` | 35 principles |
| `references/cases/` | 42 real cases, 29 failures and 13 successes |
| `references/checklists/` | 7 checklists: consumer, B2B SaaS, dev tool, marketplace, AI product, desktop app, open source |
| `references/questions.md` | Intake questions |
| `scripts/evidence.py` | Live evidence fetcher. Python 3, no dependencies, no API keys |

### Where the principles come from

| Group | Thinkers and sources |
|---|---|
| Startups | Paul Graham essays, Y Combinator library, Michael Seibel, Marc Andreessen |
| Product craft | Steve Jobs (WWDC 1997, Stanford 2005, folklore.org), 37signals *Getting Real* and *Shape Up*, Kathy Sierra |
| Product discovery | Marty Cagan (SVPG), Teresa Torres, Jobs to Be Done (Christensen Institute), April Dunford, Amazon Working Backwards, Kano model, Hamilton Helmer, Don Norman, Nielsen Norman Group |
| Growth | Lenny's Podcast and Newsletter guests (Shreyas Doshi, Elena Verna, Jason Cohen, and others), Andrew Chen, Reforge |

Every entry is written in our own words and links to its sources. Each principle file lists its thinkers and source URLs.

## Contribute

To add a principle or a case, follow [`docs/product-thinking/FORMAT.md`](../../docs/product-thinking/FORMAT.md). Every fact needs a source you opened. The research notes behind the first version are in [`docs/product-thinking/research/`](../../docs/product-thinking/research/).

## License

MIT, see [`LICENSE`](../../LICENSE). The ideas belong to the thinkers cited in each file.
