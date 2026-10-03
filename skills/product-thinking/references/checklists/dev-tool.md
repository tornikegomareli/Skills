# Dev tool checklist

Each item names what to look for in the code or spec. A failed item becomes a finding. Link it to a principle in `references/principles/` when one fits.

1. Time to first success is short: install and a working example in a few commands. Check: README quick start; count steps; run it if possible.
2. Error messages say what failed and how to fix it. Check: thrown errors and CLI output strings (NN/g heuristic 9).
3. Docs match the code. Check: documented flags, endpoints, and config keys against the actual parser or routes.
4. Versioning and breaking changes are visible: semver, changelog, deprecation warnings. Check: `CHANGELOG`, release tags, deprecation code paths.
5. Users can report issues and see them handled. Check: issue templates, response activity via GitHub Search API (section 4).
