#!/usr/bin/env python3
"""
Leland Internal Skills Audit - reusable PDF report generator.

Renders a branded HTML/CSS template to PDF via WeasyPrint. Fully data-driven:
pass an audit-data JSON object and it produces the report. The audit pipeline
(built later) only has to emit JSON in the schema documented in
audit_data.schema.md - it never touches layout or branding.

Usage:
    python generate_audit_report.py --data audit_data.json --out report.pdf
    python generate_audit_report.py            # uses bundled sample data

Branding tokens come from the Leland 2026 design kit (kit.json). Fonts
(Macan, SeasonMix) are embedded from ./assets/fonts. Brand colors, type, and
spacing all live in TOKENS / CSS below so the look is locked in one place.
"""

import argparse
import html
import json
import os
import re

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
ASSETS = os.path.join(BASE_DIR, "assets")

# ---------------------------------------------------------------------------
# Design tokens (Leland 2026 refresh - kit.json + locked audit spec)
# ---------------------------------------------------------------------------
TOKENS = {
    "tan": "#EBD4B5",
    "cream": "#F3F1E6",
    "forest": "#1F5340",
    "forest_dark": "#163C2E",
    "yellow": "#FFD96F",
    "rust": "#B85A2B",
    "white": "#FFFFFF",
    "ink": "#222222",
    "ink_soft": "#4C4C4C",
    "light_bg": "#F5F5F2",
    "hairline": "#E2DACE",
    "add_bg": "#EAFCE4",
    "add_fg": "#1A5830",
    "add_line": "#BFE6AE",
    "del_bg": "#FEE2E2",
    "del_fg": "#7F1D1D",
    "del_line": "#F2B9B9",
}

STATUS = {
    "no_issues":    {"label": "Reviewed — No Issues",  "bg": "#E8F1EC", "fg": "#1F5340", "dot": "#1F5340"},
    "updated":      {"label": "Reviewed & Updated",         "bg": "#FBEFE3", "fg": "#9A4A1E", "dot": "#B85A2B"},
    "needs_action": {"label": "Requires Human Action",      "bg": "#FCE7E7", "fg": "#9B2226", "dot": "#B23B3B"},
}

VERDICT = {
    "pass": {"label": "Pass",   "fg": "#1F5340", "dot": "#1F5340"},
    "warn": {"label": "Review", "fg": "#9A4A1E", "dot": "#B85A2B"},
    "fail": {"label": "Fail",   "fg": "#9B2226", "dot": "#B23B3B"},
    "unverified": {"label": "Unverified", "fg": "#8A6D1F", "dot": "#C99A2E"},
    "na":   {"label": "n/a",    "fg": "#4C4C4C", "dot": "#869AA6"},
}


def esc(text):
    return html.escape(str(text), quote=True)


def inline_diff(text):
    """Convert inline diff markers to highlighted spans (escaped first).

    {+added+}   -> green character-level highlight
    {-deleted-} -> red character-level highlight (struck through)
    """
    out = esc(text)
    out = re.sub(r"\{\+(.+?)\+\}", r'<span class="ins">\1</span>', out)
    out = re.sub(r"\{-(.+?)-\}", r'<span class="rem">\1</span>', out)
    return out


def quality_color(score):
    if score >= 90:
        return TOKENS["forest"]
    if score >= 75:
        return TOKENS["rust"]
    return "#B23B3B"


