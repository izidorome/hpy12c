import hpy12c

rate = 0.05 / 12
nper = 12 * 10
pmt = -100.00
fv = 20_000.00


def test_pv_with_default_arguments():
    results = hpy12c.pv(rate, nper, pmt)

    assert results == 9428.135032823473


def test_pv_with_fv_argument():
    results = hpy12c.pv(rate, nper, pmt, fv)

    assert results == -2715.0857731569663


def test_pv_due_at_beggining():
    results = hpy12c.pv(rate, nper, pmt, 0, 1)

    assert results == 9467.418928793571


def test_pv_when_fv_and_due_at_beggining():
    results = hpy12c.pv(rate, nper, pmt, fv, 1)

    assert results == -2675.801877186867
