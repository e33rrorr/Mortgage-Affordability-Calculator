from take_home_calculator import TakeHomeIncomeCalculator

# Functons for mortgage affordability calculator
def calculate_total_income(number_of_applicants):
    ''' Calculate the total annual income of all applicants and their monthly take-home incomes after taxes and NI. '''
    
    applicant_income = []
    monthly_take_home_income = []


    if number_of_applicants >= 1 and number_of_applicants <= 4:
        for applicant_number in range(1, number_of_applicants + 1):
            applicant_incomes = float(input(f"Enter the annual gross income of applicant {applicant_number}: £"))

            applicant_income.append(applicant_incomes)

            take_home_calculator = TakeHomeIncomeCalculator(applicant_incomes)
            monthly_take_home_incomes = take_home_calculator.calculate_take_home_income()
            monthly_take_home_income.append(monthly_take_home_incomes)
            
        annual_income = sum(applicant_income)
        monthly_take_home_income = sum(monthly_take_home_income)

        return annual_income, monthly_take_home_income

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




print("----- Mortgage Affordability Calculator -----\n")

number_of_applicants = int(input("How many people are applying for the mortgage: "))
annual_income, total_monthly_take_home_income = calculate_total_income(number_of_applicants)
estimated_bank_loan = calculate_estimated_bank_loan(annual_income)
estimated_deposit = calculate_deposit(estimated_bank_loan)



annual_interest_rate = float(input("Enter the annual interest rate: %"))
mortgage_term_years = int(input("Enter the mortgage term in years: "))
monthly_payment = calculate_monthly_mortgage_payment(estimated_bank_loan, annual_interest_rate, mortgage_term_years)




    
print("\n----- Mortgage Affordability Estimate -----")

print(f"\nTotal annual income: £{annual_income:,.2f}")
print(f"Estimated bank loan: £{estimated_bank_loan:,.2f}")
print(f"Estimated deposit: £{estimated_deposit:,.2f}")
print(f"Estimated monthly mortgage payment: £{monthly_payment:,.2f}")
print(f"Total monthly income after taxes and NI: £{total_monthly_take_home_income:,.2f}")


# The monthly mortgage payment is calculated based on the estimated bank loan amount, which represents the total amount borrowed from the bank. The deposit is not subtracted from the estimated bank loan when calculating the monthly mortgage payment.