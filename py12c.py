def pmt(rate, nper, pv, fv = 0, end_or_beginning = 0):
    temp = (1 + rate) ** nper
    fact = (1 + rate * end_or_beginning) * (temp - 1) / rate

    return -(fv + pv * temp) / fact
