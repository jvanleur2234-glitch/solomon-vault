# JCPaid × Fusion Design System — FORGED from Runfusion/Fusion

**Date:** 2026-05-01
**Source:** /home/workspace/Fusion/packages/dashboard/app/styles.css (3,291 lines)
**Purpose:** JCPaid client dashboard design tokens + component library

---

## Design Token System

### Spacing Scale
```
--space-xs:   4px    (tight grouping)
--space-sm:   8px    (compact)
--space-md:   12px   (default)
--space-lg:   16px   (comfortable)
--space-xl:   20px   (section gap)
--space-2xl:  24px   (major section)
--space-3xl:  32px   (page padding)
--space-4xl:  48px   (hero spacing)
```

### Border Radius
```
--radius-sm:   4px    (inputs, small)
--radius-md:   8px    (default)
--radius-lg:   12px   (cards, modals)
--radius-xl:   16px   (large)
--radius-pill: 10px   (badges, pills)
```

### Shadows
```
--shadow-sm:   0 1px 2px rgba(0,0,0,0.1)
--shadow-md:   0 4px 6px rgba(0,0,0,0.1)
--shadow-lg:   0 4px 24px rgba(0,0,0,0.4)
--shadow-glow: 0 0 8px rgba(88,166,255,0.3)
```

### Semantic Status Colors
```
--color-success: green
--color-error:   red (light) / red (dark)
--color-warning:  amber
--color-info:    blue
--color-muted:   gray
```

### Task Status Colors
```
--triage, --todo, --in-progress, --in-review, --done, --archived
```

### Typography
```
--font-primary: system font stack
--font-mono:    monospace stack
```

---

## Component Classes

### Buttons
```
.btn              — base
.btn-primary      — CTA
.btn-danger       — destructive
.btn-warning      — warning
.btn-sm           — compact (4px 10px padding)
.btn-icon         — icon-only square
.btn-badge        — notification badge
```

### Cards
```
.card             — base (grab cursor)
.card-header      — flex row
.card-id          — monospace task ID
.card-title       — 13px break-word
.card-meta        — flex row
.card-status-badge— pill shape with status colors
```

### Forms
```
.form-group       — field container
.form-group label — uppercase 12px
.input            — global input
.select           — global select
.checkbox-label   — flex gap
.form-error       — error box
```

### Modals
```
.modal-overlay    — backdrop (.open for visible)
.modal            — 480px wide
.modal-lg         — 640px wide
.modal-header     — flex space-between
.modal-close      — × icon
.modal-actions    — action bar
.modal-actions-left / .modal-actions-right
```

---

## Theme System

- Dark/light modes via `data-theme` attribute
- 54 color themes via `data-color-theme` attribute
- Token categories: **base** (redefined per theme) / **semantic** (dark+light only) / **status** (per theme)
- Backgrounds use `color-mix(in srgb, var(--color) X%, transparent)` not `rgba()`

---

## Mobile Responsive

| Breakpoint | Value |
|------------|-------|
| Mobile | 768px |
| Tablet | 1024px |
| Small | 640px |
| XSmall | 480px |

- Touch targets: 44px minimum (Apple HIG)
- Safe area via `env(safe-area-inset-*)`

---

## Implementation Notes

1. Never hardcode pixel values, colors, or durations — always use `var(--token)`
2. Use `color-mix(in srgb, var(--color) 10%, transparent)` for translucent backgrounds
3. All buttons have `:focus-visible` using `--focus-ring-strong` and `:active` using `transform: scale(0.97)`
4. Cards use status-bg/status-text token pairs

---

## JCPaid Adoption Plan

- [ ] Copy Fusion design tokens to JCPaid dashboard CSS
- [ ] Adopt 54-theme system for client portal
- [ ] Implement card + status-badge pattern for task dispatch
- [ ] Add mobile-first responsive overrides
- [ ] Wire up `color-mix()` for translucent states
- [ ] Adopt `.btn` / `.card` / `.modal` class system

**Source file:** `/home/workspace/Fusion/packages/dashboard/app/styles.css`
