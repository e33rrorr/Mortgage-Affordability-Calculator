def calculate_total_income(number_of_applicants):
    annual_income = 0

    if number_of_applicants >= 1 and number_of_applicants <= 4:
        for applicant_number in range(1, number_of_applicants + 1):
            applicant_income = float(input(f"Enter the annual income of applicant {applicant_number}: £"))
            annual_income = annual_income + applicant_income

        return annual_income

    else:
        print("This calculator only works for 1 to 4 applicants.")
        exit()


print("Welcome to the Mortgage Affordability Calculator")

number_of_applicants = int(input("Enter the number of applicants: "))
annual_income = calculate_total_income(number_of_applicants)

estimated_bank_loan = annual_income * 4.5
estimated_deposit = estimated_bank_loan * 0.10
estimated_property_price = estimated_bank_loan + estimated_deposit

mortgage_term_years = int(input("How many years would you like your mortgage term to be? "))
annual_interest_rate = float(input("What annual interest rate percentage would you like to use? "))

# Calculates the estimated monthly mortgage repayment using the standard mortgage repayment formula.
number_of_monthly_payments = mortgage_term_years * 12
monthly_interest_rate = annual_interest_rate / 100 / 12

if monthly_interest_rate == 0:
    monthly_payment = estimated_property_price / number_of_monthly_payments

else:
    interest_growth = (1 + monthly_interest_rate) ** number_of_monthly_payments

    top_part = monthly_interest_rate * interest_growth
    bottom_part = interest_growth - 1

    monthly_payment = estimated_property_price * (top_part / bottom_part)

print()
print("\n----- Mortgage Affordability Estimate -----")

print(f"\nEstimated bank loan: £{estimated_bank_loan:,.2f}")


print("\n----- Deposit and Property Price Estimate -----")

print(
    "\nThe deposit you will need to make will vary from bank to bank, "
    "but typically it is around 10% of the property price."
)

print(
    "\nIf you add your deposit to the amount the bank is willing to lend you, "
    "that gives you the estimated property price you may be able to afford."
)

print(
    f"\nFor example, if the bank can lend you £{estimated_bank_loan:,.2f} "
    f"and you have a deposit of £{estimated_deposit:,.2f}, "
    f"then you could afford a property worth about £{estimated_property_price:,.2f}."
)

print(
    f"\nBased on borrowing £{estimated_property_price:,.2f} over {mortgage_term_years} years "
    f"at {annual_interest_rate}%, your estimated monthly mortgage payment would be "
    f"£{monthly_payment:,.2f}.\n"
)


