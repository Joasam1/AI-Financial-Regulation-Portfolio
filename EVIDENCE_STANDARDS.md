# Evidence Standards

The portfolio is intended to demonstrate technical development through verifiable artifacts rather than claims.

## Reproducibility
Projects should identify dependencies, configuration, data requirements, random seeds where relevant, and instructions sufficient to reproduce reported results.

## Evaluation
Model or system claims should be tied to appropriate metrics, baselines and test data. Where practical, evaluation should include error analysis rather than headline metrics alone.

## Provenance
Datasets and document corpora should state their source and permitted use. Confidential supervisory or institution-specific data must not be published.

## AI-generated code
AI assistance may be used in development, but generated code is not treated as validated merely because it runs or because an agent reports tests as passing. Important functionality should be reviewed, tested and documented.

## Research integrity
Generated summaries, citations and policy conclusions require source verification. Retrieval and generation components should preserve provenance wherever possible.

## Status labels
- **Planned** — defined but substantive implementation has not started.
- **Prototype** — working implementation exists but has not met the full evaluation standard.
- **Validated experiment** — methodology and results have been reproduced under documented conditions.
- **Complete release** — documented, reproducible, evaluated and versioned.

## Security and confidentiality
Secrets belong in environment variables or approved secret stores, never in source control. Public demonstrations should use public, synthetic or appropriately anonymised data.
