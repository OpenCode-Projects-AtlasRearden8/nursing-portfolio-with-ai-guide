#!/usr/bin/env python3
"""Self-checks for the Professional Portfolio With AI Help project.

Run: python3 tests/run.py

Checks:
  1. Build integrity  — site regenerates cleanly with all expected pages,
                        and a rebuild into a temp dir is byte-identical.
  2. Link resolution  — every relative .md link in docs/ resolves; every
                        internal link in site/*.html resolves.
  3. Render sanity    — no unconverted markdown leftovers in HTML output.
  4. PHI-pattern scan — no MRN-like / SSN-like identifiers in docs or site
                        (except the one documented negative example).
  5. Secret scan      — no API keys, tokens, or private keys anywhere.
  6. Legal/credit     — LICENSE copyright line exact; README credits LLC.
"""

import re
import subprocess
import sys
import tempfile
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
DOCS = ROOT / "docs"
REQUIRED_PAGES = ["index"] + [
    "00-read-me-first", "01-phi-safety", "02-competency-sheets",
    "03-ceu-summaries", "04-preceptor-feedback", "05-credential-tracker",
    "06-annual-review", "07-ai-prompt-library", "08-templates",
]

# The PHI-safety chapter deliberately contains a single *negative example*
# (a badly written fictional note). The scanner skips this exact string there;
# any other MRN-like string, anywhere, fails.
ALLOWED_PHI_EXAMPLE = "MRN 44718"

CHECKS = 0
failures: list[str] = []


def check(name: str, condition: bool, detail: str = "") -> None:
    global CHECKS
    CHECKS += 1
    if condition:
        print("PASS  %s" % name)
    else:
        print("FAIL  %s  %s" % (name, detail))
        failures.append(name)


def test_build() -> Path:
    """Build site/ for real — this is the artifact users will use."""
    proc = subprocess.run([sys.executable, str(ROOT / "build.py")],
                          capture_output=True, text=True)
    check("build.py exits 0", proc.returncode == 0, proc.stderr.strip())
    check("build.py reports page count", "Built" in proc.stdout, proc.stdout)
    site = ROOT / "site"
    missing = [s + ".html" for s in REQUIRED_PAGES
               if not (site / (s + ".html")).exists()]
    check("all %d site pages generated" % len(REQUIRED_PAGES), not missing,
          str(missing))
    check("site/style.css generated", (site / "style.css").exists())

    # Reproducibility: a second build into a temp dir is byte-identical.
    with tempfile.TemporaryDirectory() as tmp:
        proc2 = subprocess.run(
            [sys.executable, str(ROOT / "build.py"), "--out", tmp],
            capture_output=True, text=True)
        same = proc2.returncode == 0 and all(
            (site / p.name).read_bytes() == p.read_bytes()
            for p in Path(tmp).glob("*.html"))
        check("rebuild into temp dir is byte-identical", same)
    return site


def test_doc_links() -> None:
    pattern = re.compile(r"\[[^\]]*\]\(([^)]+)\)")
    for md in sorted(DOCS.glob("*.md")):
        bad = []
        for target in pattern.findall(md.read_text(encoding="utf-8")):
            if target.startswith(("http://", "https://", "#", "mailto:")):
                continue
            if not (md.parent / target.split("#")[0]).exists():
                bad.append(target)
        check("doc links resolve: %s" % md.name, not bad, str(bad))


def test_site_links(site: Path) -> None:
    bad = []
    for page in sorted(site.glob("*.html")):
        for href in re.findall(r'href="([^"]+)"', page.read_text(encoding="utf-8")):
            if href.startswith(("http://", "https://", "#", "mailto:")):
                continue
            if not (page.parent / href.split("#")[0]).exists():
                bad.append("%s -> %s" % (page.name, href))
    check("site internal links resolve", not bad, str(bad))


