---
id: technology-first
title: Starting from the technology instead of the user
thinkers: [Steve Jobs, Jason Fried, David Heinemeier Hansson]
applies_to: [all]
---

**Claim.** A product built outward from a technology has no clear user benefit, so the team cannot explain it, sell it, or judge what to cut.

## Why it is a problem
At WWDC 1997, Jobs said you must start with the customer experience and work backwards to the technology. He said he had made the opposite mistake more than anyone in the room. His example was the LaserWriter: it had a new print engine, PostScript, and AppleTalk inside. The pitch was only the printed page, because the buyer did not need to know what was in the box. 37signals makes the same point for software in "Interface First": design the screen the user sees before the code, because the interface is the product.

## How to detect
- Read the README first screen. Flag it if it names the stack, model, or architecture before it says what a user can do.
- Check the feature list. Flag items named after a technology ("vector search", "WebSocket sync", "GPT-4 integration") with no user result next to them.
- Compare the commit history: if infrastructure, frameworks, or plugins came weeks before the first user-facing screen or command, flag it.
- Look for a spec or doc that names a user and a situation. If the only "why" is "because we can do X", flag it.
- Intake question: "Who asked for this, and what were they doing when they needed it?"

## Fixes
- Write one paragraph about the user's experience after the product works. Remove every technical term from it. Rebuild the README intro from that paragraph.
- Rename features by the result the user gets. Move technology names to a "How it works" section.
- Design the main screen or main command output first. Build only the technology that this screen needs.

## Cases
- `college-conductor-stack-before-customer` (failure)
- `exambuff-built-before-asking` (failure)
- `juicero-hardware-cost` (failure)
- `tract-ai-planning-editor` (failure)
- `wattage-prototype-before-demand` (failure)
- `google-glass-explorer-vs-enterprise` (failure)

## Sources
- https://www.youtube.com/watch?v=yQ16_YxLbB8 (WWDC 1997 closing Q&A, third-party upload; read via auto-captions)
- https://basecamp.com/gettingreal/09.1-interface-first
- https://stevejobsarchive.com/stories/40-years-of-macintosh
