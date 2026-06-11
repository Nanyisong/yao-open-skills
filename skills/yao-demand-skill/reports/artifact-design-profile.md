# Artifact Design Profile

## Artifact Family

High-trust product demand assessment report.

The artifact should read like a decision memo with evidence and model-backed reasoning, not like a marketing landing page or a BI dashboard.

## Visual System

- background: pure white `#ffffff`
- accent: ink-blue `#1B365D`
- text: warm near-black and warm graphite
- typography: serif-led Chinese document hierarchy
- layout: centered long document, bounded width, quiet section rhythm
- navigation: HTML-only sticky top menu
- diagrams: inline SVG for workflow, demand triangle, and visual diagnostic charts
- tables: restrained borders, horizontal overflow on screen, compact print styling

## Density Strategy

- Open with decision, score, opportunity, and risk.
- Follow with a visual diagnosis section containing at least 10 chart modules.
- Each chart module carries an insight, a recommendation, confidence, and source or assumption binding.
- Use short fact cards for product overview only.
- Use tables when comparing segments, competitors, sources, risks, or experiments.
- Use prose for score reasoning.
- Move dense source metadata to appendix or method section.

## Diagram Strategy

Core visual modules are part of the artifact contract:

1. Process flow: input -> parse -> research -> analyze -> score -> output.
2. Demand triangle: lack, target object, consumer ability, center demand statement, score values.
3. Visual diagnostics: score gauge, radar, bar, heatmap, matrix, funnel, evidence distribution, recommendation priority, risk, and forecast charts.

HTML and PDF render diagrams as static SVG. Markdown gets table/text equivalents. Word gets PNG chart insertion when optional dependencies are available and chart-equivalent tables otherwise.

## QA Focus

- white background in HTML and PDF
- sticky top menu visible in HTML and hidden in PDF
- no nested cards or decorative visual noise
- no clipped diagram text
- at least 10 chart modules in formal HTML/PDF reports
- each chart has visible insight and recommendation text
- no long URL or evidence overflow
- citations readable without cluttering core paragraphs
