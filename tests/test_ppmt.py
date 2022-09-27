import hpy12c as hp

rate = 0.075 / 12
nper = 12 * 15
per = 8
pv = 200_000.00


def test_ppmt_with_default_arguments():
    results = hp.ppmt(rate, per, nper, pv)

    assert results == -630.9514842574954


def test_ppmt_with_fv_argument():
    results = hp.ppmt(rate, per, nper, pv, 1000)

    assert results == -634.1062416787827


def test_ppmt_due_at_beggining():
    results = hp.ppmt(rate, per, nper, pv, 0, 1)

    assert results == -627.032530939126


def test_ppmt_when_per_and_end_at_beggining_is_1():
    results = hp.ppmt(rate, 1, nper, pv, 0, 1)

    assert results == -1842.5090385147448
