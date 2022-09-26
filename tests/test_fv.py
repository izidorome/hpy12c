import py12c

rate = 0.05 / 12
nper = 12 * 10
pv = -100.00
pmt = -100.00


def test_fv_with_default_arguments():
    results = py12c.fv(rate, nper, pmt, pv)

    assert results == 15692.928894335748


def test_fv_due_at_beggining():
    results = py12c.fv(rate, nper, pmt, pv, 1)

    assert results == 15757.629844104778
