---
id: no-focus
title: Too many directions, no clear core
thinkers: [Steve Jobs, Mike Markkula, Jason Fried, David Heinemeier Hansson]
applies_to: [all]
---

**Claim.** A project that says yes to many directions spreads its effort thin, so no single part becomes good and the parts do not add up.

## Why it is a problem
At WWDC 1997, Jobs described Apple's engineers going in 18 different directions. Each project was arguably interesting, but the total was less than the sum of the parts. He said focus means saying no, and that saying no makes people angry. Markkula's 1977 Apple marketing memo already listed focus as one of three principles: drop what is not important. 37signals turns this into a default in "Start With No": every yes is a long-term cost in design, testing, and support. Getting Real also says Jobs kept the first iTunes small by saying no to all but the key features.

## How to detect
- Count the top-level modules, apps, or packages. For each one, ask which single user problem it serves. Flag modules that serve different users or different problems.
- Read the README and landing copy. Flag it if it describes the product with "and" lists of unrelated jobs ("CRM, chat, and analytics").
- Check the issue tracker for open epics. Flag many parallel epics with partial progress and none finished.
- Check whether a written list of non-goals or "things we will not do" exists. No list is a flag.
- Intake question: "If you could ship only one thing this month, what is it?"

## Fixes
- Pick one core use case. Write it as one sentence at the top of the README.
- Write a non-goals list. Move features outside the core to it, or archive them.
- Make "no" the default answer to new requests. Revisit a request only if users keep asking for it.

## Cases
- `sonar-engagement-over-growth` (failure)
- `apple-1997-product-grid` (success)
- `instagram-burbn-pivot` (success)
- `evernote-feature-sprawl` (failure)

## Sources
- https://www.youtube.com/watch?v=yQ16_YxLbB8 (WWDC 1997 closing Q&A, third-party upload; read via auto-captions)
- https://stevejobsarchive.com/artifact/the-apple-marketing-philosophy
- https://basecamp.com/gettingreal/05.3-start-with-no
- https://basecamp.com/gettingreal/05.1-half-not-half-assed
