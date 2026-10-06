# Skills

Coding-agent skills I use every day in Claude Code, Codex, and pi: product thinking, engineering workflow, SwiftUI, Swift concurrency, and Apple platforms.

## Included skills

- `product-thinking/`: model-invoked review of a project or spec as a product. Each problem comes with proof: what it saw, the principle it breaks, and a real case. Suggests fixes and missing features. See its [README](product-thinking/README.md).
- `iphone-duo-adapt/`: model-invoked audit of an iOS app for iPhone Duo, then fixes for every problem it finds.
- `wwdc-knowledge/`: model-invoked answers from WWDC session transcripts instead of memory.

Each skill uses `SKILL.md` as its entrypoint. Supporting files sit in the skill's own folder.

### Vendored from Matt Pocock

From [mattpocock/skills](https://github.com/mattpocock/skills) v1.3.1 (MIT). Do not edit them by hand; copy them again from upstream.

- `setup-matt-pocock-skills/`: configure a repo's issue tracker, labels, and doc layout. Run it once before the others.
- `grill-with-docs/`: stress-test a plan and write ADRs and a glossary as you go.
- `improve-codebase-architecture/`: find deepening opportunities and pick one to work on.
- `codebase-design/`: design deep modules with a shared vocabulary.
- `domain-modeling/`: build a project's glossary and ADRs.
- `wayfinder/`: plan work too big for one session as decision tickets.
- `to-spec/`: turn the conversation into a spec on the issue tracker.
- `to-tickets/`: split a plan or spec into tracer-bullet tickets.
- `implement/`: implement work from a spec or tickets.
- `implement-spec/`: implement a whole spec in one run, with subagents in parallel worktrees.
- `tdd/`: build features or fix bugs test-first.
- `diagnosing-bugs/`: diagnosis loop for hard bugs and regressions.
- `research/`: research a question from primary sources into a Markdown file.
- `pr/`: write a PR body.
- `retro/`: run a retrospective on a coding session.

### Vendored SwiftUI and Swift concurrency

- `swiftui-expert-skill/`, `swift-concurrency/`: from [avdlee](https://github.com/avdlee) (MIT).
- `swiftui-pro/`: from [twostraws/swiftui-agent-skill](https://github.com/twostraws/swiftui-agent-skill) (MIT).
- `swiftui-ui-patterns/`, `swiftui-view-refactor/`, `swiftui-performance-audit/`, `swiftui-liquid-glass/`, `swift-concurrency-expert/`: from [Dimillian/Skills](https://github.com/Dimillian/Skills) (MIT).

### Other vendored skills

- `typesafe-ai/`: from [typesafe-ai/skills](https://github.com/typesafe-ai/skills) (MIT).
- `openai-docs/`: OpenAI's Codex system skill (Apache 2.0).
- `bro/`: from [dmmulroy/skills](https://github.com/dmmulroy/skills) (MIT). User-invoked: restate the last answer plainly.

Each vendored skill keeps its license file in its folder.

## Install

One skill:

```sh
npx skills add tornikegomareli/Skills --skill product-thinking -g
```

Everything, into Claude Code, Codex, and pi:

```sh
git clone https://github.com/tornikegomareli/Skills.git && cd Skills
scripts/install.sh --all
```

## License

MIT for my own skills. Vendored skills keep their original licenses.
