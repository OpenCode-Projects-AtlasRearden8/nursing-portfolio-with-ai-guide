#!/usr/bin/env python3
"""Static site generator for the Professional Portfolio With AI Help manual.

Stdlib-only: converts docs/*.md into site/*.html with a shared template that
carries the never-medical-advice banner, the do-not-include-PHI sidebar, page
navigation, and the Asdale Dynamics, LLC credit.

Usage: python3 build.py [--out site]
"""

import argparse
import html
import re
from pathlib import Path

ROOT = Path(__file__).resolve().parent
DOCS = ROOT / "docs"

# (slug, title, short description) — the manual's page order
PAGES = [
    ("00-read-me-first", "Read Me First",
     "What this manual builds, and the three rules that guard it."),
    ("01-phi-safety", "PHI Safety",
     "The do-not-include-PHI sidebar: what never goes in your portfolio."),
    ("02-competency-sheets", "Competency Sheets",
     "One-page, sanitized records of each skill you can do."),
    ("03-ceu-summaries", "CEU Summaries",
     "Five-field cards plus a rolling log that make courses retrievable."),
    ("04-preceptor-feedback", "Preceptor Feedback Language",
     "Asking for, recording, and summarizing preceptor feedback."),
    ("05-credential-tracker", "Credential Tracker",
     "One dashboard of every license and certification renewal."),
    ("06-annual-review", "Annual-Review Talking Points",
     "Turn your sanitized records into a four-layer review script."),
    ("07-ai-prompt-library", "AI Prompt Library",
     "Copy-paste, sanitizer-safe prompts for every chapter."),
    ("08-templates", "Templates",
     "Blank fill-in versions of everything, ready to copy."),
]

TITLE = "Professional Portfolio With AI Help"
TAGLINE = "A healthcare-education manual for nurses — never medical advice."
BANNER = ("Educational content only — this manual teaches documentation, "
          "organization, and professional communication. It is never medical "
          "advice; your facility policy and state board always outrank it.")

PHI_SIDEBAR = [
    ("Never include patient identifiers",
     "Names, initials, MRNs, dates of birth, room/bed numbers."),
    ("Watch for identifying combinations",
     "A rare procedure + a date + a unit can point at one specific patient."),
    ("Use roles instead of names",
     "“my preceptor,” “charge nurse” — never “Jane R. on 4 West.”"),
    ("No screenshots or photos of work",
     "EHR screenshots and printed MARs violate privacy outright."),
    ("No secrets, ever",
     "Logins, badge numbers, API keys stay out of files and prompts."),
]

