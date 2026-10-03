---
id: broken-end-to-end-experience
title: Parts work alone, but the whole journey breaks
thinkers: [Steve Jobs, Jason Fried, David Heinemeier Hansson, Ryan Singer]
applies_to: [all]
---

**Claim.** A product built and tested piece by piece can pass every piece and still fail the user, because the user goes through the whole path, including the first run and the failure states.

## Why it is a problem
Jobs judged OpenDoc by how it fit a whole product vision, not by what it could do alone. The parts had to add up to something greater than their sum. 37signals says every screen has three states: normal, blank, and error. Teams design the normal state because they test with full data. The blank state is the first thing a new user sees, and the error state is where trust is won or lost. Ryan Singer's Shape Up asks teams to finish one vertical slice, front end and back end together, early. Otherwise many tasks are done but nothing works end to end.

## How to detect
- List the user journey from discovery to install or sign-up, first use, the main result, and the return visit. Find the code or doc for each step. Flag missing steps.
- For each main screen or command, search for empty-state and error-state handling. Flag lists with no empty message and requests with no error UI.
- Check tests. Flag projects with unit tests but no end-to-end or integration test of the main flow.
- Follow the README install steps on a clean machine or container. Flag any step that fails or needs unstated knowledge.
- Check hand-offs: emails, links, redirects, and payment returns. Flag links that point to placeholders or dead routes.

## Fixes
- Write the main journey as a numbered list of steps. Add one end-to-end test that runs it.
- Design the blank state and the error state for each main screen before calling it done.
- Build one thin slice that works end to end before widening any single layer.

## Cases
- `humane-ai-pin-unfinished-launch` (failure)
- `quibi-short-form-mobile-only` (failure)
- `figma-multiplayer-browser` (success)

## Sources
- https://www.youtube.com/watch?v=yQ16_YxLbB8 (WWDC 1997 closing Q&A, third-party upload; read via auto-captions)
- https://basecamp.com/gettingreal/09.3-three-state-solution
- https://basecamp.com/gettingreal/09.4-the-blank-slate
- https://basecamp.com/gettingreal/09.5-get-defensive
- https://basecamp.com/shapeup/3.2-chapter-10
