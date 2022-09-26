from decimal import Decimal

import py12c

nper = 12
pmt = 363.78
pv = -3056.00


def test_rate_with_default_arguments():
    results = py12c.rate(nper, pmt, pv)

    assert results == 0.05963422268883278


def test_rate_with_fv_argument():
    results = py12c.rate(nper, pmt, pv, 10000, 1)

    assert results == 0.20020470756876815


def test_rate_due_at_beginning():
    results = py12c.rate(nper, pmt, pv, 0, 1)

    assert results == 0.07265012823626603


def test_rate_with_large_decimal_scale():
    pmt = Decimal("351.622169863986539264256777349669281495")
    pv = Decimal("-3061.762000011")

    results = py12c.rate(nper, pmt, pv) * 100

    assert round(results, 2) == 5.32
