# B2B SaaS checklist

Each item names what to look for in the code or spec. A failed item becomes a finding. Link it to a principle in `references/principles/` when one fits.

1. An activation event is defined and tracked. Check: analytics calls for a named "first value" event. Benchmark: average activation is 34%, median 25% (Lenny's Newsletter, 2022).
2. A new account can invite teammates and assign roles. Check: invite flow, role model, permission checks on the server.
3. There is a way in for buyers' IT: SSO/SAML, audit log, data export. Check: auth providers, audit tables, export endpoints.
4. Billing handles plan limits, trial end, failed payment, and downgrade. Check: billing webhooks and states for `past_due` and cancel.
5. Empty states teach the next step. Check: list views with zero items; is there a call to action or sample data?
