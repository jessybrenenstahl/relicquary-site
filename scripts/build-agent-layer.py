#!/usr/bin/env python3
"""Build the agent-readable layer for relicquary.com.

Regenerates, deterministically, from the HTML pages:
  <page>.md twins, relicquary-corpus.md, relicquary-md.zip,
  llms-full.txt (orientation + corpus), relicquary.md (legacy pointer),
  and the data-stamp spans inside the HTML downloads strips.

Stamps are content hashes (sha256, first 8 hex chars) of the generated
Markdown, so re-running on an unchanged tree is a no-op. CI runs this
script and fails on any diff, which keeps the twins honest.

Requires: pandoc.
"""
import hashlib
import html as htmllib
import io
import os
import re
import subprocess
import sys
import zipfile

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
BASE = "https://relicquary.com/"

PAGES = [
    ("index.html", "index.md", "Relicquary: local-first memory OS for AI agents"),
    ("tools.html", "tools.md", "Relicquary tool catalog: 57 MCP tools"),
    ("record.html", "record.md", "The record: what ran, when, at what scope"),
    ("stack.html", "stack.md", "AIM: the full stack that acts, on a verifiable floor"),
    ("touchlink.html", "touchlink.md", "TouchLink: a virtual touchscreen driver"),
    ("support.html", "support.md", "Relicquary support"),
    ("privacy.html", "privacy.md", "Relicquary privacy policy"),
    ("terms.html", "terms.md", "Relicquary terms of service"),
]


def read(p):
    with open(os.path.join(ROOT, p), encoding="utf-8") as fh:
        return fh.read()


def write(p, s):
    with open(os.path.join(ROOT, p), "w", encoding="utf-8") as fh:
        fh.write(s)


def strip_tags(s):
    s = re.sub(r"<br\s*/?>", "\n", s)
    s = re.sub(r"<[^>]+>", "", s)
    return htmllib.unescape(s)


def clean(page_html):
    m = re.search(r"<main\b[^>]*>(.*?)</main>", page_html, re.S)
    s = m.group(1) if m else page_html

    for pat in (r"<svg\b.*?</svg>", r"<script\b.*?</script>",
                r"<style\b.*?</style>", r"<button\b.*?</button>"):
        s = re.sub(pat, " ", s, flags=re.S)

    # command/config blocks: keep only their <pre> (becomes fenced code)
    s = re.sub(r'<div class="cmd-block[^"]*"[^>]*>.*?(<pre>.*?</pre>).*?</div>',
               r"\1", s, flags=re.S)

    # the early-access path terminal: keep its tbody text as a fenced block
    def tbody_to_pre(m2):
        return "<pre>" + strip_tags(m2.group(1)).strip() + "</pre>"
    s = re.sub(r'<div class="cta-term"[^>]*>.*?<div class="tbody">(.*?)</div>\s*</div>',
               tbody_to_pre, s, flags=re.S)

    # governed-tick style wire terminals: each step becomes "k: v"
    def wire_to_pre(m2):
        steps = re.findall(
            r'<span class="k[^"]*">(.*?)</span><span class="v">(.*?)</span>',
            m2.group(1), re.S)
        lines = [strip_tags(k).strip() + ": " + strip_tags(v).strip()
                 for k, v in steps]
        return "<pre>" + "\n".join(lines) + "</pre>"
    s = re.sub(r'<div class="wire">(.*?)</div>\s*</div>', wire_to_pre, s, flags=re.S)

    # decorative / chrome blocks
    for cls in ("hero-glow", "hero-actions", "cta-actions", "hero-meta",
                "eyebrow", "term-body", "term-bar", "tbar"):
        s = re.sub(r'<div class="' + cls + r'"[^>]*>.*?</div>\s*', " ", s, flags=re.S)
    for cls in ("downloads", "for-agent"):
        s = re.sub(r'<section class="' + cls + r'".*?</section>', " ", s, flags=re.S)
    s = re.sub(r'<nav class="jump-row".*?</nav>', " ", s, flags=re.S)
    s = re.sub(r'<div class="jump-row".*?</div>', " ", s, flags=re.S)

    # chip rows join with a separator instead of merging into token soup
    def join_spans(m2):
        parts = [strip_tags(x).strip() for x in
                 re.findall(r"<span[^>]*>(.*?)</span>", m2.group(1), re.S)]
        parts = [p for p in parts if p]
        return "<p>" + htmllib.escape(" · ".join(parts)) + "</p>"
    s = re.sub(r'<div class="kinds"[^>]*>(.*?)</div>', join_spans, s, flags=re.S)

    def join_anchors(m2):
        parts = [strip_tags(x).strip() for x in
                 re.findall(r"<a[^>]*>(.*?)</a>", m2.group(1), re.S)]
        return "<p>" + htmllib.escape(" · ".join(p for p in parts if p)) + "</p>"
    s = re.sub(r'<div class="verb-wall"[^>]*>(.*?)</div>', join_anchors, s, flags=re.S)

    def join_proof(m2):
        parts = [strip_tags(x).strip() for x in
                 re.findall(r'<span class="pf">(.*?)</span>', m2.group(1), re.S)]
        parts = [re.sub(r"\s+", " ", p) for p in parts if p]
        return "<p>" + htmllib.escape(" · ".join(parts)) + "</p>"
    s = re.sub(r'<section class="proof"[^>]*>(.*?)</section>', join_proof, s, flags=re.S)

    # tool cards: fold the verb into the heading
    s = re.sub(r'<div class="cap-num">(.*?)</div>\s*<h3>(.*?)</h3>',
               r"<h3>\1 · \2</h3>", s, flags=re.S)
    return s


