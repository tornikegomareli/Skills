# Examples

The project below is invented. The principles and the case are real entries from `references/`.

Project: an iOS habit tracker. Goal: a business with a $4/month subscription. Type: `consumer`.

## Finding

```markdown
### 1. Nobody knows when a new user gets value  [critical] [confidence: high]

**Seen.** `Analytics.swift` logs `app_open` and `paywall_shown` only. No event fires when a user completes a habit. The README calls 2,000 downloads "traction". The user answered intake question 13 with "we don't know".
**Principle.** No defined moment when a new user gets value (`no-activation-metric`). Without an activation event, the team cannot see where new users drop off, and the first days are where most of them leave.
**Case.** Superhuman made onboarding calls mandatory and measured activation. Those users activated at 2x the self-serve rate. https://review.firstround.com/superhuman-onboarding-playbook/
**Fix.**
- Recommended: define activation as "completed the same habit on 3 days in the first week". Log it, and chart it weekly. It is one event and one chart.
- Add a day-1 reminder tied to the habit the user created, and measure its effect on that event.
```

## Missing feature

```markdown
- **Streak repair.** Problem: one missed day resets a long streak, and users quit after the reset. Evidence: 9 of the 40 newest App Store reviews of the top two competitors mention losing a streak. Effort: small. Fixes finding 1, because it keeps users past their first missed day.
```

## Report opening

```markdown
1. Nobody knows when a new user gets value (critical).
2. The paywall shows before the first habit is done (major).
3. No reason to come back on day 2 (major).
```
