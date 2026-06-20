# Mortgage Affordability Calculator

def calculate_total_income(number_of_applicants):
    ''' Calculate the total annual income of all applicants. '''
    
    annual_income = 0

    if number_of_applicants >= 1 and number_of_applicants <= 4:
        for applicant_number in range(1, number_of_applicants + 1):
            applicant_income = float(input(f"Enter the annual income of applicant {applicant_number}: £"))
            annual_income = annual_income + applicant_income

        return annual_income

    else:
        print("This calculator only works for 1 to 4 applicants.")
        exit()

def calculate_estimated_bank_loan(annual_income):
    ''' Calculate the estimated bank loan based on the total annual income. '''

    income_multiplier = 4.5
    estimated_bank_loan = annual_income * income_multiplier
    return estimated_bank_loan

def calculate_deposit(estimated_bank_loan):
    ''' Calculate the estimated deposit based on the estimated bank loan. '''
    
    deposit_percentage = 0.10
    estimated_deposit = estimated_bank_loan * deposit_percentage
    return estimated_deposit

def calculate_monthly_mortgage_payment(estimated_bank_loan, annual_interest_rate, mortgage_term_years):
    ''' Calculate the estimated monthly mortgage payment based on the estimated bank loan, annual interest rate, and mortgage term. '''
    
    number_of_monthly_payments = mortgage_term_years * 12
    monthly_interest_rate = annual_interest_rate / 100 / 12

    if monthly_interest_rate == 0:
        monthly_payment = estimated_bank_loan / number_of_monthly_payments
    else:
        monthly_payment = estimated_bank_loan * (
            monthly_interest_rate * (1 + monthly_interest_rate) ** number_of_monthly_payments
        ) / (
            (1 + monthly_interest_rate) ** number_of_monthly_payments - 1
        )

    return monthly_payment


print("----- Mortgage Affordability Calculator -----")

number_of_applicants = int(input("How many people are applying for the mortgage? "))
annual_income = calculate_total_income(number_of_applicants)
estimated_bank_loan = calculate_estimated_bank_loan(annual_income)
estimated_deposit = calculate_deposit(estimated_bank_loan)

annual_interest_rate = float(input("Enter the annual interest rate: "))
mortgage_term_years = int(input("Enter the mortgage term in years: "))
monthly_payment = calculate_monthly_mortgage_payment(estimated_bank_loan, annual_interest_rate, mortgage_term_years)

    
print("\n----- Mortgage Affordability Estimate -----")

print(f"\nTotal annual income: £{annual_income:,.2f}")
print(f"Estimated bank loan: £{estimated_bank_loan:,.2f}")
print(f"Estimated deposit: £{estimated_deposit:,.2f}")
print(f"Estimated monthly mortgage payment: £{monthly_payment:,.2f}")