# PHI Safety: What Never Goes In Your Portfolio

The **do-not-include-PHI sidebar**. This page is the safety gate for the whole
manual. Read it before you touch your first competency sheet, CEU summary, or
annual-review note — and re-scan it before you share anything with an AI tool,
a preceptor, or a manager.

> **Educational content only — never medical advice.** This page is about
> *document hygiene*, not clinical care or HIPAA legal interpretation. Your
> facility's privacy policy is the authority; follow it wherever it is stricter
> than this page.

## The PHI Sidebar (copy this onto your monitor)

**DO NOT INCLUDE — in portfolio files, in AI prompts, in printed notes, anywhere:**

| Category | Examples | Why |
|---|---|---|
| Patient identifiers | Names, initials, MRN/record numbers, DOB, SSN | Direct PHI, 1:1 identifiers |
| Room/bed/locale | "48-2, telemetry," "bed 12 in the PACU" | Identifiable in combination |
| Specific dates+tell | "Tuesday night, post-op day 2" combined with procedure details | Re-identifies a person |
| Coworker names | "Preceptor Jane R." | People are people; use roles |
| Facility specifics that trace | "the only peds unit in town" | Triangulates who/where |
| Images of work | EHR screenshots, badge photos, printed MAR/labels | HIPAA-per-se violation |
| Your own excess IDs | SSN, home address, license number on drafts | Identity theft risk |
| Secrets | Passwords, login codes, API keys to anything | Plain bad practice |

The single most important word in the table is **combination**. A single detail
(rare procedure, specific date, tiny unit) is usually harmless. Two or three
combined can point at exactly one human being. When sanitizing, it is almost
never one field you remove — it is the *overlap* between fields.

## Pre-flight sanitization checklist

Run your entry through these before it goes into a prompt, a portfolio file,
or a review folder:

1. **Names gone?** No patient/coworker/facility names you don't need. Say
   "a long-term ICU patient," "my preceptor," "my mid-size community hospital."
2. **Dates generalized?** "A winter night shift" instead of "Jan 14." Exact dates
   are fine for *your own* CEU certificates and renewals — that's your record,
   not a patient's story.
3. **Numbers depersonalized?** Room numbers out. Counts about *you* are fine
   ("I did 40 IV starts across the year"); counts about *a patient* are not.
4. **Combination test?** Could a coworker recognize which patient this is? If
   yes, blur one more axis: the procedure, the date, the unit, or the outcome.
5. **Images stripped?** No screenshots or photos unless fully synthetic
   (your own mock table).
6. **AI-prompt-safety double-check?** Prompts only ever carry *sanitized,
   already-blurred* summaries. If you can't sanitize it, you can't prompt it.

## Worked example: sanitizing an anecdote

**Before (do not use):**

> On Tuesday night I had R.T., MRN 44718—, a 68-year-old in room 12 who went
> for a Whipple that afternoon, and at 0200 his Jackson-Pratt drained over
> 200 mL of blood; Dr. Mati came and we packed him, and my preceptor Kay
> coached me through hanging 4 units.

**After (sanitized, portfolio-safe):**

> During a night shift, I cared for a postoperative patient whose surgical
> drain output changed suddenly. I notified the provider, supported fluid
> resuscitation per protocol, and my preceptor coached me through IV push
> medications I had not previously administered. What I took from it: report
> drain output changes early; a calm, scripted SBAR gets a faster response.

Notice what survived: the *skill*, the *setting level*, the *lesson*. What got
removed: the person, the date, the room, the colleague, the institution.

**Test to apply:** if the before-version makes you think "oh, that was Mr. —" you
are done sanitizing; the after-version is what belongs in the portfolio.

## How this maps to the rest of the manual

- **Competency sheets** ([02](02-competency-sheets.md)) — describe the skill,
  never the patient who taught you it.
- **CEU summaries** ([03](03-ceu-summaries.md)) — CEU records are about *you*;
  they almost never touch PHI at all.
- **Preceptor feedback** ([04](04-preceptor-feedback.md)) — feedback talks about
  your practice, not cases; store learned lessons, not story details.
- **Annual review** ([06](06-annual-review.md)) — talking points come from the
  same sanitized set; you'll never need a patient story to sound competent.

## The one-line rule

> **If it would be awkward to explain to a privacy officer, don't put it in the
> portfolio — and definitely don't paste it into a chat window.**