STYLE = """\
:root {
  --ink: #1c2733; --muted: #5b6b7b; --line: #d9e1e8;
  --accent: #0f6d5f; --accent-soft: #e8f3f1;
  --warn: #9d3b12; --warn-bg: #fdf1e7; --warn-line: #e7b98f;
  --code-bg: #f4f7f9;
}
* { box-sizing: border-box; }
body {
  margin: 0; color: var(--ink);
  font: 16px/1.6 Georgia, "Times New Roman", serif;
  background: #fbfcfd;
}
.layout { display: flex; max-width: 1100px; margin: 0 auto; gap: 32px; padding: 24px; }
main { flex: 1; min-width: 0; }
nav.sidebar {
  width: 220px; flex-shrink: 0;
  font-family: Verdana, sans-serif; font-size: 13px;
}
nav.sidebar h2 {
  font-size: 12px; letter-spacing: .08em; text-transform: uppercase;
  color: var(--muted); margin: 0 0 8px;
}
nav.sidebar a {
  display: block; padding: 5px 8px; border-radius: 4px;
  color: var(--ink); text-decoration: none; margin-bottom: 2px;
}
nav.sidebar a:hover { background: var(--accent-soft); }
nav.sidebar a.active { background: var(--accent); color: #fff; }
.phisidebar {
  background: var(--warn-bg); border: 1px solid var(--warn-line);
  border-radius: 6px; padding: 14px 16px; margin: 0 0 20px;
  font-family: Verdana, sans-serif; font-size: 13px;
}
.phisidebar h2 { margin: 0 0 8px; color: var(--warn); font-size: 14px; }
.phisidebar ul { margin: 0; padding-left: 18px; }
.phisidebar li { margin-bottom: 5px; }
.phisidebar b { color: var(--warn); }
.phisidebar a { color: var(--warn); }
.banner {
  background: var(--accent-soft); border-left: 4px solid var(--accent);
  padding: 10px 14px; margin-bottom: 20px; border-radius: 0 6px 6px 0;
  font-family: Verdana, sans-serif; font-size: 13px; color: var(--ink);
}
header.site { padding: 24px 24px 0; max-width: 1100px; margin: 0 auto; }
header.site h1 { margin: 0; font-size: 26px; }
header.site p { margin: 4px 0 12px; color: var(--muted); font-size: 14px; }
h1, h2, h3, h4 { line-height: 1.25; font-weight: 700; }
main h1 { font-size: 24px; margin-top: 8px; }
main h2 { font-size: 19px; margin-top: 1.4em; border-bottom: 1px solid var(--line); padding-bottom: 3px; }
main h3 { font-size: 16px; margin-top: 1.2em; }
p, li { max-width: 70ch; }
a { color: var(--accent); }
code {
  font-family: "SFMono-Regular", Consolas, monospace; font-size: .88em;
  background: var(--code-bg); border: 1px solid var(--line);
  border-radius: 3px; padding: 1px 4px;
}
pre {
  background: var(--code-bg); border: 1px solid var(--line);
  border-radius: 6px; padding: 12px 14px; overflow-x: auto;
}
pre code { background: none; border: none; padding: 0; }
table { border-collapse: collapse; margin: 1em 0; font-size: 14px; max-width: 100%; display: block; overflow-x: auto; }
th, td { border: 1px solid var(--line); padding: 6px 10px; text-align: left; vertical-align: top; }
th { background: var(--accent-soft); font-family: Verdana, sans-serif; font-size: 12.5px; }
blockquote {
  margin: 1em 0; padding: 6px 14px; color: #3d4c5a;
  border-left: 3px solid var(--accent); background: #f6faf9;
  border-radius: 0 6px 6px 0; max-width: 70ch;
}
blockquote p { margin: .3em 0; }
hr { border: none; border-top: 1px solid var(--line); margin: 1.6em 0; }
.cards { display: grid; grid-template-columns: repeat(auto-fill, minmax(260px, 1fr)); gap: 14px; padding: 0; list-style: none; }
.cards li {
  border: 1px solid var(--line); border-radius: 8px; padding: 14px 16px;
  background: #fff; max-width: none;
}
.cards a { font-weight: 700; text-decoration: none; font-family: Verdana, sans-serif; font-size: 14px; }
.cards p { margin: 6px 0 0; font-size: 14px; color: var(--muted); }
footer {
  text-align: center; color: var(--muted); font-size: 12.5px;
  font-family: Verdana, sans-serif; padding: 18px 24px 28px;
}
@media (max-width: 760px) {
  .layout { flex-direction: column; }
  nav.sidebar { width: auto; }
}
"""


def inline(md: str) -> str:
    """Render inline markdown (code, bold, italic, links) to HTML."""
    s = html.escape(md, quote=False)
    s = re.sub(r"`([^`]+)`", r"<code>\1</code>", s)
    s = re.sub(r"\[([^\]]+)\]\(([^)\s]+)\)",
               lambda m: '<a href="%s">%s</a>' % (m.group(2), m.group(1)), s)
    s = re.sub(r"\*\*(.+?)\*\*", r"<strong>\1</strong>", s)
    s = re.sub(r"(?<![\w*])\*([^*\n]+)\*(?![\w*])", r"<em>\1</em>", s)
    return s


def _link(text: str) -> str:
    """Convert relative .md link targets (with optional #anchors) to .html."""
    return re.sub(r'(?<=href=")([\w./-]+\.md)(#[A-Za-z0-9\-]+)?(?=")',
                  lambda m: m.group(1)[:-3] + ".html" + (m.group(2) or ""), text)


def _collect_list(lines: list[str], i: int, marker: str,
                  strip_marker: bool = False) -> tuple[int, list[str]]:
    """Gather list items, folding wrapped continuation lines into each item.

    Continuation logic: after a marker line, any following non-blank line that
    does not itself open a new block (marker, heading, table, code, quote)
    continues the current item. A blank line ends the list.
    """
    block_openers = re.compile(
        r"^(#{1,4}\s|\s*[-*]\s|\s*\d+[.)]\s|>|\||```|-{3,}|\*{3,})")
    items: list[str] = []
    text = None
    while i < len(lines):
        line = lines[i]
        if re.match(marker, line):
            if text is not None:
                items.append(text)
            if strip_marker:
                text = re.sub(marker, "", line.strip())
            else:
                text = line.strip()[2:]
        elif not line.strip():
            break
        elif text is not None and not block_openers.match(line.strip()):
            text += " " + line.strip()
        else:
            break
        i += 1
    if text is not None:
        items.append(text)
    return i, items


