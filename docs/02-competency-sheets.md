# Competency Sheets

A **competency sheet** is a one-page, sanitized record of one skill: what it is,
what you can do with it, who verified it, and where your gaps are. Over a year
these sheets become your strongest annual-review evidence — and the raw material
for resignation letters, transfer requests, and a future resume.

> **Educational content only.** Facility check-off requirements, sim-lab passes,
> and super-user designations are set by your institution and accreditor. This
> manual shows you how to *document and talk about* competencies; your unit's
> own checklists outrank these templates.

## What makes a good competency sheet

| Element | Example (sanitized) |
|---|---|
| **Name of the skill** | Peripheral IV insertion, adult |
| **Category** | Procedural / assessment / equipment / education |
| **Level** | Introduced / practiced with supervision / independent / can teach others |
| **Verification** | Who and what: "annual skills fair check-off," "preceptor sign-off," "simulation lab" |
| **Context** | Setting type and rough frequency: "metro med-surg, ~2–4 per shift" |
| **Reflection** | What's solid, what's next, one concrete growth step |
| **No PHI** | No patients, no dates that trace, no unit identifiers |

The reflection is the part everyone skips and the part managers actually read.
Two honest sentences beat a wall of "competent at everything."

## Filled example

```markdown
## Competency: Peripheral IV insertion (adult)

- **Category:** Procedural
- **Level:** Independent (can orient students with supervision)
- **Verified by:** Annual skills fair, plus consistent preceptor feedback
- **Context:** Adult med-surg; routine workload, frequent difficult-access patients
- **Strengths:** High first-stick success on routine access; calm with anxious patients
- **Growth edge:** Ultrasound-guided PIV — observed many times, not yet signed off
- **Next step:** Schedule UGPIV module with unit educator by end of next quarter
- **Last updated:** 2026-02 (I keep my own local updated date — no patient data here)
```

## Levels you can use (plain English)

- **Introduced:** watched, technically capable, not yet trusted solo on it
- **Practicing:** do it routinely with support available
- **Independent:** do it without a check; normal part of my shift
- **Experienced:** handle the complicated versions and troubleshoot for others
- **Can teach:** oriented students/staff on it (say so only if true)

Pick honestly. "Practicing with supervision" reads as confident, not weak —
managers trust self-assessments that aren't all green.

## The AI loop for competency sheets

1. **You capture raw notes** (sanitized): skill, level, verification contexts,
   one honest reflection.
2. **You prompt the AI** to restructure. Several ready prompts are in
   [07-ai-prompt-library.md](07-ai-prompt-library.md#2-competency-sheet-prompts).
3. **AI returns** a formatted sheet, a tighter reflection, or a growth plan.
4. **You verify** against your skills-fair record/preceptor sign-off, sanitize
   once more against [01-phi-safety.md](01-phi-safety.md), then file.

Example raw note → AI prompt (both already safe to type):

> Here are my rough notes for a competency sheet (no patient info included):
> IV insertion adult, independent, skills-fair check-off last year, pretty good
> at nervous patients, weak on ultrasound-guided. Turn this into a one-page
> competency sheet with the categories: Category, Level, Verified by, Context,
> Strengths, Growth edge, Next step, Last updated.

## Anti-patterns

- Completing the sheet with a **patient story** instead of a reflection. Write
  the lesson, not the case.
- Copy-pasting a facility checklist whose wording you don't have permission to
  redistribute — paraphrase in your own words instead.
- Listing a skill at a level you can't back up if asked. Verification column
  exists precisely so every claim has a paper trail.
- Letting the sheet go stale. 20 minutes per quarter keeps a healthy one alive.

## Folder structure that works

```
portfolio/
  competencies/
    2026-iv-access.md
    2026-pacemaker-monitoring.md
  ceu/
    2026-... .md   (see 03-ceu-summaries.md)
  feedback/
    quarterly-preceptor-summary.md  (see 04-preceptor-feedback.md)
  credentials.md   (see 05-credential-tracker.md)
```

One file per competency, named `YYYY-skill-slug.md`. Ten minutes to type, a
decade to be glad you did.
