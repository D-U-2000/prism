# Brand guide

Status: Proposed. Owner: @vothanhdat2000. Updated: 2026-10-28.

## Name and promise

Write **Prism** in prose and accessible labels. The dotless letter in the drawing is a visual construction, not the spelling to use in search, URLs or documentation.

Promise: **Make complex operations understandable, recoverable, and verifiable.**

Product description: **Payment exception investigation with traceable evidence.** This describes the proposed direction, not implemented capabilities. Avoid claims of guaranteed safety, regulatory compliance or superiority to named companies.

## Identity and provenance

The owner supplied an SVG wordmark on 2026-10-28: pale lettering on an obsidian field, with a violet parallelogram replacing the dot of the i. Preserve that concept; do not substitute a generic prism illustration.

The supplied SVG used an invalid SVG namespace and a platform-dependent font stack. The prepared assets correct the namespace, use Arial Bold outlines for stable rendering, and trim excess right-hand space. Font fallback, weight and spacing therefore differ from some renderings of the original. The new light variant and compact accent are derived proposals, not separately approved identities.

Distributed wordmarks contain paths rather than font dependencies. The editable source retains text for future design work; its rendering depends on the installed font. No font files are redistributed. These assets follow the repository license; trademark clearance and exclusive rights have not been established. Apache-2.0 does not grant trademark rights.

## Assets

- [Dark wordmark](../assets/brand/prism-wordmark-dark.svg): primary README and dark-surface use.
- [Light wordmark](../assets/brand/prism-wordmark-light.svg): light-surface use.
- [Compact accent](../assets/brand/prism-mark.svg): favicon-sized proposal, accompanied by Prism context.
- [Editable source](../assets/brand/prism-wordmark-source.svg): text-based working source; publish outlined variants for predictable rendering.
- [Asset preview](../assets/brand/preview.html): open locally to compare surfaces and 16/24/32/64 px accent sizes.

Keep the complete wordmark at least 147 px wide, preserve aspect ratio and retain the built-in clear space. Below that size, use the compact accent with nearby text. Do not stretch, animate the wordmark, add gradients or recolor its components independently. Use `alt="Prism"` when the logo names the product; use empty alt text when adjacent text already supplies the same name.

## Palette and UI intent

Obsidian `#0C0F16` is the dark surface; Cloud `#E2E8F0` is its foreground. Paper `#F8FAFC` is the light surface; Obsidian is its foreground. Violet `#6B4EFF` is the brand accent, not a payment-success indicator.

Use plain English labels for confirmed, unknown, conflicting and resolved evidence. Choose and check semantic UI tokens when the interface is designed; this palette is not an accessibility audit or a complete design system. Never distinguish financial states by color alone. Use tabular figures for amounts and explicit currency labels.

Prefer readable system typography, aligned layouts and progressive disclosure for technical evidence. Motion must explain a transition and respect reduced-motion preferences. No motion is required for the static identity.

## Review and maintenance

Review this identity with the product direction in [the product-direction PR](https://github.com/D-U-2000/prism/pull/12). Verify asset rendering, small sizes and both surfaces after edits. Keep text source and outlines visually aligned; regenerate and inspect the outlined variants after typography changes. Screenshots prove appearance on the inspected renderer only, not trademark availability or user recognition.