def md_to_html(md: str) -> str:
    """Convert a constrained subset of markdown to HTML."""
    lines = md.split("\n")
    out: list[str] = []
    i = 0
    while i < len(lines):
        line = lines[i]
        stripped = line.strip()

        if not stripped:
            i += 1
            continue

        if stripped.startswith("```"):
            lang = stripped[3:].strip()
            body: list[str] = []
            i += 1
            while i < len(lines) and not lines[i].strip().startswith("```"):
                body.append(lines[i])
                i += 1
            i += 1  # closing fence
            cls = ' class="language-%s"' % lang if lang else ""
            out.append("<pre><code%s>%s</code></pre>" % (cls, html.escape("\n".join(body))))
            continue

        m = re.match(r"^(#{1,4})\s+(.*?)\s*#*\s*$", line)
        if m:
            level = len(m.group(1))
            raw = m.group(2)
            slug = re.sub(r"[^\w\s-]", "", raw.lower()).strip() \
                .replace(" ", "-")
            out.append('<h%d id="%s">%s</h%d>'
                       % (level, html.escape(slug, quote=True), inline(raw), level))
            i += 1
            continue

        if re.match(r"^-{3,}$", stripped) or re.match(r"^\*{3,}$", stripped):
            out.append("<hr>")
            i += 1
            continue

        if stripped.startswith("|"):
            rows: list[list[str]] = []
            while i < len(lines) and lines[i].strip().startswith("|"):
                cells = [c.strip() for c in lines[i].strip().strip("|").split("|")]
                if not all(re.fullmatch(r":?-{2,}:?", c) for c in cells if c):
                    rows.append(cells)
                i += 1
            if rows:
                head, *body_rows = rows
                t = ["<table>", "<thead><tr>"]
                t += ["<th>%s</th>" % inline(c) for c in head]
                t.append("</tr></thead>")
                if body_rows:
                    t.append("<tbody>")
                    for r in body_rows:
                        t.append("<tr>" + "".join("<td>%s</td>" % inline(c) for c in r) + "</tr>")
                    t.append("</tbody>")
                t.append("</table>")
                out.append("\n".join(t))
            continue

        if stripped.startswith(">"):
            body = []
            while i < len(lines) and lines[i].strip().startswith(">"):
                body.append(lines[i].strip().lstrip(">").strip())
                i += 1
            content = "\n".join(body)
            # blockquotes may contain lists; treat indented "- " lines as list items
            paras: list[str] = []
            buf: list[str] = []
            for bl in content.split("\n"):
                if re.match(r"^\s*-\s+", bl):
                    if buf:
                        paras.append("<p>%s</p>" % inline(" ".join(buf)))
                        buf = []
                    paras.append("<li>%s</li>" % inline(re.sub(r"^\s*-\s+", "", bl)))
                else:
                    buf.append(bl)
            if buf:
                paras.append("<p>%s</p>" % inline(" ".join(buf)))
            items = "".join(paras)
            if paras and paras[0].startswith("<li>"):
                items = "<ul>" + items + "</ul>"
            out.append("<blockquote>%s</blockquote>" % items)
            continue

        if re.match(r"^\s*[-*]\s+", line):
            marker = r"^\s*[-*]\s+"
            i, items = _collect_list(lines, i, marker)
            rendered = []
            for text in items:
                text = re.sub(r"^\[ \]\s*", "&#9744; ", text)
                text = re.sub(r"^\[[ xX]\]\s*", "&#9745; ", text)
                rendered.append("<li>%s</li>" % inline(text))
            out.append("<ul>" + "".join(rendered) + "</ul>")
            continue

        if re.match(r"^\s*\d+[.)]\s+", line):
            marker = r"^\s*\d+[.)]\s+"
            i, items = _collect_list(lines, i, marker, strip_marker=True)
            out.append("<ol>" + "".join("<li>%s</li>" % inline(t) for t in items) + "</ol>")
            continue

        para: list[str] = []
        while (i < len(lines) and lines[i].strip()
               and not re.match(r"^(#{1,4}\s|\s*[-*]\s|\s*\d+[.)]\s|>|\||```|-{3,}|\*{3,})", lines[i])):
            para.append(lines[i].strip())
            i += 1
        out.append("<p>%s</p>" % inline(" ".join(para)))

    return _link("\n".join(out))


