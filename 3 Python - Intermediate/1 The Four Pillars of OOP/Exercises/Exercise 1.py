"""1- Cree una clase de BankAccount que:
Tenga un atributo de balance.
Tenga un método para ingresar dinero.
Tengo un método para retirar dinero.

Cree otra clase que herede de esta llamada SavingsAccount que:
Tenga un atributo de min_balance que se pueda asignar al crearla.
Arroje un error si al intentar retirar dinero, el retiro haría que el balance quede debajo del min_balance.
Es decir que sí se pueden hacer retiros siempre y cuando el balance quede arriba del min_balance."""

class InsufficientFundsError(Exception):
    def __init__(self, amount, balance, min_balance = None):
        message = ''
        if min_balance is None:
            message = f"You attempted to withdraw ${amount}, but balance is only ${balance}."
        else:
            message = (f"You attempted to withdraw ${amount}, but balance ${balance} cannot go below the minimum ${min_balance}.")
        super().__init__(message)
        self.amount = amount
        self.balance = balance
        self.min_balance = min_balance


class BankAccount():
    def __init__(self,balance = 0):
        self.balance = balance

    def deposit(self, amount):
        self.balance += amount
        print(f"You deposited ${amount}. New balance: ${self.balance}")

    def withdraw(self, amount):
        try:
            if amount > self.balance:
                raise InsufficientFundsError(amount, self.balance)
            self.balance -= amount
            print(f"You withdrew ${amount}. New balance: ${self.balance}")
        except InsufficientFundsError as e:
            print(f"Error [InsufficientFundsError]: {e}")


class SavingsAccount(BankAccount):
    def __init__(self,balance,min_balance):
        BankAccount.__init__(self, balance)
        self.min_balance = min_balance

    def withdraw(self, amount):
        try:
            if self.balance - amount >= self.min_balance:
                self.balance -= amount
                print(f"You withdrew ${amount}. New balance: ${self.balance}")
            else:
                raise InsufficientFundsError(amount, self.balance, self.min_balance)
        except InsufficientFundsError as e:
            print(f"Error [InsufficientFundsError]: {e}")


def main():
    my_bank_ac = BankAccount(50)
    my_bank_ac.withdraw(100)
    my_bank_ac.deposit(50)
    my_bank_ac.withdraw(25)

    my_savings_ac = SavingsAccount(100,25)
    my_savings_ac.withdraw(80)
    my_savings_ac.withdraw(75)


if __name__ == "__main__":
    main()

