# UK income tax bands for England, Wales, and Northern Ireland
TAX_FREE_ALLOWANCE = 12570

# Basic rate: 20% on income between £12,571 and £50,270
BASIC_RATE_STARTS_AT = 12571
BASIC_RATE_ENDS_AT = 50270
BASIC_RATE = 0.20

# Higher rate: 40% on income between £50,271 and £125,140
HIGHER_RATE_STARTS_AT = 50271
HIGHER_RATE_ENDS_AT = 125140
HIGHER_RATE = 0.40

# Additional rate: 45% on income above £125,140
ADDITIONAL_RATE_STARTS_AT = 125141
ADDITIONAL_RATE = 0.45

# UK National Insurance (NI) Class 1 rates for employees 8% on earnings between £12,570 and £50,270 and 2% on earnings above £50,270
CLASS_1_MAIN_RATE = 0.08
CLASS_1_ADDITIONAL_RATE = 0.02

class TakeHomeIncomeCalculator:

    def __init__(self, annual_salary):
        self.annual_salary = annual_salary

    def calculate_tax(self):
        '''Calculate the total tax based on the annual salary and tax brackets.'''

        if self.annual_salary <= TAX_FREE_ALLOWANCE:
            return 0

        elif self.annual_salary >= BASIC_RATE_STARTS_AT and self.annual_salary <= BASIC_RATE_ENDS_AT:
            tax = (self.annual_salary - TAX_FREE_ALLOWANCE) * BASIC_RATE
            return tax

        elif self.annual_salary >= HIGHER_RATE_STARTS_AT and self.annual_salary <= HIGHER_RATE_ENDS_AT:
            tax = (BASIC_RATE_ENDS_AT - TAX_FREE_ALLOWANCE) * BASIC_RATE + (self.annual_salary - HIGHER_RATE_STARTS_AT) * HIGHER_RATE
            return tax
        
        else:
            basic_rate_tax = 50270 * BASIC_RATE                              # 20% on first £50,270
            higher_rate_tax = (125140 - 50270) * HIGHER_RATE                 # 40% on £50,270–£125,140
            additional_rate_tax = (self.annual_salary - 125140) * ADDITIONAL_RATE  # 45% on the rest
            tax = basic_rate_tax + higher_rate_tax + additional_rate_tax
            return tax

        
    def calculate_national_insurance(self):
        """Calculate Class 1 National Insurance based on annual salary."""

        if self.annual_salary <= TAX_FREE_ALLOWANCE:
            return 0

        elif self.annual_salary > BASIC_RATE_STARTS_AT and self.annual_salary <= BASIC_RATE_ENDS_AT:
            ni_contributions = (self.annual_salary - TAX_FREE_ALLOWANCE) * CLASS_1_MAIN_RATE
            return ni_contributions

        else:
            main_ni_contributions = (BASIC_RATE_ENDS_AT - TAX_FREE_ALLOWANCE) * CLASS_1_MAIN_RATE
            additional_ni_contributions = (self.annual_salary - BASIC_RATE_ENDS_AT) * CLASS_1_ADDITIONAL_RATE

            ni_contributions = main_ni_contributions + additional_ni_contributions

            return ni_contributions
        

    def calculate_take_home_income(self):
        """Calculate the take-home income after tax and National Insurance deductions."""
        tax = self.calculate_tax()
        ni_contributions = self.calculate_national_insurance()
        take_home_income = self.annual_salary - tax - ni_contributions
        return round(take_home_income / 12, 2)
    






