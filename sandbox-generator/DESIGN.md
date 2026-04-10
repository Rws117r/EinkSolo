# Design System: The Illuminated Cartographer

## 1. Overview & Creative North Star
**Creative North Star: "The Living Manuscript"**

This design system rejects the sterile, pixel-perfect nature of modern software in favor of the tactile, imperfect, and authoritative weight of a 17th-century field journal. We are not building a "web app"; we are crafting a digital artifact that feels as though it was inked by a master cartographer and bound in worn leather.

The experience breaks the "digital template" look through **intentional asymmetry** and **tonal depth**. Elements should not feel like they are floating on a screen, but rather like they are pressed into or embossed upon parchment. We utilize high-contrast typography scales—pairing brutalist sans-serifs with elegant serifs—to create a hierarchy that feels like a printed rulebook rather than a dashboard.

## 2. Colors & Surface Philosophy
The palette is rooted in organic materials: charcoal, bone, and dried blood.

- **Primary (`#610000` / `#8b0000`):** Reserved for "critical" actions and high-importance highlights. It represents the "Dried-Blood Crimson" of a wax seal or an urgent marginalia note.
- **Surface & Background (`#fff8f2`):** The "Aged Parchment." This is the foundation of the entire system.
- **On-Surface/Ink (`#231a07`):** A deep, warm charcoal. Never use pure #000000. This mimics carbon-based ink that has slightly soaked into the page.

### The "No-Line" Rule
Standard 1px solid CSS borders are strictly prohibited for sectioning. To define boundaries, designers must use:
1.  **Background Color Shifts:** Use `surface-container-low` against `surface` to define a sidebar.
2.  **Edge Treatment:** Boundaries should feel like the "deckle edge" of paper. Use the `outline-variant` token at 10-20% opacity only if a physical "lip" is required for an interactive element.

### Surface Hierarchy & Nesting
Treat the UI as a series of stacked vellum sheets.
- **Base Level:** `surface` (The Map itself).
- **Secondary Level:** `surface-container-low` (Floating parchment scraps for UI panels).
- **High Focus:** `surface-container-highest` (The active hex-data card, creating a "lifted" parchment effect).

### Signature Textures
While we use flat tokens, the "soul" of the UI comes from **Surface Tinting**. Use a subtle linear gradient from `primary` to `primary_container` on high-value CTAs to simulate the curved, reflective surface of a wax seal.

## 3. Typography
Typography is our primary tool for conveying the "Old School Renaissance" (OSR) spirit.

- **Display & Headline (FuturaCon-Bol / SpaceGrotesk):** Used for authoritative headers. It provides a "printed press" look that contrasts the organic map.
- **Title & Body (Minion Pro / Newsreader):** The voice of the DM. It should read like a classic RPG rulebook. High legibility with a heavy literary weight.
- **Technical Data (Economica / WorkSans):** Used for hex coordinates, monster stats, and technical labels. It mimics the cramped, efficient hand-lettering of a scout’s ledger.
- **Ornate Initials (CouncilOT / FTYSKORZHENNCV):** Reserved for the first letter of a major chapter or the "Hex Title" in a detail view. This is our "Illuminated Manuscript" moment.

## 4. Elevation & Depth
In this system, depth is **Tonal**, not structural.

- **The Layering Principle:** Avoid shadows where possible. Instead, stack `surface-container-lowest` cards on `surface-container-low` backgrounds. The subtle shift in cream tones provides all the separation a user needs.
- **Ambient Shadows:** For floating elements (like a dice tray or a context menu), use an extra-diffused shadow: `blur: 24px`, `opacity: 6%`, using the `on-surface` color. This simulates the soft shadow a piece of thick paper casts on a desk.
- **The Woodcut Fallback:** If a container needs a border, do not use a line. Use a `0px` radius (as per the scale) and a "Ghost Border"—an `outline-variant` at 15% opacity that mimics the slight indentation of a woodblock print.

## 5. Components

### Buttons (The Stamped Elements)
- **Primary:** Styled as a "Wax Seal." Circular or rectangular with `0px` rounding. Background: `primary`. Text: `on-primary`. On hover, the `surface-tint` creates a slight inner glow.
- **Secondary:** Styled as "Stamped Leather." Background: `secondary_container`. Text: `on-secondary_container`. No border; the depth comes from the color contrast against the parchment.

### Cards & Hex-Details
- **Forbid dividers.** Use vertical white space from the Spacing Scale (e.g., `spacing-8`) to separate sections. 
- Content within cards should use `title-sm` for labels and `body-md` for descriptions.

### Inputs & Fields
- **Text Inputs:** Use a "Hand-Underlined" style. Only the bottom border is visible, using `outline` at 30% opacity.
- **Focus State:** The underline transitions to `primary` (Crimson), as if someone underlined the text with a red ink pen.

### Specialized Components
- **The Ledger List:** For encounter tables. Alternating rows using `surface-container-low` and `surface`, with no vertical lines.
- **The Map Overlay (Glassmorphism):** When a UI element sits directly over the hexmap, use a backdrop-blur (8px) with a semi-transparent `surface` color (`opacity: 80%`). This allows the cartography to "bleed through" the UI, maintaining immersion.

## 6. Do's and Don'ts

### Do:
- **Use "Hard" Corners:** All `roundedness` tokens are `0px`. The world of OSR is sharp and dangerous; the UI should reflect that.
- **Embrace White Space:** Use the Spacing Scale to let the typography breathe. A "crowded" page should feel like a deliberate design choice (a scout's frantic notes), not a layout error.
- **Use Woodcut Icons:** All iconography must look etched, with varying line weights and high contrast.

### Don't:
- **Don't use modern "Blue" for links.** Use `tertiary` (`#00178d`) sparingly or stick to `primary` crimson.
- **Don't use 1px solid borders.** They break the "hand-drawn" illusion instantly.
- **Don't use smooth animations.** Transitions should be "snappy" or "ink-bleed" style (fast opacity fades), avoiding the "sliding" animations typical of modern mobile OSs.