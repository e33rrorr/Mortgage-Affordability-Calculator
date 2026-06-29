from take_home_calculator import TakeHomeIncomeCalculator
from monthly_expenses_calculator import MonthlyExpensesCalculator


def parse_amount(value):
    """Parse a monetary amount, accepting an optional 'k' suffix (e.g. 200k → 200000)."""
    value = value.strip().lower()
    if value.endswith("k"):
        return float(value[:-1]) * 1000
    return float(value)


def get_number_of_applicants():
    """Ask for and validate a number of applicants between 1 and 4."""
    while True:
        value = input("How many people are applying for the mortgage: ").strip()

        try:
            number_of_applicants = int(value)
        except ValueError:
            print("Only numbers from 1 to 4 are valid.")
            continue

        if 1 <= number_of_applicants <= 4:
            return number_of_applicants

        print("Only numbers from 1 to 4 are valid.")


# Functons for mortgage affordability calculator
def calculate_total_income(number_of_applicants):
    ''' Calculate the total annual income of all applicants and their monthly take-home incomes after taxes and NI. '''
    
    applicant_incomes = []
    monthly_take_home_incomes = []


    if number_of_applicants >= 1 and number_of_applicants <= 4:
        for applicant_number in range(1, number_of_applicants + 1):
            incomes = float(input(f"Enter the annual gross income of applicant {applicant_number}: £"))

            applicant_incomes.append(incomes)

            take_home_calculator = TakeHomeIncomeCalculator(incomes)
            take_home_incomes = take_home_calculator.calculate_take_home_income()
            monthly_take_home_incomes.append(take_home_incomes)

        annual_income = sum(applicant_incomes)
        monthly_take_home_income = sum(monthly_take_home_incomes)

        return annual_income, monthly_take_home_income

    else:
        print("This calculator only works for 1 to 4 applicants.")
        exit()

def calculate_estimated_bank_loan(annual_income):
    ''' Calculate the estimated bank loan based on the total annual income. '''

    income_multiplier = 4.5
    estimated_bank_loan = annual_income * income_multiplier
    return estimated_bank_loan

def calculate_deposit(property_price):
    ''' Calculate the estimated deposit based on the property price. '''
    
    deposit_percentage = 0.10
    estimated_deposit = property_price * deposit_percentage
    return estimated_deposit

def calculate_monthly_mortgage_payment(
    mortgage_amount,
    annual_interest_rate,
    mortgage_term_years,
    mortgage_term_months
):
    ''' Calculate the estimated monthly mortgage payment based on the property price minus the deposit. '''
    
    number_of_monthly_payments = (
        mortgage_term_years * 12
        + mortgage_term_months
    )
    monthly_interest_rate = annual_interest_rate / 100 / 12

    if monthly_interest_rate == 0:
        monthly_payment = mortgage_amount / number_of_monthly_payments
    else:
        monthly_payment = mortgage_amount * (
            monthly_interest_rate * (1 + monthly_interest_rate) ** number_of_monthly_payments
        ) / (
            (1 + monthly_interest_rate) ** number_of_monthly_payments - 1
        )

    return monthly_payment




print("----- Mortgage Affordability Calculator -----\n")

number_of_applicants = get_number_of_applicants()
annual_income, total_monthly_take_home_income = calculate_total_income(number_of_applicants)
estimated_bank_loan = calculate_estimated_bank_loan(annual_income)
property_price = parse_amount(input("Enter the property price: £"))
estimated_deposit = calculate_deposit(property_price)
mortgage_amount = property_price - estimated_deposit



annual_interest_rate = float(input("Enter the annual interest rate: "))
mortgage_term_years = int(input("Enter the mortgage term in years: "))
mortgage_term_months = int(input("Enter the additional mortgage term in months: "))
monthly_payment = calculate_monthly_mortgage_payment(
    mortgage_amount,
    annual_interest_rate,
    mortgage_term_years,
    mortgage_term_months
)

expenses_calculator = MonthlyExpensesCalculator()
expenses_calculator.get_monthly_expenses()
total_monthly_expenses = expenses_calculator.calculate_total_monthly_expenses()
income_after_expenses = total_monthly_take_home_income - total_monthly_expenses



    
print("\n----- Mortgage Affordability Estimate -----")

print(f"\nTotal annual income: £{annual_income:,.2f}")
print(f"Estimated bank loan: £{estimated_bank_loan:,.2f}")
print(f"Property price: £{property_price:,.2f}")
print(f"Estimated deposit: £{estimated_deposit:,.2f}")
print(f"Mortgage amount after deposit: £{mortgage_amount:,.2f}")
print(f"Mortgage term: {mortgage_term_years} years and {mortgage_term_months} months")
print(f"Estimated monthly mortgage payment: £{monthly_payment:,.2f}")
print(f"Total monthly income after taxes and NI: £{total_monthly_take_home_income:,.2f}")
print(f"Total monthly expenses: £{total_monthly_expenses:,.2f}")
print(f"Monthly income after expenses: £{income_after_expenses:,.2f}")