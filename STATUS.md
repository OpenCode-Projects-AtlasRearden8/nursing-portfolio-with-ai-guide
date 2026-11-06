# STATUS.md

**Project:** Professional Portfolio With AI Help
**Owner:** Asdale Dynamics, LLC
**Last verified:** 2026-11-06

## What was built

A healthcare-*education* manual (**never medical advice**) for building a
sanitized, hospital-safe professional nursing portfolio with AI help:

- **`docs/`** — nine-chapter Markdown manual (source of truth):
  1. `00-read-me-first.md` — purpose, three rules, manual map
  2. `01-phi-safety.md` — the do-not-include-PHI sidebar + sanitization checklist
  3. `02-competency-sheets.md` — skill sheets with levels and verification
  4. `03-ceu-summaries.md` — five-field CEU cards + rolling log
  5. `04-preceptor-feedback.md` — asking/recording/summarizing feedback language
  6. `05-credential-tracker.md` — renewal dashboard + quarterly ritual
  7. `06-annual-review.md` — four-layer review script + backup packet
  8. `07-ai-prompt-library.md` — copy-paste, sanitizer-safe prompts
  9. `08-templates.md` — blank fill-in versions of everything
  Plus `docs/sample-data/` (fictional, sanitized example).
- **`site/`** — generated static HTML site (10 pages, shared CSS, PHI sidebar on
  every page, full-text prompt book) built from the docs.
- **`build.py`** — stdlib-only Markdown → HTML static site generator
  (headings with slug IDs, lists with wrapped-continuation folding, tables,
  fenced code, blockquotes, `.md#anchor` → `.html#anchor` link rewriting).
- **`tests/run.py`** — 22 self-checks (see Verification below).
- **`README.md`**, **`LICENSE`** (MIT, exact line `Copyright (c) 2026 Asdale
  Dynamics, LLC`, credit in README and site footer), **`.gitignore`**.

The AI loop baked into every chapter: you sanitize notes → paste a prompt →
the AI drafts/organizes → you verify against real records and file it.
Positioning vs. siblings: not a job-hunting ATS tool (ats-resume-checker-cli)
and not a first-year survival guide (new-nurse-first-year-guide).

## How to run it

```bash
python3 build.py        # regenerate site/ from docs/
python3 tests/run.py    # run the 22 self-checks
```

Then open `site/index.html` in any browser. No installs (Python 3 stdlib only),
no network calls, no tracking. Data is kept where you put it.

## Verification results (2026-11-06, Python 3.13.5)

`python3 tests/run.py` → **22 checks run, 0 failures, exit 0**:

- `build.py` exits 0; reports "Built site with index + 9 pages"
- all 10 site pages (index + 9 chapters) + style.css generated
- rebuild into a temp directory is byte-identical (deterministic generator)
- all relative `.md` links inside each of the 9 docs resolve
- all internal links inside the 10 site pages resolve (incl. `#anchor`)
- no unconverted markdown leftovers in rendered HTML (fences, bold, emphasis)
- PHI-pattern scan (SSN-like, MRN-like, DOB-labeled) clean over docs + site —
  with one documented negative-example exception in the safety chapter
- secret scan (API keys, tokens, private key blocks, password literals) clean
- `LICENSE` contains the exact line `Copyright (c) 2026 Asdale Dynamics, LLC`;
  README and site footer credit Asdale Dynamics, LLC

Negative testing performed: injected a fake `MRN 5552341` into a source doc —
the PHI scan flagged it in both `.md` and rendered `.html`, tests exited 1;
removed it and re-ran to all-green. Missing site pages self-heal because the
test suite rebuilds first. HTML tag balance verified with Python's html.parser
(all 10 pages balanced).

## Known gaps

- The Markdown subset is deliberately constrained (the nine known docs render
  correctly; arbitrarily complex Markdown — nested tables, nested lists,
  footnotes — is not supported by `build.py`).
- The PHI scanner is a patterns heuristic (SSN/MRN/DOB-like), not real NLP;
  it cannot catch free-form identifying prose by itself.
- Heading anchor slugs are GitHub-style but untested against GitHub rendering;
  they work in the generated site.
- No JavaScript interactivity (e.g., in-site search, dark mode) — out of scope.
- The build is not piped into CI; tests are run manually / locally.
- No release/version tagging yet; content is a first complete draft that can
  grow (e.g., more role packs: LPN, techs, CNM audiences).

## Not included, by policy

- No secrets, API keys, or real personal data anywhere; sample data is
  fictional. Nothing is pushed remotely or published; no remote was created.
