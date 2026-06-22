# Mortgage Affordability Calculator

A simple Python command-line tool for estimating mortgage affordability based on applicant income, income tax, National Insurance, deposit, interest rate, and mortgage term.

## Features

The calculator:

* Validates that the number of applicants is between 1 and 4
* Combines the annual gross income of all applicants
* Calculates estimated monthly income after income tax and National Insurance
* Estimates the maximum bank loan using a 4.5x income multiplier
* Accepts the property price and calculates a 10% deposit
* Calculates the mortgage amount as the property price minus the deposit
* Supports mortgage terms in years and additional months
* Calculates monthly mortgage payments using the chosen term and interest rate
* Collects monthly expenses
* Calculates total monthly expenses
* Shows monthly take-home income remaining after expenses

## Example Output

```text
----- Mortgage Affordability Estimate -----

Total annual income: £65,000.00
Estimated bank loan: £292,500.00
Property price: £300,000.00
Estimated deposit: £30,000.00
Mortgage amount after deposit: £270,000.00
Mortgage term: 25 years and 6 months
Estimated monthly mortgage payment: £1,562.87
Total monthly income after taxes and NI: £4,021.48
Total monthly expenses: £1,200.00
Monthly income after expenses: £2,821.48

-------------------------------------------
```

## Mortgage Payment Formula

The estimated monthly mortgage payment is calculated using the standard repayment mortgage formula:

M = P * (r * (1 + r)^n) / ((1 + r)^n - 1)

Where:

M = monthly mortgage payment
P = mortgage loan amount
r = monthly interest rate
n = total number of monthly payments

## Calculator Assumptions

This tool provides an estimate only. It uses the following assumptions:

* Bank loan affordability is estimated as total annual gross income multiplied by 4.5.
* Monthly income after tax and NI is estimated using the income tax and National Insurance calculation in `take_home_calculator.py`.
* Monthly payments assume a repayment mortgage with a fixed interest rate for the full term.
* The deposit is estimated as 10% of the property price.
* Monthly mortgage payments are calculated using the property price minus the deposit.

> [!IMPORTANT]
> Actual mortgage affordability can vary depending on lender criteria, credit history, debts, expenses, income type, tax rules, interest rates, deposit size, and regional lending rules.
