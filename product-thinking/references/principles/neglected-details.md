---
id: neglected-details
title: Small details left rough in the parts users touch most
thinkers: [Steve Jobs, Andy Hertzfeld, Mike Markkula, Jason Fried, David Heinemeier Hansson]
applies_to: [all]
---

**Claim.** Users judge the whole product by the small parts they touch every day, so rough details there cost trust out of proportion to their size.

## Why it is a problem
Andy Hertzfeld's folklore.org tells how Jobs pushed for faster Mac boot in 1983. He argued that with five million users, ten seconds saved each day adds up to many lifetimes. The team then cut more than ten seconds. In 1981 Jobs pointed out rounded rectangles all around the office, and Bill Atkinson added a fast RoundRect primitive that the Mac UI used everywhere. Jobs's 2005 Stanford speech credits a Reed calligraphy class for the Mac's proportional fonts. Markkula's 1977 memo calls this "impute": people judge a product by how it is presented. 37signals adds the timing rule: work from large to small, then polish the details that real use shows.

## How to detect
- Measure the most frequent actions: startup time, page load, command run time. Flag any that feel slow or have no measurement.
- Check UI text for typos, mixed terms for one thing, placeholder text ("Lorem", "TODO", "test"), and raw error messages.
- Check visual consistency in code: hard-coded colors, spacings, and font sizes outside a token or theme file.
- Check small states: loading indicators, disabled buttons, focus states, empty lists, and long names that overflow.
- Check the edges a user meets first: app icon, page title, favicon, install message, and default CLI help output.
- Intake question: "Which three actions do users do most often each day?"

## Fixes
- List the five most frequent user actions. Time each one and set a target. Fix the slowest first.
- Run a text pass on all UI strings. Use one term per thing, and remove placeholders.
- Move colors, spacing, and type into shared tokens. Replace hard-coded values in the main screens.

## Cases
- `slack-sell-the-outcome` (success)

## Sources
- https://www.folklore.org/Saving_Lives.html
- https://www.folklore.org/Round_Rects_Are_Everywhere.html
- https://news.stanford.edu/stories/2005/06/youve-got-find-love-jobs-says (read through the web.archive.org copy; direct fetch returned 403)
- https://stevejobsarchive.com/artifact/the-apple-marketing-philosophy
- https://basecamp.com/gettingreal/04.2-ignore-details-early-on
