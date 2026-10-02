# Exercise 01 Reflection

**Status:** Conceptual work completed; execution/independent rerun still to be recorded

## 1. Explain the program in my own words

A bank record is sent to the indicator-calculation function. The program first validates the record, extracts the required values, performs the calculations, and returns a dictionary containing the calculated indicators. Selecting a key such as `result["npl_ratio_pct"]` displays only that indicator rather than the entire returned dictionary.

## 2. What did I change?

During the guided exercise, I designed an additional relationship-validation rule, proposed an additional calculated indicator, and decided how its zero-denominator case should be represented. These changes were then incorporated into the learning scaffold.

## 3. Additional validation rule I implemented

Under the simplified definition used in this exercise, NPL should not exceed gross loans. The rule is:

```python
if npl > gross_loans:
    raise ValueError("npl cannot exceed gross_loans")
```

I placed the check before `return` because the function executes sequentially and should reject the invalid relationship before returning calculated results.

## 4. Additional indicator I implemented

I proposed the performing-loans-to-NPL ratio:

```text
(gross_loans - npl) / npl
```

It expresses the performing loan balance relative to the NPL balance. For example, a value of 6.69 means the performing loan balance is approximately 6.69 times the NPL balance.

## 5. Edge case I tested and what happened

If NPL equals zero, the bank record is not automatically invalid. However, the performing-to-NPL ratio cannot be calculated because its denominator would be zero. The program therefore retains the record, reports an NPL ratio of 0%, calculates other valid indicators, and returns `None` for the performing-to-NPL ratio.

## 6. What I learned about Python

This exercise introduced dictionaries, lists, variables, functions, `return`, data types, loops, conditional statements, validation, exceptions and the handling of unavailable derived values. I also learned that quoted numbers are strings, that `return` ends function execution, and that a test can pass because invalid data were correctly rejected.

## 7. Supervisory relevance

Data validation should distinguish between observations that are impossible under the defined data model and observations that are merely unusual. An unusual value may deserve supervisory scrutiny without being deleted or automatically treated as invalid. Derived indicators also require explicit treatment of denominator and data-quality issues.

## 8. What I still need to understand

The next learning step is to run and modify the code independently, strengthen familiarity with Python syntax, and then move from lists/dictionaries toward NumPy and pandas for larger datasets.
