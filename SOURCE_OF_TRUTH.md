# SOURCE OF TRUTH

This document defines the canonical evidence hierarchy for **Velocidades de Internet — Chile, Colombia y comparadores internacionales**.

## Canonical hierarchy

1. `data/comparacion_anual_2008_2026.csv` for the published lightweight analytical series.
2. `sources.csv` for source families and official URLs.
3. `docs/metodologia.md` for breaks in comparability and interpretation.
4. `docs/fuentes.md` for source descriptions and reuse caveats.
5. Scripts under `scripts/` for reproducible summaries.
6. README as a presentation layer.

## Methodological boundary

Akamai and Ookla are separate methodological families. The repository does not treat 2008–2026 as one homogeneous measurement system. The 2018 Ookla observation is partial and 2026 is provisional for the periods available at cutoff.

## Integrity rules

- Never interpolate `NA`.
- Do not infer continuity across Akamai/Ookla.
- Keep provider-reported index observations separate from aggregates constructed from Ookla Open Data tiles.
- Preserve source licensing and attribution requirements.
- Label provisional observations and partial coverage.

## Citation

Use `CITATION.cff` for this analytical dataset and retain the attribution required by original publishers.
