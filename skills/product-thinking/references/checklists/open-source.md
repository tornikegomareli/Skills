# Open-source project checklist

Each item names what to look for in the repo. A failed item becomes a finding. Link it to a principle in `references/principles/` when one fits.

Use this checklist next to the one for the product type. An open-source dev tool gets both `dev-tool` and `open-source`.

1. A new user gets to a working result from the README. Check: the README top screen says what the project does, who it is for, and how to install it. Count the steps to the first result. Principle: `high-friction-onboarding`. Source: https://opensource.guide/best-practices/
2. Issues get a reply. Check: run `gh issue list --state open --limit 100` and look at the oldest open issues with no maintainer comment. Many unanswered issues tell users the project is not alive. Principle: `no-user-contact`.
3. Releases are regular and readable. Check: `python3 scripts/evidence.py releases <owner/repo>` for release dates and download counts. Check for a changelog (https://keepachangelog.com/) and version numbers that signal breaking changes (https://semver.org/). Download counts per release are a usage signal when there is no analytics. Principle: `wrong-early-metric`.
4. Contributors know how to help. Check: `CONTRIBUTING.md`, issue and PR templates, a code of conduct, and labels such as "good first issue" (https://docs.github.com/en/communities/setting-up-your-project-for-healthy-contributions/creating-a-default-community-health-file, https://opensource.guide/building-community/). Principle: `no-growth-loop`.
5. The project can keep going. Check: the number of active maintainers in recent commits, and any funding (sponsors, paid tier, company backing). One maintainer with no funding is a risk to state, not a defect. Principle: `viability-ignored`. Source: https://opensource.guide/getting-paid/
6. Users can see what is planned and what is not. Check: a roadmap, milestones, or pinned issues. Check that the most-requested issues have an answer, even if the answer is no. Principle: `no-opinion`.