def page(slug: str = None) -> str:
    """Render the full-site template for one page slug (or the index)."""
    nav = []
    nav.append('<a href="index.html" %s>Home</a>' % ('class="active"' if slug is None else ""))
    nav += [
        '<a href="%s"%s>%s</a>' % (s + ".html", ' class="active"' if s == slug else "", t)
        for s, t, _ in PAGES
    ]
    phi = "\n".join(
        "<li><b>%s</b> — %s</li>" % (b, d) for b, d in PHI_SIDEBAR)
    banner = '<div class="banner">%s</div>' % html.escape(BANNER, quote=False)
    phi_block = (
        '<div class="phisidebar"><h2>Do not include PHI</h2>'
        '<p style="margin:0 0 8px">Before any content goes into a portfolio file, note, or AI prompt:</p>'
        "<ul>%s</ul>"
        '<p style="margin:8px 0 0">Full rules: <a href="01-phi-safety.html">PHI Safety</a>.</p>'
        "</div>" % phi)
    return f"""<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>{TITLE}</title>
<style>
{STYLE}
</style>
</head>
<body>
<header class="site">
<h1>{TITLE}</h1>
<p>{TAGLINE} By Asdale Dynamics, LLC.</p>
</header>
<div class="layout">
<nav class="sidebar"><h2>Manual</h2>{"".join(nav)}</nav>
<main>{banner}{phi_block}{{CONTENT}}
</main>
</div>
<footer>
© 2026 Asdale Dynamics, LLC · Educational content, never medical advice ·
CC0-style docs; site and code MIT licensed ·
Built locally; no tracking, no network.
</footer>
</body>
</html>
"""


def render_docs() -> dict[str, str]:
    """Return {slug: rendered body HTML} for every doc page."""
    pages = {}
    for slug, _title, _desc in PAGES:
        src = DOCS / (slug + ".md")
        pages[slug] = md_to_html(src.read_text(encoding="utf-8"))
    return pages


def render_index() -> str:
    cards = "\n".join(
        "<li><a href=\"%s.html\">%s</a><p>%s</p></li>" % (s, t, html.escape(d, quote=False))
        for s, t, d in PAGES)
    intro = md_to_html((DOCS / "00-read-me-first.md").read_text(encoding="utf-8"))
    three_rules = (
        '<section>'
        "<h2>The three rules of this manual</h2>"
        "<ol>"
        "<li><strong>Never put PHI in your portfolio, notes, or AI prompts.</strong> "
        'See <a href="01-phi-safety.html">PHI Safety</a>.</li>'
        "<li><strong>Your portfolio describes you, not a patient.</strong> "
        "If it reads oddly out loud in a hallway, rewrite it.</li>"
        "<li><strong>AI drafts, you verify.</strong> Certificates, check-off "
        "sheets, and your state board are the sources of truth.</li>"
        "</ol>"
        "<h2>Chapters</h2>"
        '<ul class="cards">'
        + cards
        + "</ul></section>")
    top = "<h1>Professional Portfolio With AI Help</h1>"
    return page(None).replace("{CONTENT}", top + three_rules + "\n<section><h2>Start here</h2>" +
                              rows_of(intro) + "</section>")


def rows_of(intro_html: str) -> str:
    """Take the 'What this manual helps you build' table from the intro."""
    m = re.search(r"(<table>.*?</table>)", intro_html, flags=re.S)
    return m.group(1) if m else ""


def render_page(slug: str, body: str) -> str:
    return page(slug).replace("{CONTENT}", body)


def build(out_dir: Path) -> None:
    out_dir.mkdir(parents=True, exist_ok=True)
    (out_dir / "style.css").write_text(STYLE, encoding="utf-8")
    (out_dir / "index.html").write_text(render_index(), encoding="utf-8")
    for slug, _t, _d in PAGES:
        rendered = render_page(slug, render_docs()[slug])
        (out_dir / (slug + ".html")).write_text(rendered, encoding="utf-8")
    print("Built %s with index + %d pages" % (out_dir, len(PAGES)))


def main() -> None:
    ap = argparse.ArgumentParser(description=__doc__)
    ap.add_argument("--out", default="site", help="output directory (default: site)")
    args = ap.parse_args()
    build(ROOT / args.out)


if __name__ == "__main__":
    main()
