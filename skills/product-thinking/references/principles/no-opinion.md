---
id: no-opinion
title: Trying to please everyone, so the product takes no side
thinkers: [Jason Fried, David Heinemeier Hansson, Kathy Sierra]
applies_to: [all]
---

**Claim.** A product that avoids decisions, through endless options or a neutral pitch, gives no one a strong reason to choose it.

## Why it is a problem
37signals says good software has a vision and takes sides. A clear point of view draws users who share it and turns away users who do not, and that is acceptable. Their example is the wiki, which removed author ownership on purpose, and that choice shaped Wikipedia. "Avoid Preferences" says to make the call for the customer: pick 25 messages per page and newest first, instead of adding a setting. Kathy Sierra points the same way: a product that offers many choices and no defaults drains the user's limited mental effort.

## How to detect
- Count settings and toggles that change core behavior. Flag settings added because the team could not agree.
- Read the README and landing copy. Flag text that says "flexible", "for any team", or "fully customizable" without naming a user or a way of working.
- Check for a written stance: a philosophy, principles, or "why we built it this way" section. No stance is a flag.
- Search the tracker for feature requests that were accepted only because one customer asked. Flag a pattern of yes with no stated rule.
- Intake question: "Which users do you want to lose, and why?"

## Fixes
- Write three to five product principles that say what the product believes. Put them in the README or docs.
- Replace each low-use setting with one default. Note the reason in the docs.
- Name the user the product is not for. Use this to answer new requests.

## Cases
- `linear-opinionated-workflow` (success)

## Sources
- https://basecamp.com/gettingreal/04.6-make-opinionated-software
- https://basecamp.com/gettingreal/06.4-avoid-preferences
- https://businessofsoftware.org/2014/05/building-the-minimum-badass-user-pt-2-unfinished-business-kathy-sierra/
