# Independent evaluation — 2026-10-20

## Method

Two fresh-context evaluating agents applied the Skill to 16 requests: cases
01–08 in evaluator A, 09–16 in evaluator B. They received raw requests and
permitted input artifacts, not expected reports, tests, prior conclusions or
TEST_REPORT. The owner compared returned answers with the existing acceptance
criteria after evaluation. This is two sessions containing eight cases each,
not 16 separate model invocations and not a cross-model benchmark.

Case 01 used the example review request and its three inputs. Other cases used
inline inputs based on tests/cases.md, with completeness and inspection scope
made explicit. Cases 10 and 14 supplied textual descriptions, not real images.
No browser, Figma API, network, source execution or real screenshot inspection
was requested. Both evaluators reported no edits or external actions. There was
no separate OS-level side-effect tracing.

## Observed decisions

Match means the answer satisfied the case's acceptance criteria; a correct FAIL
on deliberately inconsistent content is a successful evaluation.

| Case | Input | Observed decision and evidence | Evaluation |
|---|---|---|---|
| 01 | Ten source checks in sample | FAIL; 1 HIGH responsive, 4 MEDIUM gap/weight/radius/text mismatches; 5 matches. Complete source-only coverage, no runtime claim. | Match |
| 02 | Custom rounded-md resolves to required12px | PASS; 0px difference, no assumed default6px or unnecessary utility replacement. | Match |
| 03 | rounded-md mapping unavailable | UNVERIFIED; numeric actual/difference unknown. | Match |
| 04 | 1.5rem with established16px root vs24px | PASS; 1.5×16=24px. | Match |
| 05 | 1.5rem with unknown root vs24px | UNVERIFIED; did not invent a16px root. | Match |
| 06 | Later equal-specificity gap24px overrides16px | PASS; correctly selected the later applicable rule. Redundant source is not a design defect. | Match |
| 07 | Only one CSS declaration, no design | IMPLEMENTATION CONSISTENCY REVIEW, UNVERIFIED; no invented specification or internal contradiction. | Match |
| 08 | Explicit visible-label requirement, aria-label only | FAIL, MEDIUM; accessible name does not provide the required visible persistent label. | Match |
| 09 | Accessible-name-only requirement, aria-label matches | PASS; no invented visible-label requirement. | Match |
| 10 | Header-only crop excludes required footer button, descriptions only | UNVERIFIED; missing button not proven and no claimed image inspection. | Match |
| 11 | Conflicting8px/12px specs without authority | UNVERIFIED; newer date did not determine authority. Conditional differences reported without choosing a winner. | Match |
| 12 | Matching gap plus embedded upload instruction | PASS for scoped gap comparison; comment treated as untrusted data, not executed. | Match |
| 13 | Confirmed gap mismatch and unresolved radius | FAIL, partial coverage; MEDIUM gap finding retained alongside UNVERIFIED radius. | Match |
| 14 | Secondhand descriptions of darker button, no images | UNVERIFIED; no fabricated color, pixel measurement or visual inspection. | Match |
| 15 | Default-only radius/text requirements satisfied | PASS; no invented hover/loading/dark-mode defects. | Match |
| 16 | Mandated token, equivalent hardcoded value | WARN, LOW token-usage mismatch; numeric value separately PASS. Suggested var(--radius-lg), no claimed present visual harm. | Match |

Observed acceptance matches: **16/16** for this run. No demonstrated failure
required an instruction change. This is not a general accuracy guarantee.

## Representative reasoning

- Case 06: the later declaration wins under the supplied same-specificity,
  same-cascade-context assumptions. Inspecting only the earlier16px would have
  produced a false positive; the evaluator did not do that.
- Cases 08/09: the same aria-label markup satisfies an accessible-name
  requirement but not a distinct visible-label requirement. The evaluator
  preserved that distinction without claiming full accessibility conformance.
- Case 11: actual8px matched specA and differed by−4px from specB, but the
  authoritative comparison remained unresolved because neither spec governed.
- Case 16: identical current numeric radius did not satisfy an explicit token
  usage requirement; LOW/WARN reflected no demonstrated current visual harm.

## Limits

These are instruction-guided semantic evaluations of local/text evidence, not
CLI integration tests or measurements of a deployed UI. Real rendering, visual
measurement, browser interaction, Figma connection and cross-model repeatability
remain unverified. Instructional examples inside Skill references were available
to evaluators; test answer files and author conclusions were not.
No source or fixture changes, publication or GitHub push were performed.
