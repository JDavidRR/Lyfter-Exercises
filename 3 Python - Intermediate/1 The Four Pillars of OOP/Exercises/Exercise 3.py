"""3- Investigue qué usos se le pueden dar a la herencia multiple y cree un ejemplo."""

"""Multiple inheritance is best applied when modeling hybrid entities
like robots, smart devices, or financial accounts that naturally combine features from different clases."""

class Account:
    def __init__(self,balance = 0):
            self.balance = balance

    def deposit(self, amount):
        self.balance += amount
        print(f"You deposited ${amount}. New balance: ${self.balance}")

    def withdraw(self, amount):
        self.balance -= amount
        print(f"You withdrew ${amount}. New balance: ${self.balance}")


class Loan:
    def __init__(self, principal, interest_rate, term_months):
        self.principal = principal
        self.interest_rate = interest_rate
        self.term_months = term_months
        self.payments_made = 0

    def calculate_interest(self):
        return self.principal * self.interest_rate

    def calculate_monthly_interest(self):
            return self.principal * (self.interest_rate / 12)

    def make_payment(self, amount):
        self.principal -= amount
        self.payments_made += 1
        print(f"Payment of ${amount} made. Remaining loan: ${self.principal}")


class LoanAccount(Account, Loan):
    def __init__(self, balance, principal, interest_rate, term_months):
        Account.__init__(self, balance)
        Loan.__init__(self, principal, interest_rate, term_months)

    def account_summary(self):
        print("=== Loan Account Summary ===")
        print(f"Balance: ${self.balance}")
        print(f"Loan principal: ${self.principal}")
        print(f"Interest rate: {self.interest_rate * 100}% annually")
        print(f"Term: {self.term_months} months")
        print(f"Payments made: {self.payments_made}\n")

    def make_payment(self, amount):
        self.principal -= amount
        self.balance -= amount
        self.payments_made += 1
        print(f"Payment of ${amount} made. Remaining loan: ${self.principal}")


def main():
    my_loan_ac = LoanAccount(100000,3000000,0.12,24)
    my_loan_ac.account_summary()
    my_loan_ac.make_payment(100000)
    my_loan_ac.account_summary()


if __name__ == "__main__":
    main()

