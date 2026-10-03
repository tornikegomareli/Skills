# AI product checklist

Each item names what to look for in the code or spec. A failed item becomes a finding. Link it to a principle in `references/principles/` when one fits.

1. The product sets expectations about what the AI can and cannot do. Check: onboarding copy, empty prompt state, example prompts.
2. Users can correct, retry, or undo AI output. Check: edit, regenerate, and undo actions (NN/g heuristic 3, user control).
3. Failure and latency are handled: streaming or progress, timeouts, model errors. Check: API error handling and loading UI (Laws of UX, Doherty Threshold).
4. Output quality is measured: evals, feedback buttons, logged ratings. Check: eval scripts, thumbs up/down events.
5. Unit cost fits the price. Check: tokens per request against plan price. ChartMogul (2025-12) reports AI-native products under $50/month at 23% GRR and 32% NRR.
