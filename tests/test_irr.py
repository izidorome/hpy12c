from decimal import Overflow

import pytest

import hpy12c


def test_irr_computation(cashflows):
    results = hpy12c.irr(cashflows)

    assert round(results, 5) == 0.00146


@pytest.mark.parametrize(
    "v, desired",
    [
        ([-150000, 15000, 25000, 35000, 45000, 60000], 0.05243),
        ([-100, 0, 0, 74], -0.0955),
        ([-100, 39, 59, 55, 20], 0.28095),
        ([-100, 100, 0, -7], -0.0833),
        ([-100, 100, 0, 7], 0.06206),
        ([-5, 10.5, 1, -8, 1], 0.0886),
    ],
)
def test_basic_values(v, desired):
    results = hpy12c.irr(v)

    assert round(results, 5) == desired


@pytest.mark.parametrize(
    "v",
    [
        (1, 2, 3),
        (-1, -2, -3),
    ],
)
def test_is_none(v):
    # Test that if there is no solution then hpy12c.irr returns None.
    assert hpy12c.irr(v) is None