# ---------------------------------------------------------------------------
# Section renderers
# ---------------------------------------------------------------------------
def render_cover(meta):
    issues = meta.get("critical_issues", 0)
    return f"""
<section class="cover">
  <div class="cover-top">
    <div class="brand">
      <img class="logomark" src="assets/LogomarkYellow.png" alt="Leland logomark"/>
      <span class="wordmark">{esc(meta.get('org','Leland'))}</span>
    </div>
    <div class="cover-kicker">Internal Audit · Confidential</div>
  </div>
  <div class="cover-band">
    <div class="cover-band-inner">
      <div class="cover-eyebrow">{esc(meta.get('portfolio','Skills Portfolio Audit'))}</div>
      <h1 class="cover-title">{esc(meta.get('title','SKILLS AUDIT REPORT'))}</h1>
      <div class="cover-subtitle">{esc(meta.get('subtitle',''))}</div>
    </div>
  </div>
  <div class="cover-bottom">
    <div class="cover-date">Audit Date — {esc(meta.get('date',''))}</div>
    <div class="stat-row">
      <div class="stat">
        <div class="stat-num">{esc(meta.get('skills_audited','—'))}</div>
        <div class="stat-label">Skills Audited</div>
      </div>
      <div class="stat">
        <div class="stat-num">{esc(meta.get('avg_quality','—'))}<span class="stat-unit">/100</span></div>
        <div class="stat-label">Average Quality</div>
      </div>
      <div class="stat">
        <div class="stat-num">{esc(issues)}</div>
        <div class="stat-label">Critical Issues</div>
      </div>
    </div>
  </div>
</section>
"""


def render_exec(es):
    cards = ""
    for c in es.get("metrics", []):
        cards += f"""
      <div class="metric-card">
        <div class="metric-value">{esc(c.get('value',''))}</div>
        <div class="metric-label">{esc(c.get('label',''))}</div>
      </div>"""
    paras = "".join(f"<p>{esc(p)}</p>" for p in es.get("overview", []))
    closing = f'<p class="note">{esc(es.get("closing"))}</p>' if es.get("closing") else ""
    return f"""
<section class="page">
  <h1 class="section-title">Executive Summary</h1>
  {paras}
  <h3 class="sub-title">Key Results</h3>
  <div class="metric-grid">{cards}</div>
  {closing}
</section>
"""


def render_methodology(m):
    items = ""
    for c in m.get("criteria", []):
        items += f"""
    <div class="criterion">
      <div class="criterion-num">{esc(c.get('num',''))}</div>
      <div class="criterion-body">
        <div class="criterion-name">{esc(c.get('name',''))}</div>
        <div class="criterion-desc">{esc(c.get('description',''))}</div>
        <div class="criterion-verify"><span class="verify-label">Verification</span> {esc(c.get('verification',''))}</div>
      </div>
    </div>"""
    return f"""
<section class="page">
  <h1 class="section-title">Audit Methodology &amp; Criteria</h1>
  <p>{esc(m.get('intro',''))}</p>
  <div class="criteria-list">{items}</div>
</section>
"""


def render_results(r):
    rows = ""
    for s in r.get("status_breakdown", []):
        st = STATUS.get(s.get("status"), {"label": s.get("label", ""), "dot": TOKENS["forest"]})
        rows += f"""
      <tr>
        <td class="rs-status"><span class="dot" style="background:{st['dot']}"></span>{esc(s.get('label', st['label']))}</td>
        <td class="rs-count">{esc(s.get('count',''))}</td>
        <td class="rs-desc">{esc(s.get('description',''))}</td>
      </tr>"""
    notes = f'<p class="note">{esc(r.get("notes"))}</p>' if r.get("notes") else ""
    return f"""
<section class="page">
  <h1 class="section-title">Results Summary</h1>
  <p>{esc(r.get('intro',''))}</p>
  <table class="results-table">
    <thead><tr><th>Status</th><th>Count</th><th>Meaning</th></tr></thead>
    <tbody>{rows}</tbody>
  </table>
  {notes}
</section>
"""


