# Fill-In Templates

Blank versions of everything in this manual. Copy a template, fill it in, run it
through the sanitizer ([01-phi-safety.md](01-phi-safety.md)), then file it.
No real data belongs in this repository — fill your copies in your own private
folder.

## Competency sheet template

```markdown
## Competency: [skill name]

- **Category:** [Procedural / Assessment / Equipment / Education / Leadership]
- **Level:** [Introduced / Practicing / Independent / Experienced / Can teach]
- **Verified by:** [skills fair check-off / preceptor sign-off / sim lab / module + post-test]
- **Context:** [setting type, rough frequency — no patient details]
- **Strengths:** [1–2 lines, honest]
- **Growth edge:** [the part you're still building]
- **Next step:** [one concrete action + target quarter]
- **Last updated:** [YYYY-MM — your own record-keeping date]
```

## CEU summary card template

```markdown
### CEU card: [course title]

- **Provider:** [provider name from the certificate]
- **Date taken:** YYYY-MM-DD
- **Format:** [online self-paced / live webinar / conference session / unit course]
- **Hours (per certificate):** [N]
- **3 things I learned:**
  1. [one line]
  2. [one line]
  3. [one line]
- **How it changed me:** [one sentence, concrete]
```

## CEU log templates

Rolling table (Markdown or spreadsheet — either works):

```markdown
| Date | Title | Provider | Hours | Category | 1-line takeaway |
|------|-------|----------|-------|----------|-----------------|
|      |       |          |       |          |                 |
```

Category subtotal check (run at your quarterly ritual):

```markdown
| Category | Hours this year | Target | Status |
|----------|-----------------|--------|--------|
|          |                 |        |        |
```

## Preceptor feedback card template

```markdown
### Feedback card

- **Date:** YYYY-MM-DD
- **Source:** [role only, unless the person consented to being named]
- **Context:** [end-of-block check-in / after first solo X / weekly 1:1]
- **What they said (or your one-line version):** "…"
- **My read:** [what you think they're actually pointing at]
- **Action:** [the one behavior you'll change, stated concretely]
```

## Preceptorship summary template

```markdown
# Preceptorship summary — [unit type], [N] weeks, [season year]

*Assembled from check-in records; sanitized per 01-phi-safety; no patient content.*

1. [Rhythm/build-up over the block]
2. [Feedback trend — what was true early vs. late]
3. [Standing skill goals still open]
4. [One sentence (from preceptor or self) worth keeping for reviews]
```

## Credential tracker template

```markdown
# Credential tracker

| Credential | Issuer | Type | Expires | First earned | Renewal requirement (plain English) | Status | Next 3 actions |
|------------|--------|------|---------|--------------|--------------------------------------|--------|----------------|
|            |        |      |         |              |                                      |        |                |

Status vocabulary: Green (>6 mo), Yellow (3–6 mo), Orange (1–3 mo), Red (<1 mo / lapsed).
Do not use full license/certificate numbers in shared copies of this file.
```

## Annual-review prep template

```markdown
# Annual review prep — [year]

## Layer 1 — Growth
- Claim: [one sentence]
- Evidence: [competency sheet / feedback note reference]

## Layer 2 — Contribution
- Claim: [one sentence about the unit or team, no names]
- Evidence: [what changed and how you know]

## Layer 3 — Learning
- CEU categories + hours: [from your log]
- One applied example: [where you used it]

## Layer 4 — Next
- Ask (needs a resource/decision): [one sentence, with what + when]
- Goal (needs only me): [one sentence, with date]

## Backup packet
| Topic | Evidence |
|-------|----------|
| Growth | |
| Contribution | |
| Learning | |
| Next | |
| Credentials (abbreviated) | |
| Feedback trend | |
```

## Filing structure template

```markdown
portfolio/
  competencies/YYYY-skill-slug.md
  ceu/YYYY-course-slug.md   (+ logs/ceu-log.md with the rolling table)
  feedback/YYYY-feedback-cards.md  (+ YYYY-quarter-summary.md)
  credentials.md
  review/YYYY-annual-review-prep.md
  sample-data/              ← keep anything fictional here
```

Everything above stays PHI-free by design; the templates force the lesson,
not the case.
