# Credential Tracker

The **credential tracker** is the one-page dashboard of everything you're
licensed or certified to do, and when it expires. It's the least AI-flavored
chapter of this manual — the data comes from certificates and regulatory
mail — but AI still earns its keep here: as a renewal-checklist generator, a
reminder-keeper, and a plain-English explainer of renewal rules.

> **Educational content only.** Your state board, your certification body, and
> your facility's education department own this truth. Never let a chatbot's
> recital of "renewal requirements" stand in for looking at the actual renewal
> page. Treat every AI answer about credentials as a summary that *must* be
> checked against the source.

## The tracker table

One table, one file (`credentials.md` in your portfolio folder), one update per
week at most:

| Credential | Issuer | Type | Expires | First earned | Renewal requirement (plain English) | Status | Next 3 actions | Hours required for CEU | Next date |
|---|---|---|---|---|---|---|---|---|---|
| RN license | State board | License | 2027-10-31 | 2020-05-15 | Renew online, pay fee | Green — renew window Aug | Check email for CEU attestation form | 20 per 2 yrs (per board) | 2026-08 |
| BLS | National certifying org | Cert | 2026-11-30 | 2019-02-04 | Instructor-led course, ~4 hrs | Yellow — book by Oct | Book class; request CEU credit; file the new card in my records | Per course | 2026-10 |
| PCCN (sample) | Nursing certification board | Cert | 2028-01-15 | 2024-01-15 | 100 CE hrs over 3 yrs OR re-exam | Green — accumulating | Log CEU courses into [03-ceu-summaries.md](03-ceu-summaries.md) log; verify policy annuals | Varies (per org) | 2027-01 |

**Status colors** (use in your file, plain text is fine):
`Green` (>6 months out), `Yellow` (3–6), `Orange` (1–3), `Red` (lapsed or <1
month). Seeing a column of color names is faster than doing date math.

## The renewal protocol (any credential, same 5 steps)

1. **Pull the source page.** Find the issuer's official renewal page. Screenshot
   to your own private location if it helps. Never rely on memory or copy
   someone else's summary.
2. **Write the requirement in plain English.** One sentence: what, how many
   hours, what form, what fee. That sentence's wording is yours — it is the one
   thing LLMs *can* help rewrite.
3. **Backward-plan 3 dates.** (a) date the renewal is due, (b) date you must
   *start* the course/exam process to finish in time (usually 8–12 weeks
   earlier), (c) date to do the desk work (70+ days before due).
4. **Record it in this table.** Add "Next action + date."
5. **Set the calendar** on the device you actually look at (phone, wall calendar
   — whichever you will not ignore).

## How AI helps (within guardrails)

| Use | Prompt style |
|---|---|
| Plain-English renewal language rewrite | "Rewrite this renewal requirement in plain English: [paste from source page]." |
| Renewal checklist generation | "Make a 5-step checklist to renew this credential: [paste plain-English requirement + due date]." |
| Backward planning | "If this expires 2026-11-30 and takes ~4 hours of course time, give me three dates: bench work, finish, calendar alarm." |
| Cross-checking | "Given this table, which two are due in the next quarter?" (from your own data) |

**Guardrail:** pasted text about *your own credentials* is the safest prompt
input the whole manual has to offer (it's about you, not patients). But no —
don't paste your full license number or SSN into a chat. Redact
"RN-000000X" to "RN-XXXXX00X" (keep just enough shape to recognize);
your transcript is still usable.

## Quarterly desk ritual (20 minutes)

- [ ] Add/update every credential's row — including days
- [ ] Recompute CEU totals year-to-date from the log in [03-ceu-summaries.md](03-ceu-summaries.md)
- [ ] Verify any newly earned cert physically arrived (not just submitted)
- [ ] Anything `Yellow`? Book the course *now*, not next quarter
- [ ] One line "Notes" per row on any weirdness (fee changed, provider moved,
      prerequisite added)

That's the entire lifetime maintenance of a credential tracker. Under 30
minutes, four times a year.

## Anti-patterns

- Replacing "issuer" with a nickname ("that nurse board thing") — a loss of
  of precision you will regret in renewal season.
- Storing your license number repeatedly in shared docs. Keep it in your
  private record at home; "RN license" is enough of a label here.
- Trusting any chatbot on "does this course count toward X" — there is exactly
  one source of truth and it is not a language model.
- Letting the tracker drift because "the emails will remind me." They will
  not arrive at the pace you need.
