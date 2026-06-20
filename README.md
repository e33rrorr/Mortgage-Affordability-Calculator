# Mortgage Affordability Calculator

A simple Python command-line tool for estimating mortgage affordability based on applicant income, income tax, National Insurance, deposit, interest rate, and mortgage term.

## Features

The calculator:

* Supports between 1 and 4 applicants
* Combines the annual gross income of all applicants
* Calculates estimated monthly income after income tax and National Insurance
* Estimates the maximum bank loan using a 4.5x income multiplier
* Calculates monthly mortgage payments using the chosen term and interest rate
* Estimates a 10% deposit
* Estimates the maximum affordable property price

## Example Output

```text
----- Mortgage Affordability Estimate -----

Total annual gross income: £65,000.00
Total monthly income after tax and NI: £3,984.78
Estimated bank loan: £292,500.00
Estimated deposit: £29,250.00
Estimated monthly mortgage payment: £1,709.93

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
* The deposit is estimated as 10% of the bank loan.
* The property price is estimated by adding the deposit to the bank loan.

> [!IMPORTANT]
> Actual mortgage affordability can vary depending on lender criteria, credit history, debts, expenses, income type, tax rules, interest rates, deposit size, and regional lending rules.
