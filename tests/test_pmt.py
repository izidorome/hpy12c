import hpy12c

rate = 0.075 / 12
nper = 12 * 15
pv = 200_000.00
fv = 10_000.00


def test_pmt_with_default_arguments():
    results = hpy12c.pmt(rate, nper, pv)

    assert results == -1854.0247200054619


def test_pmt_with_fv_argument():
    results = hpy12c.pmt(rate, nper, pv, fv)

    assert results == -1884.225956005735


def test_pmt_due_at_beggining():
    results = hpy12c.pmt(rate, nper, pv, 0, 1)

    assert results == -1842.5090385147448


def test_pmt_with_fv_and_due_at_beggining():
    results = hpy12c.pmt(rate, nper, pv, 0, 1)

    assert results == -1842.5090385147448
