import py12c

rate = 0.075 / 12
nper = 12 * 2
per = 8
pv = 5_000.00


def test_ipmt_with_default_arguments():
    results = py12c.ipmt(rate, per, nper, pv)

    assert results == -22.612926783996798


def test_ipmt_with_fv_argument():
    results = py12c.ipmt(rate, per, nper, pv, 1000)

    assert results == -20.88551214079616


def test_ipmt_due_at_beggining():
    results = py12c.ipmt(rate, per, nper, pv, 0, 1)

    assert results == -22.47247382260551


def test_ipmt_when_per_and_end_at_beggining_is_1():
    results = py12c.ipmt(rate, 1, nper, pv, 0, 1)

    assert results == 0
