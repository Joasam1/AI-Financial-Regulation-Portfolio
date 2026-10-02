"""Tests for Exercise 01."""

import pytest

from exercise_01_prudential_summary import calculate_indicators, summarize_portfolio


def test_calculate_indicators() -> None:
    record = {
        "bank": "Test Bank",
        "gross_loans": 1000.0,
        "npl": 100.0,
        "capital": 150.0,
        "risk_weighted_assets": 1000.0,
    }
    result = calculate_indicators(record)
    assert result["npl_ratio_pct"] == pytest.approx(10.0)
    assert result["capital_ratio_pct"] == pytest.approx(15.0)


def test_multiple_records() -> None:
    records = [
        {"bank": "A", "gross_loans": 100.0, "npl": 5.0, "capital": 12.0, "risk_weighted_assets": 80.0},
        {"bank": "B", "gross_loans": 200.0, "npl": 20.0, "capital": 30.0, "risk_weighted_assets": 200.0},
    ]
    result = summarize_portfolio(records)
    assert len(result) == 2
    assert result[0]["bank"] == "A"


def test_zero_denominator_rejected() -> None:
    record = {
        "bank": "Test Bank",
        "gross_loans": 0.0,
        "npl": 0.0,
        "capital": 10.0,
        "risk_weighted_assets": 100.0,
    }
    with pytest.raises(ValueError):
        calculate_indicators(record)


def test_negative_value_rejected() -> None:
    record = {
        "bank": "Test Bank",
        "gross_loans": 100.0,
        "npl": -1.0,
        "capital": 10.0,
        "risk_weighted_assets": 100.0,
    }
    with pytest.raises(ValueError):
        calculate_indicators(record)
