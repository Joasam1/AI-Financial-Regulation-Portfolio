"""Exercise 01: foundational Python using synthetic prudential data.

This is a learning scaffold, not a production supervisory model.
No confidential or institution-specific data are used.
"""

from typing import Dict, List


BankRecord = Dict[str, float | str]


def validate_record(record: BankRecord) -> None:
    """Raise ValueError when required fields are missing or invalid."""
    required = {"bank", "gross_loans", "npl", "capital", "risk_weighted_assets"}
    missing = required.difference(record)
    if missing:
        raise ValueError(f"Missing required fields: {sorted(missing)}")

    numeric_fields = required - {"bank"}
    for field in numeric_fields:
        value = record[field]
        if not isinstance(value, (int, float)) or value < 0:
            raise ValueError(f"{field} must be a non-negative number")


def calculate_indicators(record: BankRecord) -> Dict[str, float | None]:
    """Calculate simple prudential ratios from one bank record."""
    validate_record(record)

    gross_loans = float(record["gross_loans"])
    npl = float(record["npl"])
    capital = float(record["capital"])
    rwa = float(record["risk_weighted_assets"])

    if gross_loans == 0 or rwa == 0:
        raise ValueError("gross_loans and risk_weighted_assets must be greater than zero")

    # Learner-designed business validation: under this simplified definition,
    # NPL cannot exceed the gross-loan balance.
    if npl > gross_loans:
        raise ValueError("npl cannot exceed gross_loans")

    # Learner-designed indicator. A zero NPL is valid, but makes this
    # particular ratio mathematically undefined.
    if npl == 0:
        performing_to_npl_ratio = None
    else:
        performing_to_npl_ratio = (gross_loans - npl) / npl

    return {
        "npl_ratio_pct": 100 * npl / gross_loans,
        "capital_ratio_pct": 100 * capital / rwa,
        "performing_to_npl_ratio": performing_to_npl_ratio,
    }


def summarize_portfolio(records: List[BankRecord]) -> List[Dict[str, float | str | None]]:
    """Return bank names with calculated indicators."""
    summary: List[Dict[str, float | str | None]] = []
    for record in records:
        indicators = calculate_indicators(record)
        summary.append({"bank": record["bank"], **indicators})
    return summary


def main() -> None:
    # Synthetic values created solely for this exercise.
    records: List[BankRecord] = [
        {"bank": "Bank A", "gross_loans": 1200.0, "npl": 96.0, "capital": 180.0, "risk_weighted_assets": 1000.0},
        {"bank": "Bank B", "gross_loans": 900.0, "npl": 117.0, "capital": 126.0, "risk_weighted_assets": 900.0},
        {"bank": "Bank C", "gross_loans": 1500.0, "npl": 105.0, "capital": 195.0, "risk_weighted_assets": 1300.0},
    ]

    for row in summarize_portfolio(records):
        performing_ratio = row["performing_to_npl_ratio"]
        performing_text = "N/A" if performing_ratio is None else f"{performing_ratio:.2f}"

        print(
            f'{row["bank"]}: '
            f'NPL ratio={row["npl_ratio_pct"]:.2f}% | '
            f'Capital ratio={row["capital_ratio_pct"]:.2f}% | '
            f'Performing/NPL={performing_text}'
        )


if __name__ == "__main__":
    main()
