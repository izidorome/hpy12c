import hpy12c

rate = 0.07 / 12
pmt = -150.00
pv = 8_000.00
fv = 1_000.00


def test_nper_with_default_arguments():
    results = hpy12c.nper(rate, pmt, pv)

    assert results == 64.07334877066185


def test_nper_with_fv_argument():
    results = hpy12c.nper(rate, pmt, pv, fv)

    assert results == 70.63270889829036


def test_nper_due_at_beggining():
    results = hpy12c.nper(rate, pmt, pv, 0, 1)

    assert results == 63.62363537435202


def test_nper_with_fv_and_due_at_beggining():
    results = hpy12c.nper(rate, pmt, pv, fv, 1)

    assert results == 70.14566694692749


def test_nper_when_interest_rate_is_zero():
    # number of $100 payments to pay off a $1000 loan in full
    results = hpy12c.nper(0.0, -100.0, 1000.0)

    assert results == 10


def test_nper_when_interest_rate_is_zero_with_fv():
    # number of $100 payments to reduce a $1000 loan to $200
    results = hpy12c.nper(0.0, -100.0, 1000.0, -200.00)

    assert results == 8
