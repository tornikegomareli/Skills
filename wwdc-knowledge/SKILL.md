---
name: wwdc-knowledge
description: Brings Apple's WWDC guidance into development — session transcripts, Apple's own code snippets, and the documentation each session links, as primary sources across 1638 sessions from 2014 to 2026 plus Tech Talks and Meet with Apple. Use when writing or reviewing code for an Apple platform and Apple has a recommended approach (SwiftUI, UIKit, Swift concurrency, Foundation Models, SwiftData, Metal, StoreKit); when adopting a framework or choosing between APIs; when an availability or deprecation claim needs pinning to a version; when the user names a WWDC session, a year, or asks what changed in a framework; or when another skill needs Apple's stated guidance rather than recall.
---

# WWDC Knowledge

Apple's engineers explained these frameworks on stage, and said how they intend them to be used.
Those talks are the **primary source** for both, and this skill reads them locally.

Every claim you return carries a **timecode**: `wwdc2025-286 [4:01]`. The timecode is what separates
a sourced answer from recall wearing a citation's clothes.

`wwdc.py` below means `python3 <this skill's directory>/scripts/wwdc.py`. Use the absolute path.

## Steps

1. **Find the sessions.**

   ```
   wwdc.py search "guided generation"
   wwdc.py search "scroll performance" --topic swiftui --event wwdc2026
   wwdc.py search --regex '@Generable\b' --excerpts 1
   wwdc.py search --topic ai --event wwdc2026        # survey a slice, no query
   ```

   Query terms are ANDed within a single transcript paragraph, so two or three specific words beat a
   sentence. Use `--regex` for exact API spellings that spoken prose mangles. Filter vocabulary for
   `--topic`, `--event`, and `--platform` comes from `wwdc.py info`.

   Output gives you a session id, a timecode per excerpt, and the dataset path. Carry the id
   forward; it is what `show` takes.

2. **Read what the excerpt promised.** The search excerpt is a pointer, not the answer.

   ```
   wwdc.py show wwdc2025-286                    # summary, counts, what's available
   wwdc.py show wwdc2025-286 --at 4:01 --pad 60 # sentence-level transcript around a timecode
   wwdc.py show wwdc2025-286 --code             # Apple's snippets, each with its timecode
   wwdc.py show wwdc2025-286 --resources        # linked docs, with markdown URLs
   wwdc.py show wwdc2025-286 --full             # whole transcript
   ```

   Prefer `--at` over `--full`: it returns the exact sentences to quote, and `--full` can run past
   20 KB. Reach for `--code` whenever the answer involves writing Swift, because Apple's own snippet
   beats one you compose.

3. **Follow the API into Apple's documentation.** Each resource carries a `sosumiURL`, which renders
   a `developer.apple.com` page as Markdown. Fetch it when the session names a symbol whose
   signature, parameters, or availability you need. Any Apple docs URL converts the same way:
   swap the host for `sosumi.ai`.

4. **Answer in timecodes.** Done when every API name, signature, availability claim, and line of
   code you produce traces to a transcript segment, a code snippet, or a doc page you opened this
   turn, each carrying its session id and timecode. A statement you cannot attribute that way is one
   you still need to look up, or one you present plainly as your own inference.

   When the output is code rather than prose, the citation goes in the message beside it, naming the
   session that recommends the approach.

   Quote the sentences that carry the point and link the session. These transcripts are Apple's
   copyrighted material, so short cited excerpts are the shape to use.

## Dating a claim

The corpus spans twelve years, so two sessions can both be right about different years. Prefer the
newest session covering the API, and read an older talk as a record of how the API stood that year.
When they conflict, say which year each came from. `search` sorts newer events first, so the top hit
is usually the current one.

## Dataset

Sessions live in a clone of `github.com/guitaripod/wwdc-sessions`, at `$WWDC_SESSIONS_DIR` or
`~/.local/share/wwdc-sessions`. `wwdc.py` prints the exact fix if it is missing.

- **Absent** — ask the user before running `wwdc.py setup`; it downloads about 175 MB.
- **Stale** — `wwdc.py refresh` fast-forwards it. `search` footers and `wwdc.py info` show the build
  date. Apple publishes in bursts around June, so a refresh matters most right after a WWDC.
- 87 sessions have no transcript and are flagged `[no transcript]`; their metadata still resolves.