def render_swot(swot):
    quads = [
        ("Strengths", "s", swot.get("strengths", [])),
        ("Weaknesses", "w", swot.get("weaknesses", [])),
        ("Opportunities", "o", swot.get("opportunities", [])),
        ("Threats", "t", swot.get("threats", [])),
    ]

    def cell(title, cls, items):
        lis = "".join(f"<li>{esc(i)}</li>" for i in items) or "<li class='empty'>None noted</li>"
        return (f'<div class="swot-cell swot-{cls}">'
                f'<div class="swot-head">{title}</div><ul>{lis}</ul></div>')

    s = cell(*quads[0])
    w = cell(*quads[1])
    o = cell(*quads[2])
    th = cell(*quads[3])
    return (f'<table class="swot-table"><tbody>'
            f'<tr><td>{s}</td><td>{w}</td></tr>'
            f'<tr><td>{o}</td><td>{th}</td></tr>'
            f'</tbody></table>')


def render_diff(diff):
    lines = ""
    for ln in diff:
        t = ln.get("type", "context")
        code = inline_diff(ln.get("text", ""))
        if t == "add":
            lines += f'<div class="dline add"><span class="gutter">+</span><span class="code">{code}</span></div>'
        elif t == "del":
            lines += f'<div class="dline del"><span class="gutter">−</span><span class="code">{code}</span></div>'
        elif t == "inline":
            lines += f'<div class="dline ins-line"><span class="gutter">~</span><span class="code">{code}</span></div>'
        else:
            lines += f'<div class="dline ctx"><span class="gutter"></span><span class="code">{code}</span></div>'
    return f'<div class="diff">{lines}</div>'


def render_changes(changes):
    if not changes:
        return '<div class="no-change">No code changes were required.</div>'
    blocks = ""
    for ch in changes:
        loc = f'<span class="change-loc">{esc(ch.get("location"))}</span>' if ch.get("location") else ""
        desc = f'<div class="change-desc">{esc(ch.get("description"))}</div>' if ch.get("description") else ""
        blocks += f"""
    <div class="change">
      <div class="change-title">{esc(ch.get('title',''))} {loc}</div>
      {desc}
      {render_diff(ch.get('diff', []))}
    </div>"""
    return blocks


def render_action(sk):
    status = sk.get("status")
    rec = esc(sk.get("recommended_action", "")) if sk.get("recommended_action") else ""
    if status == "needs_action":
        body = rec or "Human review required — see the weaknesses and change applied above, then decide and apply."
        return f"""<h4 class="block-head">Required Action</h4>
  <div class="action action-required">
    <span class="action-tag">Action needed</span>
    <div class="action-text">{body}</div>
  </div>"""
    if status == "updated":
        body = rec or "Confirm the applied change above, then promote the skill to production."
        return f"""<h4 class="block-head">Required Action</h4>
  <div class="action action-confirm">
    <span class="action-tag">Confirm &amp; promote</span>
    <div class="action-text">{body}</div>
  </div>"""
    body = rec or "No action required — reviewed and cleared for production use."
    return f"""<h4 class="block-head">Required Action</h4>
  <div class="action action-none"><span class="action-dot"></span>{body}</div>"""


def render_skill(sk, group_label=""):
    st = STATUS.get(sk.get("status"), STATUS["no_issues"])
    score = sk.get("quality_score", 0)
    qcolor = quality_color(score)
    chips = ""
    for cr in sk.get("criteria_results", []):
        v = VERDICT.get(cr.get("verdict", "na"), VERDICT["na"])
        chips += (f'<span class="chip"><span class="dot" style="background:{v["dot"]}"></span>'
                  f'{esc(cr.get("name",""))}<span class="chip-v" style="color:{v["fg"]}">{v["label"]}</span></span>')
    chips_block = f'<div class="chip-row">{chips}</div>' if chips else ""
    summary = f'<p class="skill-summary">{esc(sk.get("summary"))}</p>' if sk.get("summary") else ""
    width = max(0, min(100, int(score)))
    _ch = sk.get('changes', [])
    _changes_html = ('<h4 class="block-head">Change Applied</h4>' + render_changes(_ch)) if _ch else ''
    return f"""
<section class="page skill">
  {f'<div class="skill-eyebrow">{esc(group_label)} Skills</div>' if group_label else ''}
  <h2 class="skill-title">Skill Evaluation — {esc(sk.get('name',''))}</h2>
  <div class="skill-head">
    <span class="badge" style="background:{st['bg']};color:{st['fg']}"><span class="dot" style="background:{st['dot']}"></span>{st['label']}</span>
    <span class="class-tag">{esc(sk.get('classification',''))}</span>
    <div class="score">
      <div class="score-num" style="color:{qcolor}">{esc(score)}<span class="score-unit">/100</span></div>
      <div class="score-bar"><span style="width:{width}%;background:{qcolor}"></span></div>
      <div class="score-label">Quality Score</div>
    </div>
  </div>
  {summary}
  {chips_block}
  <h4 class="block-head">SWOT Analysis</h4>
  {render_swot(sk.get('swot', {}))}
  {_changes_html}
  {render_action(sk)}
</section>
"""


