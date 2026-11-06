# Read Me First

**Professional Portfolio With AI Help** — a healthcare-education manual for registered
nurses (and other healthcare workers) who want to build a working, hospital-safe
professional portfolio with the help of AI tools.

> **This manual is educational content, never medical advice.** It teaches you how to
> document, organize, and *talk about* your own professional work. It does not teach
> clinical care, does not interpret your license or credentials, and cannot make
> decisions for you. Your nursing policy manual, your state board of nursing, your
> HR department, and your credentialed preceptor/manager always outrank anything
> written here. If any advice in this manual conflicts with your facility's policy,
> follow your facility's policy.

## What this manual helps you build

By the end, you will have a clean, reusable portfolio containing:

| Portfolio piece | Doc | What it's for |
|---|---|---|
| PHI safety checklist | [01-phi-safety.md](01-phi-safety.md) | Sanitizing everything before it goes anywhere |
| Competency sheets | [02-competency-sheets.md](02-competency-sheets.md) | Documenting skills and check-offs |
| CEU summaries | [03-ceu-summaries.md](03-ceu-summaries.md) | Turning continuing education into organized, review-ready records |
| Preceptor feedback language | [04-preceptor-feedback.md](04-preceptor-feedback.md) | Asking for, recording, and summarizing feedback |
| Credential tracker | [05-credential-tracker.md](05-credential-tracker.md) | License/cert renewal dates at a glance |
| Annual-review talking points | [06-annual-review.md](06-annual-review.md) | Walking into your review prepared, not panicked |
| AI prompt library | [07-ai-prompt-library.md](07-ai-prompt-library.md) | Copy-paste prompts for every step above |
| Fill-in templates | [08-templates.md](08-templates.md) | Blank versions of everything, ready to use |

## The three rules of this manual

1. **Never put PHI (protected health information) in your portfolio, your prompts,
   or this project's files.** See [01-phi-safety.md](01-phi-safety.md). This includes
   anything that could identify a patient, coworker, or facility — that means no
   names, no room numbers, no MRNs, no "you know the guy on 4 West" stories.
   Cartoonishly specific clinical anecdotes are out; sanitized "skill + setting +
   what I learned" summaries are in.
2. **Your portfolio describes *you*, not a patient.** Every competency sheet,
   CEU summary, and talking point should pass one test: could I read this out loud
   in a hallway with the unit clerk, the charge nurse, and a visitor listening
   without anyone learning anything about a patient? If not, rewrite it.
3. **AI drafts, you verify.** AI is great at restructuring your rough notes into a
   polished sheet. AI is *not* a source of truth for your license number, your CEU
   totals, your facility's policy, or anything clinical. Every AI-generated sentence
   about your career gets checked against a real document before it goes in the
   portfolio.

## What NOT to include (the short list)

Even sanitized entries must stay scrubbed of these. See
[01-phi-safety.md](01-phi-safety.md) for the full sidebar and examples.

- Patient names or initials, MRNs, room/bed numbers, dates of birth
- Any combination of details that could point to one specific patient
- Coworker or preceptor **names** (use roles: "my ICU preceptor," "charge nurse")
- Exact facility names where a story could land on someone (use "a metro ICU" or
  keep "my facility" — your employer knows where you work, they don't need your
  notes to prove it)
- Badge/ID numbers, internal logins, screenshots of the EHR, printed work labels
- Your own identifiers you don't need here (SSN, home address)

## How to use this with AI (the friendly version)

This manual assumes you use a conversational AI assistant (a chat app, or a local
model you run yourself) as a **writing helper** — like a friend with a red pen who
never gets tired of restructuring a table.

The pattern is always the same, in every chapter:

1. **You** collect the raw, sanitized facts from your own records.
2. **You** paste a sanitizer-checked summary into a prompt from
   [07-ai-prompt-library.md](07-ai-prompt-library.md).
3. **The AI** reorganizes, tightens wording, formats a table, or drafts the summary.
4. **You** verify every factual claim against the real source, sanitize again, and
   only then file it in your portfolio (Markdown file, printed sheet, or however
   your unit stores these).

That's it. No magic. The manual just applies that loop to six different
portfolio jobs.

## Privacy of this project itself

Everything in this repository is template content — no real people, no real
records, no secrets, no API keys. The build runs entirely on your machine with
Python's standard library; nothing is sent anywhere. Load your own sanitized data
before you start filling it in.

## About

Built by **Asdale Dynamics, LLC** as part of its beginner-friendly AI education
line. It sits between two sibling projects: it is *not* a job-hunting resume tool
and *not* a first-year-new-nurse survival guide — it is the professional-portfolio
manual that a nurse uses any time of year to keep evidence of their own growth
organized, sanitized, and easy to talk about.

MIT licensed. See [LICENSE](../LICENSE).
