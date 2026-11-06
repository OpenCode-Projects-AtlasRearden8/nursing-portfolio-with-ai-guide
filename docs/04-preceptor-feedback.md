# Preceptor Feedback Language

Preceptor feedback is the most valuable — and most perishable — material in a
portfolio. It is valuable because it is *somebody accountable noticing how you
actually practice*. It is perishable because between "how'd the shift go?" and
"can you write two sentences about my IV skills?" lies exactly one week.

This chapter gives you language: how to **ask for** feedback, how to **record**
it, and how to **summarize** a whole preceptorship without turning it into a
case list. Feedback records talk about *your practice*, never *cases*, so this
chapter is naturally low-PHI — careful with "the time I learned from Mrs.
whatever" anecdotes anyway.

> **Educational content only.** Formal, written evaluations use your facility's
> language and rubric — those documents belong to HR, not to this template.
> What's here is the *informal* note-keeping layer that survives between
> official reviews.

## Asking (say it once, simply)

Most people fail to get feedback not because preceptors don't want to give it,
but because the question is too big ("anything for me?"). Ask for one thing,
at one moment:

| Moment | What you can actually say |
|---|---|
| End of a shift block | "One thing I did well this block and one to sharpen?" |
| After a specific skill | "How did that go compared to how you'd want it in six months?" |
| Once per preceptorship | "I keep a growth record. Two sentences of feedback I can file, please?" |
| When you're unsure | "Where are you guessing about my readiness, and what would settle it?" |

**Why "two sentences I can file" works:** it's small enough to be honest, and
naming that you keep a record makes both of you take the two sentences
seriously. Bring it up on day one, not day ten.

## Recording (the feedback card)

One card per feedback moment, 30 seconds to write:

```
Date (real — it's your own record)
Source: my ICU preceptor (role, not name, unless
         they've ok'd being named)
Context: end-of-shift check-in / after first solo
         med pass / weekly one-on-one
What they said (or the closest one-line version):
  "Slightly slow to call for help, great pattern of
   saying what they're thinking as it happens."
My read: They want earlier escalation. That matches
  what I noticed myself.
Action: Tell the charge nurse a plan before problems,
  not during.
```

Sanitize before filing: coworker names only with their permission; absolutely no
case details in the "context" line — a skill happens, that's enough.

## Summarizing a preceptorship (the shared language doc)

Between evaluations, keep a one-page running summary the way the two of you cut
up the work — numbered, plain, no individuals:

```markdown
# Preceptorship summary — ICU, 12 weeks, spring 2026

*Assembled from weekly check-in records; no patient-specific content.*

1. Built independent rhythm over the block: first two solo med passes,
   then routine prioritization.
2. Feedback trend: moved from "look things up before asking" to
   "thinking process is now consistent" — kept both habits.
3. Standing skill goals: UGPIV sign-off; ACLS megacode confidence.
4. One sentence the preceptor said I should keep for reviews:
   "Moderates speed down and accuracy up during high-stress passes."
```

Notice: zero PHI, zero names, zero real dates that could re-identify — and it
still reads like a real preceptorship happened.

## The AI loop for feedback

1. You paste your sanitized feedback cards into a prompt from
   [07-ai-prompt-library.md](07-ai-prompt-library.md#4-preceptor-feedback-prompts).
2. The AI **clusters** the cards into strengths/themes and finds the trend.
3. You read the AI's summary and **correct anything false** — AI is great at
   merging notes and terrible at knowing whether you actually improved.
4. You write the final summary *from the AI's draft* in your own voice.

Prompt input example (safe to type):

> I have four short feedback notes from my preceptor over 12 weeks (no patient
> info, no names). Cluster them into 2–4 strengths and 1 common growth theme,
> and draft a one-paragraph summary I can file. Notes: [paste your cards]

## Anti-patterns

- Collecting feedback and never reading it back — the *trend across cards* is
  the real gift; single cards are just weather.
- Recording cases in the context line. "After handling a rapid-response in a
  post-op patient" tells a story. "After my first rapid-response" is all you need.
- Copying formal HR evaluation language into your own file. Use your words.
- Turning feedback into self-criticism. Feedback is data about *practice*
  patterns, not a verdict on you as a person.
