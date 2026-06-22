class MonthlyExpensesCalculator:
    """Calculate the user's total monthly expenses."""

    def __init__(self):
        self.monthly_electricity = 0
        self.monthly_water = 0
        self.monthly_gas = 0
        self.monthly_internet = 0
        self.monthly_council_tax = 0

        self.monthly_food = 0
        self.monthly_transport = 0
        self.monthly_loans = 0
        self.monthly_credit_cards = 0
        self.monthly_childcare = 0
        self.monthly_other_expenses = 0

    def get_monthly_expenses(self):
        """Ask the user to enter each monthly expense."""

        self.monthly_electricity = float(input("Enter your monthly electricity bill: £"))
        self.monthly_water = float(input("Enter your monthly water bill: £"))
        self.monthly_gas = float(input("Enter your monthly gas bill: £"))
        self.monthly_internet = float(input("Enter your monthly internet bill: £"))
        self.monthly_council_tax = float(input("Enter your monthly council tax: £"))

        self.monthly_food = float(input("Enter your monthly food cost: £"))
        self.monthly_transport = float(input("Enter your monthly transport cost: £"))
        self.monthly_loans = float(input("Enter your monthly loan repayments: £"))
        self.monthly_credit_cards = float(input("Enter your monthly credit card repayments: £"))
        self.monthly_childcare = float(input("Enter your monthly childcare cost, or 0 if none: £"))
        self.monthly_other_expenses = float(input("Enter any other monthly expenses: £"))

    def calculate_total_monthly_expenses(self):
        """Calculate the user's total monthly expenses."""

        total_monthly_expenses = (
            self.monthly_electricity
            + self.monthly_water
            + self.monthly_gas
            + self.monthly_internet
            + self.monthly_council_tax
            + self.monthly_food
            + self.monthly_transport
            + self.monthly_loans
            + self.monthly_credit_cards
            + self.monthly_childcare
            + self.monthly_other_expenses
        )

        return total_monthly_expenses