def test_render_sanity(site: Path) -> None:
    bad = []
    for page in sorted(site.glob("*.html")):
        body = re.sub(r"<pre>.*?</pre>", "", page.read_text(encoding="utf-8"),
                      flags=re.S)
        issues = []
        if "```" in body:
            issues.append("stray fence")
        if re.search(r"\*\*", body):
            issues.append("unrendered bold")
        if re.search(r"<(h\d|li|p)>\*", body):
            issues.append("unrendered emphasis")
        if issues:
            bad.append("%s: %s" % (page.name, issues))
    check("no unconverted markdown in HTML", not bad, str(bad))


def test_phi_patterns(site: Path) -> None:
    patterns = {
        "SSN-like": r"\b\d{3}-\d{2}-\d{4}\b",
        "MRN-like": r"\bMRN[ :#]*\d{4,}\b",
        "DOB-labeled": r"(?i)\b(DOB|date of birth)\s*[:#]?\s*\d",
    }
    targets = (sorted(DOCS.glob("*.md"))
               + sorted((DOCS / "sample-data").glob("*.md"))
               + sorted(site.glob("*.html")))
    found = []
    for f in targets:
        text = f.read_text(encoding="utf-8")
        for name, pattern in patterns.items():
            for m in re.finditer(pattern, text):
                match = m.group(0)
                is_allowed_example = (
                    ALLOWED_PHI_EXAMPLE in match
                    and f.name in ("01-phi-safety.md", "01-phi-safety.html"))
                if not is_allowed_example:
                    found.append("%s: %s %r" % (f.name, name, match))
    check("no PHI-like identifiers in docs or site", not found, str(found))


def test_secrets(site: Path) -> None:
    patterns = {
        "api key (openai-style)": r"\bsk-[A-Za-z0-9]{20,}\b",
        "github token": r"\bgh[pousr]_[A-Za-z0-9]{20,}\b",
        "aws key id": r"\bAKIA[0-9A-Z]{16}\b",
        "private key block": r"-----BEGIN [A-Z ]*PRIVATE KEY-----",
        "password literal": r"(?i)\bpassword\s*=\s*['\"][^'\"]{8,}['\"]",
    }
    sources = (list(ROOT.glob("*.py")) + list(ROOT.glob("*.md"))
               + [ROOT / "LICENSE"]
               + sorted(DOCS.glob("*.md"))
               + sorted((DOCS / "sample-data").glob("*.md"))
               + sorted((ROOT / "tests").glob("*.py"))
               + sorted(site.glob("*.html")))
    found = []
    for f in sources:
        text = f.read_text(encoding="utf-8", errors="replace")
        for name, pattern in patterns.items():
            for m in re.finditer(pattern, text):
                found.append("%s: %s %r" % (f.name, name, m.group(0)[:20]))
    check("no secrets/API keys in repo or site", not found, str(found))


def test_legal_and_credit(site: Path) -> None:
    license_text = (ROOT / "LICENSE").read_text(encoding="utf-8")
    exact_line = "Copyright (c) 2026 Asdale Dynamics, LLC"
    check("LICENSE contains exact copyright line", exact_line in license_text,
          "expected %r" % exact_line)
    check("LICENSE is MIT", license_text.startswith("MIT License"))
    readme = (ROOT / "README.md").read_text(encoding="utf-8")
    check("README credits Asdale Dynamics, LLC", "Asdale Dynamics, LLC" in readme)
    idx = (site / "index.html").read_text(encoding="utf-8")
    check("site footer credits Asdale Dynamics, LLC", "Asdale Dynamics, LLC" in idx)


def main() -> int:
    print("== Professional Portfolio With AI Help — self-checks ==")
    site = test_build()
    test_doc_links()
    test_site_links(site)
    test_render_sanity(site)
    test_phi_patterns(site)
    test_secrets(site)
    test_legal_and_credit(site)
    print("== %d checks run, %d failures ==" % (CHECKS, len(failures)))
    if failures:
        print("FAILED:", ", ".join(failures))
        return 1
    print("All checks passed.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
