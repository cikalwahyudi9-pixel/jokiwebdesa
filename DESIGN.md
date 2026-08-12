---
name: Onyx Admin Architecture
colors:
  surface: '#0e1511'
  surface-dim: '#0e1511'
  surface-bright: '#343b36'
  surface-container-lowest: '#09100c'
  surface-container-low: '#161d19'
  surface-container: '#1a211d'
  surface-container-high: '#242c27'
  surface-container-highest: '#2f3632'
  on-surface: '#dde4dd'
  on-surface-variant: '#bbcabf'
  inverse-surface: '#dde4dd'
  inverse-on-surface: '#2b322d'
  outline: '#86948a'
  outline-variant: '#3c4a42'
  surface-tint: '#4edea3'
  primary: '#4edea3'
  on-primary: '#003824'
  primary-container: '#10b981'
  on-primary-container: '#00422b'
  inverse-primary: '#006c49'
  secondary: '#adc6ff'
  on-secondary: '#002e6a'
  secondary-container: '#0566d9'
  on-secondary-container: '#e6ecff'
  tertiary: '#c0c1ff'
  on-tertiary: '#1000a9'
  tertiary-container: '#9699ff'
  on-tertiary-container: '#1d17b2'
  error: '#ffb4ab'
  on-error: '#690005'
  error-container: '#93000a'
  on-error-container: '#ffdad6'
  primary-fixed: '#6ffbbe'
  primary-fixed-dim: '#4edea3'
  on-primary-fixed: '#002113'
  on-primary-fixed-variant: '#005236'
  secondary-fixed: '#d8e2ff'
  secondary-fixed-dim: '#adc6ff'
  on-secondary-fixed: '#001a42'
  on-secondary-fixed-variant: '#004395'
  tertiary-fixed: '#e1e0ff'
  tertiary-fixed-dim: '#c0c1ff'
  on-tertiary-fixed: '#07006c'
  on-tertiary-fixed-variant: '#2f2ebe'
  background: '#0e1511'
  on-background: '#dde4dd'
  surface-variant: '#2f3632'
typography:
  display-lg:
    fontFamily: Geist
    fontSize: 36px
    fontWeight: '700'
    lineHeight: 44px
    letterSpacing: -0.02em
  headline-md:
    fontFamily: Geist
    fontSize: 24px
    fontWeight: '600'
    lineHeight: 32px
    letterSpacing: -0.01em
  headline-sm:
    fontFamily: Geist
    fontSize: 20px
    fontWeight: '600'
    lineHeight: 28px
  title-lg:
    fontFamily: Geist
    fontSize: 18px
    fontWeight: '600'
    lineHeight: 24px
  body-md:
    fontFamily: Geist
    fontSize: 16px
    fontWeight: '400'
    lineHeight: 24px
  body-sm:
    fontFamily: Geist
    fontSize: 14px
    fontWeight: '400'
    lineHeight: 20px
  label-md:
    fontFamily: Geist
    fontSize: 12px
    fontWeight: '600'
    lineHeight: 16px
    letterSpacing: 0.05em
  label-sm:
    fontFamily: Geist
    fontSize: 11px
    fontWeight: '500'
    lineHeight: 14px
  headline-md-mobile:
    fontFamily: Geist
    fontSize: 20px
    fontWeight: '600'
    lineHeight: 28px
rounded:
  sm: 0.25rem
  DEFAULT: 0.5rem
  md: 0.75rem
  lg: 1rem
  xl: 1.5rem
  full: 9999px
spacing:
  base: 4px
  xs: 4px
  sm: 8px
  md: 16px
  lg: 24px
  xl: 32px
  gutter: 24px
  margin-mobile: 16px
  margin-desktop: 32px
  container-max: 1440px
---

## Brand & Style

The design system is engineered for high-performance administrative environments where clarity, precision, and a premium feel are paramount. It targets professional operators who require a focused workspace that minimizes cognitive load while providing a sophisticated, "command center" aesthetic.

The visual style is **Modern Corporate with a Dark-Mode focus**, utilizing **Minimalism** to ensure data density doesn't compromise readability. Key characteristics include:
- **Depth through Layering:** Avoiding pure black in favor of deep charcoals to allow for tonal depth and subtle shadowing.
- **Precision Typography:** A focus on legibility and clear hierarchy to distinguish between navigation, headers, and actionable data.
- **Vibrant Intent:** Utilizing saturated accent colors sparingly but purposefully to indicate primary and secondary administrative actions.

