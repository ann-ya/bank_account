from user import User
# from options import Options

class Account(User):
    total_deposits = 0
    total_withdrawals = 0

    def __init__(self, name, age, balance):
        super().__init__(name, age)
        self.balance = balance
        # self.Options = Options(self)

    def show_info(self):
        return f"{self.name} has a remaining balance of: £{round(self.balance, 2)}"

    def deposit(self):
        deposit = float(input(f"{self.name.title()}, please enter the amount you would like to deposit: "))
        print("Deposit complete")
        self.balance += deposit
        self.total_deposits += 1
        return f"Your balance is now: {round(self.balance, 2)}"

    def withdraw(self):
        withdraw = float(input(f"{self.name.title()}, please enter the amount you would like to withdraw: "))
        if self.balance < withdraw:
            return "You don't have sufficient funds for this operation"
        else:
            print("Withdrawal complete")
            self.balance -= withdraw
            self.total_withdrawals += 1
            return f"Your balance is now: {round(self.balance, 2)}"