def render_group_divider(g):
    skills = g.get("skills", [])
    n = len(skills)
    na = sum(1 for s in skills if s.get("status") == "needs_action")
    up = sum(1 for s in skills if s.get("status") == "updated")
    ok = n - na - up
    avg = round(sum(s.get("quality_score", 0) for s in skills) / n) if n else 0
    desc = f'<p class="group-desc">{esc(g.get("description"))}</p>' if g.get("description") else ""
    return f"""
<section class="page group-divider">
  <div class="group-kicker">Skill Group</div>
  <h1 class="group-name">{esc(g.get('name',''))}</h1>
  {desc}
  <div class="group-stats">
    <div class="gstat"><div class="gstat-num">{n}</div><div class="gstat-label">Skills</div></div>
    <div class="gstat"><div class="gstat-num">{avg}<span>/100</span></div><div class="gstat-label">Avg Quality</div></div>
    <div class="gstat"><div class="gstat-num">{ok}</div><div class="gstat-label">No Issues</div></div>
    <div class="gstat"><div class="gstat-num">{up}</div><div class="gstat-label">Updated</div></div>
    <div class="gstat"><div class="gstat-num">{na}</div><div class="gstat-label">Need Action</div></div>
  </div>
</section>
"""


# ---------------------------------------------------------------------------
# CSS
# ---------------------------------------------------------------------------
def build_css():
    t = TOKENS
    return f"""
@font-face {{ font-family:'Macan'; src:url('assets/fonts/Macan-Regular.woff2') format('woff2'); font-weight:400; font-style:normal; }}
@font-face {{ font-family:'Macan'; src:url('assets/fonts/Macan-Medium.woff2') format('woff2'); font-weight:500; font-style:normal; }}
@font-face {{ font-family:'Macan'; src:url('assets/fonts/Macan-SemiBold.woff2') format('woff2'); font-weight:600; font-style:normal; }}
@font-face {{ font-family:'SeasonMix'; src:url('assets/fonts/SeasonMix-Medium.woff2') format('woff2'); font-weight:500; font-style:normal; }}

@page {{
  size: Letter;
  margin: 20mm 20mm 18mm 20mm;
  @bottom-left {{ content: "Leland · Skills Portfolio Audit · Confidential"; font-family:'Macan',sans-serif; font-size:7.5pt; color:{t['ink_soft']}; }}
  @bottom-right {{ content: counter(page); font-family:'Macan',sans-serif; font-size:7.5pt; color:{t['ink_soft']}; }}
}}
@page cover {{ margin: 0; @bottom-left {{ content:none; }} @bottom-right {{ content:none; }} }}
@page divider {{ margin: 0; @bottom-left {{ content:none; }} @bottom-right {{ content:none; }} }}

* {{ box-sizing: border-box; }}
html {{ -weasy-hyphens: none; }}
body {{ margin:0; font-family:'Macan',sans-serif; color:{t['ink']}; font-size:10.5pt; line-height:1.6; }}
p {{ margin:0 0 10pt 0; max-width: 165mm; }}
.note {{ color:{t['ink_soft']}; font-size:9.5pt; }}

/* ---------- Cover ---------- */
.cover {{ page: cover; height: 279.4mm; display:flex; flex-direction:column; }}
.cover-top {{ background:{t['tan']}; color:{t['ink']}; padding:16mm 18mm 0 18mm; flex:0 0 auto; height:64mm;
  display:flex; justify-content:space-between; align-items:flex-start; }}
.brand {{ display:flex; align-items:center; gap:10pt; }}
.logomark {{ width:42pt; height:42pt; border-radius:6pt; }}
.wordmark {{ font-family:'Macan',sans-serif; font-weight:600; font-size:20pt; letter-spacing:1pt; }}
.cover-kicker {{ font-size:8.5pt; font-weight:500; letter-spacing:1.5pt; text-transform:uppercase; color:{t['forest']}; margin-top:6pt; }}
.cover-band {{ background:{t['forest']}; color:{t['white']}; flex:1 1 auto; display:flex; align-items:center; padding:0 18mm; }}
.cover-eyebrow {{ font-family:'Macan',sans-serif; font-weight:500; font-size:11pt; letter-spacing:2pt; text-transform:uppercase; color:{t['yellow']}; margin-bottom:8pt; }}
.cover-title {{ font-family:'SeasonMix',serif; font-weight:500; font-size:52pt; line-height:1.02; margin:0; }}
.cover-subtitle {{ font-family:'Macan',sans-serif; font-weight:400; font-size:13pt; color:#E7EFE9; margin-top:14pt; max-width:150mm; }}
.cover-bottom {{ background:{t['tan']}; color:{t['ink']}; height:78mm; padding:14mm 18mm; flex:0 0 auto;
  display:flex; flex-direction:column; justify-content:center; }}
.cover-date {{ font-weight:500; font-size:11pt; letter-spacing:.5pt; margin-bottom:10mm; }}
.stat-row {{ display:flex; gap:10mm; }}
.stat-num {{ font-family:'SeasonMix',serif; font-weight:500; font-size:34pt; line-height:1; color:{t['forest']}; }}
.stat-unit {{ font-size:16pt; color:{t['ink_soft']}; }}
.stat-label {{ font-size:9pt; font-weight:500; letter-spacing:1pt; text-transform:uppercase; color:{t['ink_soft']}; margin-top:4pt; }}

/* ---------- Generic section ---------- */
.page {{ page-break-before: always; }}
.section-title {{ font-family:'SeasonMix',serif; font-weight:500; font-size:30pt; color:{t['ink']};
  margin:0 0 4pt 0; padding-bottom:7pt; border-bottom:2.5pt solid {t['forest']}; }}
.sub-title {{ font-family:'Macan',sans-serif; font-weight:600; font-size:13pt; color:{t['ink']}; margin:18pt 0 8pt 0; }}
.block-head {{ font-family:'Macan',sans-serif; font-weight:600; font-size:11pt; letter-spacing:.5pt; text-transform:uppercase;
  color:{t['forest']}; margin:12pt 0 7pt 0; padding-bottom:3pt; border-bottom:1pt solid {t['hairline']}; }}

/* ---------- Exec metrics ---------- */
.metric-grid {{ display:flex; flex-wrap:wrap; gap:8pt; margin-top:4pt; }}
.metric-card {{ flex:1 1 30%; min-width:46mm; background:{t['light_bg']}; border:1pt solid {t['hairline']};
  border-left:3pt solid {t['forest']}; border-radius:6pt; padding:11pt 13pt; }}
.metric-value {{ font-family:'SeasonMix',serif; font-weight:500; font-size:22pt; color:{t['forest']}; line-height:1; }}
.metric-label {{ font-size:9pt; color:{t['ink_soft']}; margin-top:5pt; line-height:1.35; }}

/* ---------- Methodology ---------- */
.criteria-list {{ margin-top:10pt; }}
.criterion {{ display:flex; gap:12pt; padding:11pt 0; border-bottom:1pt solid {t['hairline']}; break-inside:avoid; }}
.criterion:last-child {{ border-bottom:none; }}
.criterion-num {{ flex:0 0 auto; width:24pt; height:24pt; border-radius:50%; background:{t['forest']}; color:{t['white']};
  font-family:'Macan',sans-serif; font-weight:600; font-size:11pt; display:flex; align-items:center; justify-content:center; }}
.criterion-name {{ font-family:'Macan',sans-serif; font-weight:600; font-size:12pt; color:{t['ink']}; margin-bottom:2pt; }}
.criterion-desc {{ font-size:10pt; color:{t['ink']}; margin-bottom:4pt; }}
.criterion-verify {{ font-size:9pt; color:{t['ink_soft']}; }}
.verify-label {{ font-weight:600; color:{t['forest']}; text-transform:uppercase; letter-spacing:.5pt; font-size:8pt; }}

/* ---------- Results table ---------- */
.results-table {{ width:100%; border-collapse:collapse; margin-top:10pt; font-size:10pt; }}
.results-table th {{ background:{t['forest']}; color:{t['white']}; text-align:left; padding:8pt 10pt; font-weight:600; font-size:9.5pt;
  text-transform:uppercase; letter-spacing:.5pt; }}
.results-table td {{ padding:9pt 10pt; border-bottom:1pt solid {t['hairline']}; vertical-align:top; }}
.rs-status {{ font-weight:600; white-space:nowrap; }}
.rs-count {{ font-family:'SeasonMix',serif; font-size:14pt; color:{t['forest']}; }}
.rs-desc {{ color:{t['ink_soft']}; }}
.dot {{ display:inline-block; width:8pt; height:8pt; border-radius:50%; margin-right:6pt; }}

/* ---------- Group divider ---------- */
.group-divider {{ page: divider; height:279.4mm; background:{t['forest']}; color:{t['white']};
  padding:0 24mm; display:flex; flex-direction:column; justify-content:center; }}
.group-kicker {{ font-family:'Macan',sans-serif; font-weight:500; font-size:11pt; letter-spacing:2.5pt; text-transform:uppercase; color:{t['yellow']}; margin-bottom:10pt; }}
.group-name {{ font-family:'SeasonMix',serif; font-weight:500; font-size:50pt; line-height:1.02; margin:0 0 14pt 0; color:{t['white']}; border:none; padding:0; }}
.group-desc {{ font-size:13pt; color:#E7EFE9; max-width:150mm; margin:0 0 22pt 0; }}
.group-stats {{ display:flex; gap:9mm; flex-wrap:wrap; margin-top:6mm; }}
.gstat-num {{ font-family:'SeasonMix',serif; font-weight:500; font-size:30pt; line-height:1; color:{t['yellow']}; }}
.gstat-num span {{ font-size:14pt; color:#CFE0D6; }}
.gstat-label {{ font-size:8pt; font-weight:500; letter-spacing:1pt; text-transform:uppercase; color:#CFE0D6; margin-top:4pt; }}
.skill-eyebrow {{ font-family:'Macan',sans-serif; font-weight:600; font-size:9pt; letter-spacing:1.5pt; text-transform:uppercase; color:{t['forest']}; margin-bottom:3pt; }}

/* ---------- Skill ---------- */
.skill-title {{ font-family:'SeasonMix',serif; font-weight:500; font-size:23pt; color:{t['ink']};
  margin:0 0 4pt 0; padding-bottom:6pt; border-bottom:2.5pt solid {t['forest']}; }}
.skill-head {{ display:flex; align-items:flex-start; gap:10pt; flex-wrap:wrap; margin-top:10pt; }}
.badge {{ display:inline-flex; align-items:center; font-weight:600; font-size:9pt; padding:3pt 8pt; border-radius:5pt; }}
.class-tag {{ font-size:9pt; font-weight:500; color:{t['ink_soft']}; border:1pt solid {t['hairline']}; border-radius:5pt; padding:3pt 8pt; }}
.score {{ margin-left:auto; width:62mm; text-align:right; }}
.score-num {{ font-family:'SeasonMix',serif; font-weight:500; font-size:26pt; line-height:1; }}
.score-unit {{ font-size:13pt; color:{t['ink_soft']}; }}
.score-bar {{ height:6pt; background:{t['light_bg']}; border:1pt solid {t['hairline']}; border-radius:4pt; margin:5pt 0 3pt 0; overflow:hidden; }}
.score-bar span {{ display:block; height:100%; }}
.score-label {{ font-size:8pt; font-weight:500; letter-spacing:1pt; text-transform:uppercase; color:{t['ink_soft']}; }}
.skill-summary {{ margin-top:9pt; font-size:10.5pt; }}
.chip-row {{ display:flex; flex-wrap:wrap; gap:6pt; margin-top:8pt; }}
.chip {{ font-size:8.5pt; background:{t['light_bg']}; border:1pt solid {t['hairline']}; border-radius:14pt; padding:3pt 8pt; }}
.chip-v {{ font-weight:600; margin-left:5pt; }}

/* ---------- SWOT (2x2 via table for reliable layout) ---------- */
.swot-table {{ width:100%; border-collapse:collapse; table-layout:fixed; break-inside:avoid; margin-top:2pt; }}
.swot-table td {{ width:50%; vertical-align:top; padding:0 4pt 8pt 4pt; }}
.swot-table tr td:first-child {{ padding-left:0; }}
.swot-table tr td:last-child {{ padding-right:0; }}
.swot-cell {{ border:1pt solid {t['hairline']}; border-radius:6pt; padding:8pt 10pt; background:{t['white']}; }}
.swot-head {{ font-family:'Macan',sans-serif; font-weight:600; font-size:10pt; text-transform:uppercase; letter-spacing:.5pt; margin-bottom:5pt; }}
.swot-cell ul {{ margin:0; padding-left:14pt; }}
.swot-cell li {{ font-size:9.5pt; margin-bottom:2.5pt; }}
.swot-cell li.empty {{ color:{t['ink_soft']}; list-style:none; margin-left:-14pt; font-style:italic; }}
.swot-s {{ border-left:3pt solid {t['forest']}; }}  .swot-s .swot-head {{ color:{t['forest']}; }}
.swot-w {{ border-left:3pt solid {t['rust']}; }}    .swot-w .swot-head {{ color:{t['rust']}; }}
.swot-o {{ border-left:3pt solid #2E6F8E; }}        .swot-o .swot-head {{ color:#2E6F8E; }}
.swot-t {{ border-left:3pt solid #B23B3B; }}        .swot-t .swot-head {{ color:#B23B3B; }}

/* ---------- Required action ---------- */
.action {{ break-inside:avoid; margin-top:2pt; }}
.action-required {{ background:{t['del_bg']}; border:1pt solid {t['del_line']}; border-left:3pt solid #B23B3B; border-radius:6pt; padding:9pt 12pt; }}
.action-confirm {{ background:{t['light_bg']}; border:1pt solid {t['hairline']}; border-left:3pt solid {t['rust']}; border-radius:6pt; padding:9pt 12pt; }}
.action-tag {{ display:block; font-family:'Macan',sans-serif; font-weight:600; font-size:8pt; letter-spacing:1pt; text-transform:uppercase; color:{t['del_fg']}; margin-bottom:4pt; }}
.action-confirm .action-tag {{ color:#9A4A1E; }}
.action-text {{ font-size:10pt; color:{t['ink']}; line-height:1.5; }}
.action-none {{ font-size:10pt; color:{t['ink_soft']}; font-style:italic; padding:4pt 0; }}
.action-dot {{ display:inline-block; width:7pt; height:7pt; border-radius:50%; background:{t['forest']}; margin-right:6pt; }}

/* ---------- Change / diff ---------- */
.no-change {{ font-size:10pt; color:{t['ink_soft']}; font-style:italic; padding:8pt 0; }}
.change {{ margin-bottom:12pt; break-inside:avoid; }}
.change-title {{ font-family:'Macan',sans-serif; font-weight:600; font-size:10.5pt; margin-bottom:3pt; }}
.change-loc {{ font-family:'SF Mono',Consolas,monospace; font-size:8.5pt; color:{t['ink_soft']}; font-weight:400; margin-left:6pt; }}
.change-desc {{ font-size:9.5pt; color:{t['ink_soft']}; margin-bottom:6pt; }}
.diff {{ border:1pt solid {t['hairline']}; border-radius:6pt; overflow:hidden; font-family:'SF Mono',Consolas,monospace; font-size:8.5pt; line-height:1.5; }}
.dline {{ display:flex; }}
.dline .gutter {{ flex:0 0 auto; width:16pt; text-align:center; color:{t['ink_soft']}; }}
.dline .code {{ flex:1 1 auto; padding-right:8pt; white-space:pre-wrap; word-break:break-word; }}
.dline.ctx {{ background:{t['white']}; color:{t['ink']}; }}
.dline.add {{ background:{t['add_bg']}; color:{t['add_fg']}; }}
.dline.add .gutter {{ color:{t['add_fg']}; }}
.dline.del {{ background:{t['del_bg']}; color:{t['del_fg']}; }}
.dline.del .gutter {{ color:{t['del_fg']}; }}
.dline.ins-line {{ background:{t['white']}; }}
.ins {{ background:{t['add_bg']}; color:{t['add_fg']}; border-radius:2pt; padding:0 1pt; box-shadow:inset 0 -1.5pt 0 {t['add_line']}; }}
.rem {{ background:{t['del_bg']}; color:{t['del_fg']}; border-radius:2pt; padding:0 1pt; text-decoration:line-through; }}
"""


