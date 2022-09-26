from decimal import Overflow

import pytest

import py12c


def test_npv_computation(cashflows):
    results = py12c.npv(0.281, cashflows)

    assert results == -7787.382638079077


def test_npv_does_not_raises_overflow_error(cashflows):
    try:
        py12c.npv(6.387405495738, cashflows)
    except OverflowError:
        pytest.fail("Overflow Error")
