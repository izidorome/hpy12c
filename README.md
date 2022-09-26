# HPy12C

A **pure python** implementation of HP-12C financial calculator.

## Installation


```ruby
pip install 'hpy12c'
```

## Usage

First import hpy12c module and use any financial function provided by the library:

```python
import hpy12c

hpy12c.pmt(0.075 / 12, 12 * 15, 200_000) # ==> -1854.0247200054619
```

## Available Functions

### FV

What is the future value after 10 years of saving $100 now, with
an additional monthly savings of $100 with the interest rate at
5% (annually) compounded monthly?

```python
hpy12c.fv(0.05 / 12, 10 * 12, -100, -100) # ==> 15692.928894335748
```

By convention, the negative sign represents cash flow out (i.e. money not
available today).  Thus, saving $100 a month at 5% annual interest leads
to $15,692.93 available to spend in 10 years.

### IRR

Suppose one invests 100 units and then makes the following withdrawals at regular (fixed)
intervals: 39, 59, 55, 20. Assuming the ending value is 0, one's 100 unit investment
yields 173 units; however, due to the combination of compounding and the periodic
withdrawals, the "average" rate of return is neither simply 0.73/4 nor (1.73)^0.25-1.

```python
hpy12c.irr([-100, 39, 59, 55, 20]) # ==> 0.28095
```

So, the internal rate of return is 28.09%

### IPMT

What is the interest part of a payment in the 8th period (i.e., 8th month),
having a $5,000 loan to be paid in 2 years at an annual interest rate of 7.5%?

```python
hpy12c.ipmt(0.075 / 12, 8, 12 * 2, 5_000.00) # ==> -22.612926783996798
```

So, in the 8th payment, $22.61 are the interest part.

### NPER

If you only had $150/month to pay towards the loan, how long would it take
to pay-off a loan of $8,000 at 7% annual interest?

```python
hpy12c.nper(0.07 / 12, -150, 8000) # ==> 64.07334877066185
```

So, over 64 months would be required to pay off the loan.

### NPV

Calculates the Net Present Value of an investment

```python
hpy12c.npv(0.281, [-100, 39, 59, 55, 29]) # ==> 2.6025181340459755
```

### PMT

What is the monthly payment needed to pay off a $200,000 loan in 15
years at an annual interest rate of 7.5%?

```python
hpy12c.pmt(0.075 / 12, 12 * 15, 200_000) # ==> -1854.0247200054619
```

In order to pay-off (i.e., have a future-value of 0) the $200,000 obtained
today, a monthly payment of $1,854.02 would be required.  Note that this
example illustrates usage of `fv` (future value) having a default value of 0.

### PV

What is the present value (e.g., the initial investment) of an investment
that needs to total $20,000.00 after 10 years of saving $100 every month?
Assume the interest rate is 5% (annually) compounded monthly.

```python
hpy12c.pv(0.05 / 12, 12 * 10, -100, 20_000) # ==> -2715.0857731569663
```

By convention, the negative sign represents cash flow out (i.e., money not available today).
Thus, to end up with $20,000.00 in 10 years saving $100 a month at 5% annual
interest, an initial deposit of $2715,09 should be made.

### RATE

Suppose you take a loan of $50,000.00 to pay in 3 years with a monthly payment of $2,500.00.
What is the rate applied to this loan?

```python
hpy12c.rate(12 * 3, 2_500, -50_000) # ==> 0.036006853458478955
```

So, the rate applied is 3.60%.

# What about others financial libraries available (e.g NumPy financials)?

Most of the algorithms here was heavily inspired by the NumPy project.
The main difference, is that **HPy12C** does not need any dependency, as it was written in Pure Python.
There are some special cases that influenced the development of this library:

* Having a C (or Rust) binding dependency in some environments is not feasable;
* Having the full blown NumPy library could be too much (e.g AWS Lambda);
* Cases when you just want to do some simple financial calculation;

## License

hpy12c is released under the MIT License.

## Special Thanks

A special thanks goes to the python [NumPy project](https://www.numpy.org/) and [Exonio](https://github.com/noverde/exonio), which was the source for most of the functions.