def build_html(data):
    meta = data.get("meta", {})
    css = build_css()
    parts = [render_cover(meta)]
    if data.get("executive_summary"):
        parts.append(render_exec(data["executive_summary"]))
    if data.get("methodology"):
        parts.append(render_methodology(data["methodology"]))
    if data.get("results"):
        parts.append(render_results(data["results"]))
    groups = data.get("groups")
    if groups:
        for g in groups:
            parts.append(render_group_divider(g))
            for sk in g.get("skills", []):
                parts.append(render_skill(sk, g.get("name", "")))
    else:
        for sk in data.get("skills", []):
            parts.append(render_skill(sk))
    body = "\n".join(parts)
    return (f'<!doctype html><html lang="en"><head><meta charset="utf-8">'
            f'<title>{esc(meta.get("title","Skills Audit Report"))}</title>'
            f'<style>{css}</style></head><body>{body}</body></html>')


def main():
    ap = argparse.ArgumentParser(description="Generate the Leland Skills Audit PDF report.")
    ap.add_argument("--data", default=os.path.join(BASE_DIR, "audit_data_sample.json"),
                    help="Path to audit-data JSON (defaults to bundled sample).")
    ap.add_argument("--out", default=os.path.join(BASE_DIR, "Leland_Skills_Audit_Report.pdf"),
                    help="Output PDF path.")
    ap.add_argument("--html", default=None, help="Optional: also write the intermediate HTML here.")
    args = ap.parse_args()

    with open(args.data, "r", encoding="utf-8") as f:
        data = json.load(f)

    htmlstr = build_html(data)
    if args.html:
        with open(args.html, "w", encoding="utf-8") as f:
            f.write(htmlstr)

    from weasyprint import HTML
    HTML(string=htmlstr, base_url=BASE_DIR).write_pdf(args.out)
    print(f"Wrote {args.out}")


if __name__ == "__main__":
    main()
