# Severity and status

Severity expresses impact; confidence expresses evidence strength. They are
independent. A tiny radius deviation is not HIGH merely because it is measurable.

| Severity | Impact |
|---|---|
| CRITICAL | Confirmed violation makes a required core interaction unavailable/unusable, with evidence that the full relevant path is affected. |
| HIGH | Prominent or functionally meaningful layout, responsive, hierarchy or variant mismatch. |
| MEDIUM | Visible, meaningful mismatch that does not itself prevent use: typography, radius, spacing or text inconsistency. |
| LOW | Minor, explicitly specified cosmetic deviation with limited effect. |

Assign confidence HIGH for direct applicable evidence, MEDIUM for supported but
conditional interpretation, LOW for hypotheses. Keep hypotheses out of confirmed
defect counts. Missing evidence has severity null, status UNVERIFIED; do not invent
an impact just to fill the field. Optional suggestions are not findings.

## Per-check results

- PASS: explicit expectation is supported by sufficient applicable evidence.
- FAIL: confirmed meaningful mismatch of CRITICAL/HIGH/MEDIUM impact.
- WARN: confirmed LOW-impact mismatch, or an evidence-backed probable mismatch
  labeled as such. A suspicion without a valid expected/actual basis is UNVERIFIED.
- UNVERIFIED: missing/ambiguous expectation, actual value or relevant context.

## Overall result (in order)

1. Any confirmed FAIL -> FAIL, even if other checks cannot be verified.
2. Otherwise any WARN -> WARN; show any unresolved checks separately.
3. Otherwise some checks passed and others are UNVERIFIED -> WARN, partial coverage.
4. Otherwise all applicable checks are UNVERIFIED, or none are inspectable ->
   UNVERIFIED. No audit conclusion is possible.
5. Otherwise all applicable requested checks passed -> PASS within declared scope.

An internal-only implementation review may have its own PASS/WARN/FAIL result,
but must separately state design_conformity=UNVERIFIED. Do not count absence of
external specifications as a confirmed design error.

Report coverage as complete / partial / not_verifiable relative to the agreed
scope. Complete source-declaration coverage does not imply runtime validation.
When the request includes rendered behavior, source-only checks leave that part
UNVERIFIED. State that distinction prominently.
