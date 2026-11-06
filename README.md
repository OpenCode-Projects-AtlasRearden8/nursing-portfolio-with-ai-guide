# Professional Portfolio With AI Help

A healthcare-*education* manual — **never medical advice** — for registered
nurses and other healthcare workers who want to build a working, sanitized,
hospital-safe professional portfolio with the help of AI tools.

Inside: competency sheets, CEU summaries, preceptor feedback language, a
credential tracker, annual-review talking points, a fill-in template pack, and
a copy-paste AI prompt library — with a standing **do-not-include-PHI sidebar**
that gates every page.

## What's here

| Path | What it is |
|---|---|
| `docs/` | The manual in plain Markdown — the source of truth |
| `site/` | Generated static HTML site (build with `python3 build.py`) |
| `build.py` | Tiny stdlib-only Markdown → HTML static site generator |
| `tests/` | Self-checks: build integrity, link resolution, PHI-pattern scan |
| `STATUS.md` | Build state, how to run, verification results, known gaps |

## Quick start

```bash
python3 build.py        # builds site/ from docs/
python3 tests/run.py    # runs the self-checks
```

Open `site/index.html` in any browser. No network needed; the site is static
and the build uses only Python's standard library.

## The three rules of the manual

1. **Never include PHI** — patient identifiers, room numbers, coworker names in
   stories, facility-tracing details — in portfolio files, notes, or AI prompts.
2. **Your portfolio describes you, not a patient.** If it reads oddly out loud
   in a hallway, rewrite it.
3. **AI drafts, you verify.** Certificates, check-off sheets, and your state
   board are the sources of truth; the AI reorganizes words, not facts.

## Where this fits

- Distinct from **ats-resume-checker-cli** (job hunting): this is not a resume
  tool; it is the year-round evidence-of-practice portfolio.
- Distinct from **new-nurse-first-year-guide** (year-one survival): this is not
  about surviving orientation; it is about keeping organized proof of growth any
  year, at any experience level.

## Safety posture

- Educational content only; your facility policy, state board, and credentialed
  reviewers always outrank this manual.
- No secrets, API keys, or personal data in this repository. All sample data
  is fictional and kept in `docs/sample-data/`.
- The build is local-first: Python stdlib, no installs, nothing phones home.

## Credits

Created and maintained by **Asdale Dynamics, LLC** as part of its
beginner-friendly AI education line (plain English, step by step, never
condescending). MIT licensed — see [LICENSE](LICENSE).

## Verification (what "it works" means here)

`python3 tests/run.py` checks that:

1. all nine docs parse and render, and `site/` regenerates byte-for-byte clean,
2. every internal Markdown/HTML link resolves,
3. the rendered HTML contains no PHI-pattern matches (MRN-like, SSN-like,
   room-number-like strings),
4. no obvious secrets/API keys are committed anywhere.

Current status and known gaps live in [STATUS.md](STATUS.md).
