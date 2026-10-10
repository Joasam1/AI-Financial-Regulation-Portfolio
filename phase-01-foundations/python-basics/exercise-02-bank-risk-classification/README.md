# Exercise 02 — Bank Risk Classification and Supervisory Analytics

## Objective
Build a beginner-friendly Python workflow to validate bank-level capital adequacy and non-performing loan (NPL) ratios, classify banks into four illustrative supervisory risk states, and summarize the distribution of valid records.

## Inputs
Each bank is represented by a Python dictionary containing `name`, `car`, and `npl_ratio`. CAR and NPL ratios are expressed as percentages (e.g., `13` means 13%).

## Illustrative classification rules

| Classification | CAR | NPL ratio |
|---|---|---|
| Green — Stable | >= 13% | <= 10% |
| Blue — Asset Quality Risk | >= 13% | > 10% |
| Yellow — Capital Risk | < 13% | <= 10% |
| Red — Combined Risk | < 13% | > 10% |

These are learning thresholds, **not official regulatory thresholds or supervisory decisions**.

## Data validation
Records are excluded from risk classification when CAR or NPL is missing, is not numeric, is a Boolean, or is non-finite (`NaN`, positive infinity, or negative infinity). Negative CAR/NPL values and NPL ratios above 100% are also rejected. CAR is not capped at 100%.

## Illustrative results
For the eight-bank integration-test dataset discussed during development:

| Classification | Count | Share of valid records |
|---|---:|---:|
| Green | 2 | 40% |
| Blue | 1 | 20% |
| Yellow | 1 | 20% |
| Red | 1 | 20% |
| **Valid records** | **5** | **100%** |
| Invalid records | 3 | Excluded |
| **Total submitted** | **8** | |

These are expected results from the example data; they should be confirmed by running the notebook end to end.

## How to run
1. Open `bank_risk_classification.ipynb` in JupyterLab.
2. Select the Python environment containing the notebook kernel.
3. Choose **Kernel → Restart Kernel and Run All Cells**.
4. Confirm that the displayed classifications and totals match the expected results above.

## Skills demonstrated
Python dictionaries, functions, conditional statements, loops, input validation, handling missing/non-finite values, aggregation, percentage calculations, and basic supervisory risk reporting.

## Limitations and next steps
This is a small illustrative dataset, not a calibrated early-warning system. The thresholds are fixed and hypothetical. Future work could add automated unit tests, file-based inputs, charts, time-series analysis, and sensitivity testing.