## Colors

This design system uses a "Refined Charcoal" palette. The background is never true black (#000), which allows for soft shadows and better perception of depth.

- **Backgrounds:** The foundation is a deep navy-charcoal. Surfaces (cards/modals) use a slightly lighter tint to "lift" them off the base.
- **Accents:** 
    - **Emerald Green (#10B981):** Reserved for "Tambah" (Add) or "Success" states. It represents growth and positive action.
    - **Electric Blue (#3B82F6):** Used for "Ubah" (Edit) or "Primary" interactions.
    - **Indigo (#6366F1):** For specialized insights or navigation highlights.
- **Contrast:** Typography uses high-contrast whites and off-whites (Slate 50 to Slate 400) to ensure WCAG AA compliance against dark backgrounds.

## Typography

The design system utilizes **Geist** for its technical precision and modern geometric construction, which excels in data-heavy dashboard environments.

- **Hierarchy:** Large display titles are used for page headings to ground the layout. Labels use uppercase with slight letter spacing to differentiate metadata from body content.
- **Readability:** Line heights are generous (1.5x for body) to ensure that even dense tables remain scanable.
- **Weight:** Use `SemiBold` (600) for interactive elements and `Regular` (400) for descriptive text to maintain a clear distinction between what is "info" and what is "action."

## Layout & Spacing

The layout follows a **Fluid Grid** model with strict margin constraints to maintain a premium, spacious feel.

- **Grid Model:** 12-column system for desktop, 4-column for mobile.
- **Card Layouts:** Information is grouped into cards. Cards should have a default internal padding of `lg` (24px) to avoid "cramped" data visuals.
- **Rhythm:** An 8pt grid system governs all spacing. Vertical rhythm between sections should be consistently `xl` (32px).
- **Safe Zones:** Sidebars are fixed at 280px on desktop, collapsing to a hamburger menu on mobile. The main content area utilizes `margin-desktop` (32px) to provide "breathing room" against the viewport edges.

## Elevation & Depth

To achieve a premium look without "AI slop," the design system relies on **Tonal Layers** supplemented by **Low-contrast outlines**.

- **Surface 0 (Base):** Deep Charcoal (#0F172A). Used for the main background.
- **Surface 1 (Cards):** Slightly lighter (#1E293B). These are the primary containers.
- **Surface 2 (Modals/Popovers):** The lightest surface tint (#334155). 
- **Borders:** Every card and input uses a 1px solid border (#334155). This provides crispness that shadows alone cannot achieve.
- **Shadows:** Use a single, highly diffused "Ambient Shadow" for elevated elements like Modals. 
    - *Shadow Profile:* `0px 10px 30px rgba(0, 0, 0, 0.5)`. 
- **Backdrop Blur:** Modals and fixed headers should use a 12px blur with 80% opacity to maintain context of the underlying data.

## Shapes

The design system uses a **Rounded** shape language to soften the industrial feel of the dark theme and make the interface feel more approachable and modern.

- **Standard Elements:** Buttons, Input fields, and small Chips use a 0.5rem (8px) radius.
- **Containers:** Dashboard cards use `rounded-lg` (16px) to create clear visual containment.
- **Avatars/Badges:** Use full pill-shapes (999px) for status indicators and user imagery to provide organic contrast to the rectangular grid.

## Components

### Buttons
- **Primary (Tambah):** Emerald Green background with White text. Bold weight.
- **Secondary (Ubah):** Electric Blue background with White text.
- **Ghost/Tertiary:** No background, Slate-400 text, becomes White on hover.
- **Sizing:** Large (48px height) for main CTA, Medium (36px) for table actions.

### Cards
- Must include a subtle border (#334155) and `rounded-lg` corners.
- Headers within cards should be separated by a subtle horizontal divider.

### Input Fields
- Background: Surface 2 tint (#334155).
- Border: Slate-600.
- Focus State: Border becomes Electric Blue with a subtle 2px outer glow.

### Chips & Badges
- Used for categories or status.
- Semi-transparent backgrounds (10% opacity of the accent color) with full-opacity text of the same color.

### Lists & Tables
- Remove all vertical borders. Use only horizontal dividers.
- Row hover state: Surface 1 highlight to indicate interactivity.
- High-contrast text for primary data (Title/Name) and Slate-400 for secondary data (ID/Date).