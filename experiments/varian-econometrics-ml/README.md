# Varian (2014) — Integrated Econometrics and Machine Learning Lab

**Status:** Synthetic-data teaching and reproducibility exercise. **No real bank records or real bank failures.**

## Files
- [Full Jupyter notebook](Varian_2014_Integrated_Synthetic_Banking_Lab.ipynb): source cells for 12-part structured experimental workflow.
- [Synthetic dataset](data/synthetic_varian_bank_panel.csv): 900 monthly observations, 15 fictitious banks, 2018–2022; 6-month forward label is missing in last 6 months per bank.

## Setup
```bash
python -m pip install jupyterlab numpy pandas matplotlib scikit-learn
python -m jupyter lab
```
Open the notebook from this directory and run cells sequentially. No real supervisory data is required.

## Methodology
Includes prediction versus inference; descriptive risk quadrants; point-in-time feature engineering; six-month label embargo; transparent logistic baseline; CART; Random Forest; gradient boosting; L1/L2 shrinkage; bank-block bootstrap variable selection; permutation importance; synthetic time-series plots; counterfactual cautions; model uncertainty; and ten consolidation exercises.

**Important:** This dataset is generated for teaching, not for validation of supervisory effectiveness. Random synthetic event-generation assumptions are not empirical evidence. Model evaluation may be noisy because of small validation windows. A public notebook must not contain confidential data.

**Source and classification:** Varian, H. R. (2014). *Big Data: New Tricks for Econometrics*. JEP 28(2), 3–28. https://doi.org/10.1257/jep.28.2.3 — Foundational / Methodological / Conceptual Review.
