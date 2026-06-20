# Mortgage Affordability Calculator

A simple Python command-line tool for estimating mortgage affordability based on applicant income.

## Features

The calculator:

- Supports between 1 and 4 applicants
- Combines the annual income of all applicants
- Estimates the maximum bank loan using a 4.5x income multiplier
- Calculates monthly mortgage payments using the chosen term and interest rate
- Estimates a 10% deposit
- Estimates the maximum affordable property price

## Version 1

This is the first version of the Mortgage Affordability Calculator. It runs in the terminal and focuses on providing a basic mortgage affordability estimate.

The calculator asks for:

- The number of applicants
- The annual income of each applicant
- The mortgage term in years
- The annual interest rate

Future versions may include additional property-buying costs, such as Stamp Duty, solicitor fees, mortgage broker fees, and more detailed affordability checks.

## Usage

1. Clone or download this repository.
2. Open a terminal in the project directory.
3. Run the following command:

```bash
python main.py
```

4. Follow the prompts in the terminal.

## Example Output

```text
----- Mortgage Affordability Estimate -----

Total annual income: £65,000.00
Estimated bank loan: £292,500.00
Estimated deposit: £29,250.00
Estimated monthly mortgage payment: £1,709.93

-------------------------------------------
```

## Calculator Assumptions

This tool provides an estimate only. It uses the following assumptions:

- Bank loan affordability is estimated as total annual income multiplied by 4.5.
- Monthly payments assume a repayment mortgage with a fixed interest rate for the full term.
- The deposit is estimated as 10% of the bank loan.
- The property price is estimated by adding the deposit to the bank loan.

> [!IMPORTANT]
> Actual mortgage affordability can vary depending on lender criteria, credit history, debts, expenses, interest rates, deposit size, and regional lending rules.

