# Marketplace checklist

Each item names what to look for in the code or spec. A failed item becomes a finding. Link it to a principle in `references/principles/` when one fits.

1. Both sides have a reason to join before the other side is large (cold start). Check: supply-side tools or single-user value in the spec (Andrew Chen, cold start essay).
2. Search and filters return useful results with little inventory. Check: empty search result handling, fallback suggestions.
3. Trust signals exist: reviews, verification, dispute or refund flow. Check: review model, identity checks, dispute states.
4. The transaction happens on-platform, so it is hard to bypass. Check: messaging rules, payment flow, contact-info filtering.
5. Activation is measured as the first completed transaction, not sign-up. Check: analytics events. Lenny's data shows B2C marketplaces have the lowest activation rates.
