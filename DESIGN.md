---
name: Neo-Industrial Mono
colors:
  surface: '#fbf9f8'
  surface-dim: '#dbd9d9'
  surface-bright: '#fbf9f8'
  surface-container-lowest: '#ffffff'
  surface-container-low: '#f5f3f3'
  surface-container: '#efeded'
  surface-container-high: '#eae8e7'
  surface-container-highest: '#e4e2e2'
  on-surface: '#1b1c1c'
  on-surface-variant: '#444748'
  inverse-surface: '#303030'
  inverse-on-surface: '#f2f0f0'
  outline: '#747878'
  outline-variant: '#c4c7c7'
  surface-tint: '#5f5e5e'
  primary: '#000000'
  on-primary: '#ffffff'
  primary-container: '#1c1b1b'
  on-primary-container: '#858383'
  inverse-primary: '#c8c6c5'
  secondary: '#9e4200'
  on-secondary: '#ffffff'
  secondary-container: '#fb6d00'
  on-secondary-container: '#562100'
  tertiary: '#000000'
  on-tertiary: '#ffffff'
  tertiary-container: '#00184a'
  on-tertiary-container: '#467cff'
  error: '#ba1a1a'
  on-error: '#ffffff'
  error-container: '#ffdad6'
  on-error-container: '#93000a'
  primary-fixed: '#e5e2e1'
  primary-fixed-dim: '#c8c6c5'
  on-primary-fixed: '#1c1b1b'
  on-primary-fixed-variant: '#474746'
  secondary-fixed: '#ffdbcb'
  secondary-fixed-dim: '#ffb691'
  on-secondary-fixed: '#341100'
  on-secondary-fixed-variant: '#793100'
  tertiary-fixed: '#dbe1ff'
  tertiary-fixed-dim: '#b3c5ff'
  on-tertiary-fixed: '#00184a'
  on-tertiary-fixed-variant: '#003fa5'
  background: '#fbf9f8'
  on-background: '#1b1c1c'
  surface-variant: '#e4e2e2'
typography:
  headline-lg:
    fontFamily: Space Grotesk
    fontSize: 32px
    fontWeight: '700'
    lineHeight: 40px
    letterSpacing: -0.02em
  headline-md:
    fontFamily: Space Grotesk
    fontSize: 24px
    fontWeight: '600'
    lineHeight: 32px
  body-lg:
    fontFamily: Inter
    fontSize: 16px
    fontWeight: '400'
    lineHeight: 24px
  body-sm:
    fontFamily: Inter
    fontSize: 14px
    fontWeight: '400'
    lineHeight: 20px
  label-md:
    fontFamily: Space Grotesk
    fontSize: 12px
    fontWeight: '500'
    lineHeight: 16px
rounded:
  sm: 0.5rem
  DEFAULT: 1rem
  md: 1.5rem
  lg: 2rem
  xl: 3rem
  full: 9999px
spacing:
  base: 8px
  xs: 4px
  sm: 8px
  md: 16px
  lg: 24px
  xl: 32px
  gutter: 16px
  margin: 24px
---

# Neo-Industrial Design System

## Brand & Style
The brand personality is authoritative, technical, and high-precision. It moves away from the previous warm, organic tones toward a "Neo-Industrial" aesthetic that emphasizes clarity and functional utility. The target audience includes developers, engineers, and data analysts who value efficiency over ornamentation.

The design style is a hybrid of Minimalism and Modern Corporate, utilizing a strictly neutral foundation punctuated by high-alert functional colors. It evokes an emotional response of reliability, objectivity, and focused intensity.

## Colors
The color palette is anchored by a deep charcoal primary, establishing a high-contrast, "ink-on-paper" feel.

*   **Primary:** #1a1a1a (Core branding and headlines)
*   **Secondary:** #ff6f00 (Active warnings and high-priority signals; updated for maximum visibility)
*   **Tertiary:** #226cff (Interactive links and focus states)
*   **Neutral:** #4a4a4a (UI borders and secondary metadata)

The system operates in a Light color mode to maintain a clean, professional workspace environment.

## Typography
The typography system pairs **Space Grotesk** for headings and labels with **Inter** for body copy. 

*   **Headlines & Labels:** Space Grotesk. This font provides a technical, geometric character that reinforces the industrial brand.
*   **Body:** Inter. Utilized for its exceptional readability in dense, data-heavy environments.

Headlines use tight letter-spacing and bold weights. Body text maintains a generous line height for long-form reading.

## Layout & Spacing
The system utilizes a 12-column fluid grid for desktop and a 4-column layout for mobile. A strict 8px baseline grid governs all vertical rhythm.

*   **Gutter:** 16px
*   **Margin:** 24px
*   **Rhythm:** Increments of 8px (8, 16, 24, 32, etc.)

The layout philosophy is modular; elements should feel like "blocks" within a structured machine.

## Elevation & Depth
Elevation is conveyed through **Tonal Layers** and **Low-Contrast Outlines**. Surfaces are distinguished by slight shifts in background hex codes and 1px solid borders using the neutral palette. Shadows are used only for high-level modals and are kept crisp and neutral.

## Shapes
The shape language is "Pill-Industrial." 
*   **Base Roundedness:** 16px (1rem)
*   **Large Components:** 32px (2rem)

This pronounced rounding provides a modern, friendly touch that contrasts with the rigorous, structured feel of the grid-based design.

## Components
*   **Buttons:** Primary buttons are solid #1a1a1a with white text and a pill-shaped profile. Secondary buttons use a 1px border.
*   **Inputs:** Fields use a 1px border (#4a4a4a) and rounded corners. Focus states utilize the Tertiary blue (#226cff).
*   **Cards:** Defined by 1px borders rather than shadows, using a slightly off-white background and significant corner rounding.
*   **Alerts:** Use the Secondary orange (#ff6f00) for high-priority warnings, typically with a bold left-edge border.
*   **Data Tables:** High-density grids with 1px horizontal dividers and Inter body-sm typography.