# Checks and value resolution

## Trace evidence before comparing

Follow the relevant import/component chain, conditional props, CSS specificity,
inheritance, media/container queries and custom properties. Utility class order
in JSX alone does not establish CSS cascade order. Unknown stylesheet scope,
root font size, build configuration or runtime state must stay unresolved.

Resolve rem/em/percent values only with the applicable context. Compare numeric
colors after appropriate normalization, preserving alpha, background and theme.
A token alias may resolve to the same value as another token: distinguish a
visual-value requirement from an explicit requirement to use a named token.
Matching pixels do not prove that the mandated token is used, and different
class names do not prove different pixels.

## Ten MVP categories

| Category | Inspect | Avoid |
|---|---|---|
| Layout | order, flex/grid direction, alignment, container size, positioning | inferring actual visibility or overlap from isolated declarations |
| Spacing | margin/padding/gap and box-sizing context | inventing tolerances or treating units as interchangeable |
| Typography | font family/size/weight/line-height/tracking/alignment | assuming a declared font loaded successfully |
| Color | foreground/background/border/icon/state token resolution | guessing exact hex from a scaled screenshot |
| Border | width/style/color | ignoring transparent borders or theme overrides |
| Radius | corner-specific/resolved radius and required token | assuming rounded-md/rounded-xl numeric defaults |
| Component | presence, variant, location, required children | declaring missing content from incomplete source or a crop |
| Content | headings, controls, placeholders, helper/error text | reporting harmless whitespace unless explicitly specified |
| Responsive | breakpoints, stacking/wrapping/visibility/order/overflow | assuming md is 768px or one viewport proves all widths |
| Accessibility | names/labels/alt/semantics/focus/keyboard/contrast evidence | declaring compliance from a source scan or screenshot |

For responsiveness, use supplied representative widths and relevant boundary
values. Distinguish viewport from container queries. If no breakpoint is supplied,
document implementation behavior without asserting an invented design threshold.
If a breakpoint exists only in unavailable config, mark it UNVERIFIED.

For accessibility, separate deviations from explicit design requirements from
implementation-level concerns. Empty alt is valid for a documented decorative
image; aria-label/aria-labelledby may establish a name without a visible label,
but do not satisfy a separate explicit visible-label requirement. A text input's
placeholder is not evidence that the requested persistent label exists.
Only calculate contrast when foreground, composited background, text size and
applicable target are known. Reference the supplied standard/target or verify an
authoritative standard before making conformance claims. Do not assume absence
of browser default focus merely because no custom focus CSS appears.

## Optional states

When explicitly in scope, compare default, hover, focus, active, selected,
disabled, loading, empty, error and success states; also dark mode, animation,
shadow, opacity, image ratio or stacking context. Verify conditional rendering
and async/state branches before declaring a required state missing.

## Fixes

Recommend the narrowest source change supported by inspected configuration.
For expected radius 12px and observed 6px, suggest the project's matching token
or explicit 12px declaration if no token is established. Do not recommend a
utility that happens to map correctly in some other framework configuration.
Include follow-up verification at the affected viewport/state and neighboring
breakpoints. An audit recommendation is not permission to modify source.
