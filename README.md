# Skills

Agent skills I use every day in Claude Code and Codex. Each skill is a folder with a `SKILL.md`. The same folder works in Claude Code, Codex, and pi.

## Install

```sh
git clone https://github.com/tornikegomareli/Skills.git && cd Skills
./install.sh --list            # show available skills
./install.sh tdd bro           # install some skills
./install.sh --all             # install every skill
```

The script copies each skill into `~/.claude/skills`, `~/.codex/skills`, and `~/.pi/skills`. If a skill with the same name exists there, the script replaces it. To use other directories, set `SKILL_TARGETS`:

```sh
SKILL_TARGETS="$HOME/.claude/skills" ./install.sh tdd
```

You can also copy a folder from `skills/` by hand.

## Catalog

### Product

Written by [@tornikegomareli](https://github.com/tornikegomareli) (MIT).

| Skill | Use it to |
|---|---|
| [`product-thinking`](skills/product-thinking) | Review a project or spec as a product: problems with proof, fixes, missing features |

### Engineering workflow

From [mattpocock/skills](https://github.com/mattpocock/skills) (MIT), commit `d81f3a1`. Run `setup-matt-pocock-skills` once per repo before the others.

| Skill | Use it to |
|---|---|
| `setup-matt-pocock-skills` | Configure a repo's issue tracker, labels, and doc layout |
| `grill-with-docs` | Stress-test a plan and write ADRs and a glossary as you go |
| `improve-codebase-architecture` | Find deepening opportunities and pick one to work on |
| `codebase-design` | Design deep modules with a shared vocabulary |
| `domain-modeling` | Build a project's glossary and ADRs |
| `wayfinder` | Plan work too big for one session as decision tickets |
| `to-spec` | Turn the conversation into a spec on the issue tracker |
| `to-tickets` | Split a plan or spec into tracer-bullet tickets |
| `implement` | Implement work from a spec or tickets |
| `tdd` | Build features or fix bugs test-first |
| `diagnosing-bugs` | Run a diagnosis loop on hard bugs and regressions |
| `research` | Research a question from primary sources into a Markdown file |
| `pr` | Write a PR body |
| `retro` | Run a retrospective on a coding session |

### SwiftUI and Swift concurrency

| Skill | Use it to | Source |
|---|---|---|
| `swiftui-expert-skill` | Write and review SwiftUI: state, composition, performance | [avdlee/swiftui-agent-skill](https://github.com/avdlee/swiftui-agent-skill) (MIT) |
| `swift-concurrency` | Fix concurrency issues and migrate to Swift 6 | [avdlee/swift-concurrency-agent-skill](https://github.com/avdlee/swift-concurrency-agent-skill) (MIT) |
| `swiftui-pro` | Review SwiftUI for modern APIs and maintainability | [twostraws/swiftui-agent-skill](https://github.com/twostraws/swiftui-agent-skill) (MIT) |
| `swiftui-ui-patterns` | Build views, navigation, and layouts | [Dimillian/Skills](https://github.com/Dimillian/Skills) (MIT) |
| `swiftui-view-refactor` | Split large views and clean up data flow | [Dimillian/Skills](https://github.com/Dimillian/Skills) (MIT) |
| `swiftui-performance-audit` | Find slow rendering and excess view updates | [Dimillian/Skills](https://github.com/Dimillian/Skills) (MIT) |
| `swiftui-liquid-glass` | Adopt the iOS 26 Liquid Glass API | [Dimillian/Skills](https://github.com/Dimillian/Skills) (MIT) |
| `swift-concurrency-expert` | Review concurrency for Swift 6.2+ | [Dimillian/Skills](https://github.com/Dimillian/Skills) (MIT) |

### Apple platforms

Written by [@tornikegomareli](https://github.com/tornikegomareli) (MIT).

| Skill | Use it to |
|---|---|
| `iphone-duo-adapt` | Audit an iOS app for iPhone Duo and fix what breaks |
| `wwdc-knowledge` | Answer from WWDC session transcripts instead of memory |

### AI APIs

| Skill | Use it to | Source |
|---|---|---|
| `typesafe-ai` | Build typed AI judgments with the TypeSafe System One API | [typesafe-ai/skills](https://github.com/typesafe-ai/skills) (MIT) |
| `openai-docs` | Answer questions about OpenAI models, the API, and Codex from official docs | OpenAI Codex system skill (Apache 2.0, `LICENSE.txt` in the folder) |

### Writing

| Skill | Use it to | Source |
|---|---|---|
| `bro` | Restate the last answer in plain language (call it by hand) | [dmmulroy/skills](https://github.com/dmmulroy/skills) (MIT) |

## Add a skill

1. Put the skill folder in `skills/<name>/`. The folder name must match `name:` in `SKILL.md`.
2. Add a row to the catalog with its source and license.
3. If the skill comes from another repo, put its license in `licenses/`.

## Licenses

The install script, the README, and my own skills are MIT, see `LICENSE`. Third-party skills keep their original licenses. Copies are in `licenses/`.
