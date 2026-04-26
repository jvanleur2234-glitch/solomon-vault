# RD Report: Storefront UI

**URL:** https://github.com/vuestorefront/storefront-ui
**Stars:** ~3.5K (GitHub)
**License:** MIT
**Language:** TypeScript, Vue, React, TailwindCSS

---

## What It Is

Storefront UI is a framework-agnostic UI library and design system built specifically for eCommerce, based on TailwindCSS. It provides:

- **Base components**: Button, Input, Checkbox, Modal — beautiful, accessible (WCAG AA), Lighthouse 95-100 performance
- **eCommerce-specific blocks**: ProductCard, QuantitySelector, checkout step components
- **Composables**: useDropdown and other abstracted UI interactions
- **Tailwind preset**: Maps tailwind config to CSS variables
- **Figma kit**: Pixel-perfect design files for designer/developer alignment
- **Vue + React support**: Framework-agnostic via headless/structural approach

---

## What We'd Use It For

- **Solomon OS v2 UI**: If we rebuild the Hermes dashboard or client-facing UI, Storefront UI could accelerate the eCommerce-themed components
- **Future client storefronts**: If Solomon OS ever expands into agency/client project delivery, SFUI is purpose-built for that
- **Design system reference**: Their Figma-to-code workflow is well-documented and could inform our own design token system

---

## How It Compares to What We Have

- **vs. shadcn/ui + Tailwind**: shadcn is general-purpose, SFUI is eCommerce-specific with ProductCard, checkout blocks out of the box. SFUI is heavier (eCommerceOpinionated) vs. shadcn's flexible atoms.
- **vs. our current UI approach**: We have no formal design system. If we wanted one, SFUI + Tailwind preset is a proven path.
- **Dependency risk**: Vue + React dual-support adds complexity. npm package has moderate release cadence.

---

## Verdict

**🟡 Worthwhile (for specific use cases)**

Not a priority for current Solomon OS scope. The sweet spot is if/when we build client-facing eCommerce dashboards or expand into agency work where storefront-grade UI components matter. The Figma kit + design token approach is worth studying regardless.

**Recommendation:** SKILL — file for future reference. If a client project or v2 spec calls for eCommerce UI, revisit.
