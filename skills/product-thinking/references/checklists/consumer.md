# Consumer app checklist

Each item names what to look for in the code or spec. A failed item becomes a finding. Link it to a principle in `references/principles/` when one fits.

1. First-run flow reaches the core action without a forced sign-up wall. Check: onboarding screens, auth gating on first route.
2. Every async action shows loading, success, and error states. Check: network calls in views; look for missing error UI (NN/g heuristics 1 and 9).
3. Permissions (notifications, location, camera) are asked in context, not at launch. Check: where permission prompts fire (Apple HIG onboarding and privacy pages).
4. There is a trigger that brings users back (notification, email, widget) tied to a real event. Check: push or email code and what fires it. Andrew Chen's essays put most churn in the first 3 to 7 days.
5. Accessibility basics hold: labels on icon buttons, dynamic type or scalable text, contrast. Check: accessibility labels, hard-coded font sizes (WCAG 2.2).
