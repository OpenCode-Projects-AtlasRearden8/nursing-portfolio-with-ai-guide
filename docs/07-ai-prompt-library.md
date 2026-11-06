# AI Prompt Library

Copy-paste starters for every chapter of this manual. Each prompt is
**sanitizer-safe by design**: it only ever carries your *already- sanitized*
notes, never PHI (see [01-phi-safety.md](01-phi-safety.md)).

How to use any prompt:

1. Sanitize your raw notes first. Names/patients/dates-of-battle never survive
   into the prompt.
2. Paste the prompt below into your AI chat (any mainstream assistant, or your
   own locally-run model — nothing here needs to leave your machine).
3. **Verify the output against a real source before you file it.** AI drafts;
   your certificate, your check-off sheet, your preceptor's actual sentence
   are the records that count.
4. File the final version with the chapter it belongs to.

A shared line to append to almost every prompt:

> No patient information is included in anything I paste — keep it that way.

## 1. Getting started prompts

**Set the assistant's job (paste once, at the top of a chat):**

> You are my writing helper for a professional nursing portfolio. I am a nurse
> organizing competency sheets, CEU summaries, preceptor feedback, credentials,
> and annual-review talking points. Style: clear, honest, plain English, no
> medical-jargon padding, no invented facts. If I give you numbers, use
> them as-is and tell me if anything looks off. Never add facts I didn't give
> you. Assume everything I paste is already sanitized — and if I paste anything
> that looks like patient information, stop and tell me to sanitize first.

**Data hygiene check (run before most sessions):**

> Here is what I plan to paste into a later message. Check it for anything
> that identifies a patient, coworker, or facility and tell me only what to
> remove or generalize. Paste: [your raw notes]

## 2. Competency-sheet prompts

**Build a sheet from rough notes:**

> Turn these rough notes into a one-page competency sheet with these sections:
> Skill name, Category, Level (Introduced / Practicing / Independent /
> Experienced / Can teach), Verified by, Context, Strengths, Growth edge,
> Next step, Last updated. Keep my phrasing when it's already good. If a level
> I claimed sounds inconsistent with the notes, ask me rather than guess.
> Notes: [paste]

**Reflection-tightening:**

> Here is the reflection part of a competency sheet: [paste]. Tighten it to
> two sentences, first person, honest tone, no buzzwords, no patient story.
> It should say what's solid and what I'm actively working on.

**Level ladder sanity check:**

> I described this skill as [paste level + context]. Does that level wording
> match what I described? If not, suggest which of these fits better and why:
> Introduced, Practicing, Independent, Experienced, Can teach.

## 3. CEU-summary prompts

**Course notes → summary card + log row:**

> Here are my rough notes from a continuing-education course (sanitized, no
> patient info). Turn them into: (a) a five-field summary card — Title &
> provider, Date taken, Format, "3 things I learned," "How it changed me";
> and (b) a single-row log entry: Date, Title, Provider, Hours, Category,
> 1-line takeaway. Keep each "thing I learned" to one line I could say out
> loud. Do not invent hours or a provider name I didn't give you.
> Notes: [paste]

**Theme my CEU year:**

> From this CEU log, group my hours by category and tell me which two
> categories dominated my year. One short paragraph, no flattery.
> Log: [paste your log table]

**Compare to category plan:**

> My category targets for this year: [categories + hour goals]. Here's my log
> to date: [paste]. Where am I on track, behind, or done? Plain table.

## 4. Preceptor-feedback prompts

**Cluster feedback cards:**

> Here are my short preceptor-feedback cards from the past [N] weeks
> (sanitized — roles not names, no case details). Cluster them into 2–4
> strengths and one recurring growth theme. Quote at most once, briefly.
> Cards: [paste]

**Draft a preceptorship summary:**

> Using these clustered feedback notes, draft a one-page preceptorship summary
> in first person, four numbered points, no patient-specific content, no
> names. Tone: calm, factual, the kind of paragraph a manager who respects me
> would recognize. Notes: [paste]
> Notes: [paste]

**Turn awkward wording into a good ask:**

> I want to say to my preceptor: "[your awkward draft]." Make it one calm,
> short request I would actually say out loud, asking for feedback I can file
> in my growth record. Give two versions: casual and slightly more formal.

## 5. Annual-review prompts

**Build the 4-layer script:**

> Using the following sanitized material — competency updates [paste], CEU
> category totals [paste], feedback themes [paste], my one ask [paste], and my
> one goal [paste] — draft a four-part annual-review script, about 90 seconds
> each: Growth, Contribution, Learning, Next. Keep the ask concrete and
> one-sentence. No patient stories, no names, no invented metrics. If a claim
> has no evidence behind it in what I pasted, flag it instead of keeping it.

**Backup packet:**

> Turn the same material into a one-page evidence table with rows: Growth,
> Contribution, Learning, Next, Credentials, Feedback trend; columns: Claim /
> Supporting evidence. Short cells, table format.

**Kinder, firmer ask line:**

> Rewrite my ask — "[paste]" — so it is polite but unmistakably a request,
> with a clear what and a clear when. Two versions.

## 6. Utility prompts

**Sanitizer (use constantly):**

> Scrub this text so it cannot identify a patient, coworker, or specific
> facility, keeping only skill, setting-type, and lesson. Show me before/after
> and list what you removed. Text: [paste]

**Plain-English rewrite for renewal pages:**

> Rewrite this renewal-requirement text in plain English a busy nurse can
> act on: [paste text from the official issuer page]

**Backward planning:**

> My credential expires on DATE and the renewal takes about [N] hours. Give me
> three dates: when to do the desk work, when to finish, and when to set a
> reminder. Show the steps between each.

## Frequency of use (suggested rhythm)

| cadence | prompts you run |
|---|---|
| After any course (5 min) | #3 card + log row |
| Each shift block with feedback (2 min) | #4 card or cluster |
| Each new/level-up skill (10 min) | #2 sheet + reflection |
| Quarterly desk ritual (20 min) | #5 review-draft (first pass) + #6 backward plan |
| Annual review prep (one evening) | #5 script + packet + ask line |

Nothing here is clever. That's the point — small, repeatable, sanitized loops
that compound into a real portfolio.
