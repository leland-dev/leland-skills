# Report Data Schema

Write your audit findings to a JSON file in this shape, then render with
`report/generate_audit_report.py`. See `report/example_audit_data.json` for a
full, valid example.

```jsonc
{
  "meta": {
    "org": "LELAND",                 // wordmark on cover
    "portfolio": "Skills Portfolio Audit",
    "title": "SKILLS AUDIT REPORT",
    "subtitle": "One line under the title.",
    "date": "Month D, YYYY",         // audit date (today)
    "skills_audited": 12,            // total entries
    "avg_quality": 96,               // mean of all quality_score, rounded
    "critical_issues": 0             // count of skills with a Safety/Security/Legal fail
  },
  "executive_summary": {
    "overview": ["paragraph 1", "paragraph 2"],
    "metrics":  [ { "value": "10", "label": "..." } ],   // 1-6 cards
    "closing":  "optional small note (e.g. standards/sources + date used)"
  },
  "methodology": {
    "intro": "Framework + scoring method, and which standards/sources (with date) informed this run.",
    "criteria": [ { "num":"1","name":"Safety","description":"...","verification":"..." } ]  // the 7
  },
  "results": {
    "intro": "...",
    "status_breakdown": [
      { "status":"no_issues",    "label":"Reviewed — No Issues",      "count":10, "description":"..." },
      { "status":"updated",      "label":"Reviewed & Updated",        "count":1,  "description":"..." },
      { "status":"needs_action", "label":"Requires Human Action",     "count":1,  "description":"..." }
    ],
    "notes": "optional"
  },
  "groups": [
    {
      "name": "Leland+",                       // group label (default: folder name)
      "description": "One line describing this group.",
      "skills": [
        {
          "name": "skill-name",
          "status": "no_issues | updated | needs_action",
          "quality_score": 96,
          "classification": "Industry-agnostic | Domain-specific (<area>)",
          "summary": "one-line verdict",
          "criteria_results": [
            {"name":"Safety","verdict":"pass"}, {"name":"Compliance","verdict":"pass"},
            {"name":"Completeness","verdict":"pass"}, {"name":"Usefulness","verdict":"pass"},
            {"name":"Security","verdict":"pass"}, {"name":"Adaptability","verdict":"pass"},
            {"name":"Legal","verdict":"pass"}
          ],
          "swot": { "strengths":["..."], "weaknesses":["..."], "opportunities":["..."], "threats":["..."] },
          "changes": [                         // [] when no change
            {
              "title": "What changed",
              "location": "SKILL.md - section",
              "description": "why",
              "diff": [
                {"type":"ctx","text":"unchanged context"},
                {"type":"del","text":"removed line"},
                {"type":"add","text":"added line"},
                {"type":"inline","text":"char-level {-old-}{+new+} in one line"}
              ]
            }
          ],
          "recommended_action": "One-line action + recommendation (or 'No action required ...')."
        }
      ]
    }
  ]
}
```

## Notes
- Multiple groups are supported (e.g. skills from different repositories); each
  renders its own divider page. Use one group when auditing a single folder.
- `changes` should reflect reality: when the user approved fixes, the diff is the
  *applied* edit and status is `updated`; when declined, it is the *proposed* edit
  and status stays `needs_action`.
- Render: `python report/generate_audit_report.py --data <data.json> --out "<folder>/Skill Audit Report - <date>.pdf"`.
