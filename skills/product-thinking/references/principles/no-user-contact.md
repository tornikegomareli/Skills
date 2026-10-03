---
id: no-user-contact
title: Founders do not talk to users
thinkers: [Paul Graham, Gustaf Alströmer, Y Combinator]
applies_to: [all]
---

**Claim.** A team that does not talk to users directly builds from guesses, and early feedback from users is the best it will ever get.

## Why it is a problem
Paul Graham says that if he could keep only one piece of startup advice, it would be to understand your users. In "Do Things That Don't Scale" he describes the Collison brothers setting up Stripe on a user's laptop on the spot, and Wufoo sending each new user a handwritten thank-you note. YC partner Gustaf Alströmer says the best founders talk to users for the whole life of the company. He points out that many startups hide behind "do not reply" email addresses. He also says users have good problems but bad solutions. Early Airbnb guests asked for host phone numbers, but the real issue was that they did not trust the platform yet.

## How to detect
- Search the code and config for `noreply`, `no-reply`, or `donotreply` sender addresses. Check whether replies reach a person.
- Check the app and README for a feedback link, support email, or contact channel that reaches the founders.
- Search `docs/` and the tracker for interview notes, call summaries, or user quotes. Check the date of the most recent one.
- Read the tracker. If nearly every issue was opened by the team and none quote a user, flag it.
- Check whether feature requests are copied into tickets as solutions, with no problem behind them.
- If there is no trace in the repo, ask intake questions 1 and 6.

## Fixes
- Replace the no-reply sender with a founder's address. Answer every reply for the next month.
- Talk to 5 users this week. Ask what they did the last time they hit the problem. Do not pitch the product.
- For each feature request, write down the problem behind it before you write a ticket.

## Cases
- `college-conductor-stack-before-customer` (failure)
- `exambuff-built-before-asking` (failure)
- `pebble-time-repositioning` (failure)
- `airbnb-photograph-listings` (success)
- `stripe-collison-installation` (success)
- `superhuman-human-onboarding` (success)

## Sources
- https://www.paulgraham.com/13sentences.html
- https://www.paulgraham.com/ds.html
- https://www.ycombinator.com/library/Iq-how-to-talk-to-users
- https://www.ycombinator.com/library/4D-yc-s-essential-startup-advice
