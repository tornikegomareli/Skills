---
id: schlep-avoidance
title: Avoiding the hard, tedious part that holds the value
thinkers: [Paul Graham]
applies_to: [all]
---

**Claim.** A project that skips the unpleasant work in its domain often skips the part that makes it worth paying for.

## Why it is a problem
Paul Graham calls a tedious, unpleasant task a schlep. He says founders tend not to see ideas that require schleps, and he names this schlep blindness. His main example is Stripe: thousands of programmers knew online payments were painful, but they built recipe sites instead. Fixing payments meant deals with banks, fraud, and regulation. Graham argues the hard ideas face less competition because most founders are scared away. In his list of startup mistakes he adds that founders who only want to write code avoid the business work, and that one founder in YC's 2005 batch spent half his time with phone company executives and did best by a wide margin.

## How to detect
- Read the spec's "out of scope" or "non-goals" section. Flag items that are the core pain of the domain: payments, compliance, data import, integrations with legacy systems, or onboarding of hard-to-reach users.
- Search the code for mocks, stubs, or `TODO` markers on the integration that delivers the main value.
- Check whether the product requires users to do the hard part themselves ("bring your own provider", "export your data and upload a CSV").
- Compare the feature list with what the alternative tool does. If the product only covers the easy, visible layer, flag it.
- If unsure what the hard part is, ask intake questions 4 and 8.

## Fixes
- List the 3 most painful tasks a user must do today to solve the problem. Pick the one the product will take on fully.
- Do that task by hand for the first users before you automate it.
- Move the hard integration from "later" to the first milestone, and cut easier features to make room.

## Cases
- `airbnb-photograph-listings` (success)

## Sources
- https://www.paulgraham.com/schlep.html
- https://www.paulgraham.com/startupmistakes.html