def to_md(page, title):
    cleaned = clean(read(page))
    md = subprocess.run(
        ["pandoc", "-f", "html-smart", "-t", "gfm-raw_html", "--wrap=none"],
        input=cleaned, capture_output=True, text=True, check=True).stdout
    md = md.replace(" ", " ")
    md = re.sub(r"\n{3,}", "\n\n", md).strip()
    body = md + "\n"
    h8 = hashlib.sha256(body.encode()).hexdigest()[:8]
    head = ("# " + title + "\n\n*Machine-readable Markdown of " + BASE + page
            + " (content hash " + h8 + ")*\n\n")
    return head + body, h8


PANDOC_WANT = "3.10"


def check_pandoc():
    v = subprocess.run(["pandoc", "--version"], capture_output=True, text=True).stdout.split()[1]
    if not v.startswith(PANDOC_WANT):
        sys.exit("pandoc %s found; this generator is pinned to %s (output is version-sensitive)"
                 % (v, PANDOC_WANT))


def main():
    check_pandoc()
    mds, hashes = {}, {}
    for page, slug, title in PAGES:
        mds[slug], hashes[page] = to_md(page, title)
        write(slug, mds[slug])

    # per-page stamp inside the downloads strip (stripped before conversion,
    # so writing it does not change the twin's content hash)
    for page, slug, _ in PAGES:
        t = read(page)
        t2 = re.sub(r'(<span class="dl-stamp" data-stamp>)[^<]*(</span>)',
                    r"\g<1>" + slug + " · content hash " + hashes[page] + r"\g<2>", t)
        if t2 != t:
            write(page, t2)

    toc = "\n".join("- " + title for _, _, title in PAGES)
    corpus = ("# Relicquary: full site corpus\n\n"
              "*Every content page of relicquary.com as one machine-readable Markdown "
              "document. Relicquary is a local-first memory OS for AI agents with an "
              "MCP-native surface of 57 tools; AIM is a full-stack computer-use "
              "operator built on it, acting on a verifiable floor. RQ MCP LLC.*\n\n"
              "## Contents\n" + toc + "\n\n---\n\n")
    corpus += "\n\n---\n\n".join(mds[slug] for _, slug, _ in PAGES)
    write("relicquary-corpus.md", corpus)

    orientation = read("scripts/llms-orientation.md").rstrip()
    write("llms-full.txt", orientation + "\n\n---\n\n" + corpus.lstrip())

    write("relicquary.md",
          "# Relicquary\n\nLegacy URL. The page lives at " + BASE
          + " and its Markdown twin at " + BASE + "index.md\n")

    zpath = os.path.join(ROOT, "relicquary-md.zip")
    with zipfile.ZipFile(zpath, "w", zipfile.ZIP_DEFLATED) as z:
        for _, slug, _ in PAGES:
            z.writestr(zipfile.ZipInfo(slug), mds[slug])
        z.writestr(zipfile.ZipInfo("relicquary-corpus.md"), corpus)
        z.writestr(zipfile.ZipInfo("llms.txt"), read("llms.txt"))
        z.writestr(zipfile.ZipInfo("llms-full.txt"), read("llms-full.txt"))

    total = sum(len(m) for m in mds.values())
    em = sum(m.count("—") for m in mds.values()) + corpus.count("—")
    print("agent layer built: %d twins, corpus %d chars, %d chars total, em dashes %d"
          % (len(mds), len(corpus), total, em))
    if em:
        sys.exit("em dashes found in generated markdown")


if __name__ == "__main__":
    main()
