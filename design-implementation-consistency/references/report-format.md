# Report format

Use the user's language. Heading:

- `Design Implementation Consistency Report`, or
- `IMPLEMENTATION CONSISTENCY REVIEW` for implementation-only inputs.

Include overall PASS / WARN / FAIL / UNVERIFIED, mode, scope, source inventory,
coverage, viewports/states, authority and important limitations. For internal
review explicitly include `Design conformity: UNVERIFIED`.

Summarize counts: CRITICAL / HIGH / MEDIUM / LOW findings; UNVERIFIED checks;
passed checks. Separate probable from confirmed mismatches. Deduplicate one
cause across related properties unless different fixes are needed.

For each finding provide:

```text
[MEDIUM] Primary button radius differs
Status: FAIL (confirmed source-declaration mismatch)
Confidence: HIGH
Component: PrimaryButton
Expected: 12px
Actual: 6px in inspected CSS; rendered value not measured
Difference: -6px
Evidence: design-spec.md R6; implementation.css .primary border-radius
Impact: Required component shape is inconsistent.
Recommended fix: Use the project token resolving to 12px, or set 12px if no token exists.
Verify: Reinspect computed border-radius at the specified viewports/states.
```

Use filenames/lines/selectors, design node IDs, screenshot regions or measured
properties as available. Unknown actual/expected values remain unknown. Never
invent a file location to make a recommendation appear actionable.
Sort CRITICAL, HIGH, MEDIUM, LOW, then UNVERIFIED; prioritize usability,
responsiveness, primary interactions, reusable components, then visual details.

For JSON requests use this contract (null for unknown values):

```json
{
  "mode": "implementation_consistency",
  "status": "UNVERIFIED",
  "coverage": "not_verifiable",
  "scope": "Design conformity; implementation supplied without design source",
  "design_conformity": "UNVERIFIED",
  "summary": {"critical": 0, "high": 0, "medium": 0, "low": 0, "unverified": 1, "passed": 0},
  "checks": [
    {
      "id": "RADIUS",
      "status": "UNVERIFIED",
      "classification": "missing_specification",
      "severity": null,
      "confidence": "HIGH",
      "component": "Button",
      "expected": null,
      "actual": "6px declared; rendered value unmeasured",
      "difference": null,
      "evidence": ["supplied CSS: border-radius: 6px"],
      "impact": null,
      "recommended_fix": "Supply the intended radius or design token.",
      "verify": "Compare the resolved design requirement with the implementation."
    }
  ]
}
```

Use `design_to_implementation` when both sources are supplied and
`implementation_consistency` for implementation-only review. The illustrative
scope above concerns only the unresolved design-conformity check.
Classifications: match, confirmed_mismatch, probable_mismatch,
missing_specification, missing_implementation, missing_context.
Counts derive from checks: severity counts include WARN/FAIL findings only;
UNVERIFIED counts have no severity; PASS checks contribute to passed.
