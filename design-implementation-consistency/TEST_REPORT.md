# Validation — v0.1

Date: 2026-10-20

## Structural checks

- Skill frontmatter validation: PASS (`quick_validate.py`).
- Package tests: 4/4 PASS (local references, example import, report JSON and
  counts, expected-report citation lines).
- Local Skills junction created; installed SKILL.md hash matches source.
- Selected credential, email and personal-path patterns: no matches. This is
  a limited pattern scan, not a comprehensive security certification.

## Behavioral evaluation

One fresh-context evaluator applied SKILL.md and its required references to
five source-only requests. The evaluator received no expected reports or test
oracles and reported no access to those files, no network, writes or execution
of the example source. The author compared its answers with acceptance criteria.
This was one session containing five cases, not five isolated model invocations.

| Case | Observed result | Acceptance |
|---|---|---|
| A: supplied example | FAIL; complete source-only coverage. Five mismatches (responsive HIGH; gap/weight/radius/text MEDIUM), five matches. No invented runtime result. | Match |
| B: custom rounded-md resolves to required12px | PASS for declaration scope; difference0px; no unnecessary fix. | Match |
| C: rounded-md with unavailable mapping | UNVERIFIED; numeric actual/difference unknown; asks for applicable utility definition. | Match |
| D: implementation only, one radius declaration | IMPLEMENTATION CONSISTENCY REVIEW; UNVERIFIED, no invented design or internal contradiction. | Match |
| E: confirmed gap mismatch plus unresolved radius | Overall FAIL with partial coverage; retains UNVERIFIED radius rather than discarding either finding. | Match |

Observed acceptance matches: 5/5 for this run. No Skill instruction changes were
needed after evaluation. This does not establish a general accuracy rate or
cross-model reliability. The evaluator could read instructional examples within
the Skill references, but not the answer files or prior conclusions.

## Limits

No actual browser, Figma API, real screenshot, TSX build or runtime interaction
was tested. The example is intentionally source-only and does not require an
application build. Package tests do not measure AI judgment quality.
The entries in tests/cases.md remain reusable evaluation specifications;
the expanded run below records how they were exercised.
No existing Skill was changed and no GitHub push/publication was performed.

## Expanded independent test — 2026-10-20

- Package tests repeated: 4/4 PASS; Skill structure validation: PASS.
- Installed Skill matches source.
- Two fresh-context agents evaluated all 16 scenarios in two batches without
  test answers or prior conclusions. Results matched 16/16 acceptance criteria.
- Correctly handled custom utility definitions, resolved/unresolved rem values,
  CSS overrides, missing specifications, visible versus accessible labels,
  crop limitations, conflicting authority and named-token requirements.
- Required failures remained FAIL even with other unresolved checks; missing
  evidence alone did not become a confirmed mismatch or unconditional PASS.
- No instruction or example-source changes were required or made. This test
  turn only recorded results in this report and the detailed evaluation file.

See [full evaluation](tests/forward-evaluation.md) for the method, observed
decisions and limitations. Cases involving images used descriptions only;
this test does not validate real image-reading or rendered UI measurements.
