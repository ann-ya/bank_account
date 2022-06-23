from account import Account
from enum import Enum


class Options(Enum):

    ONE = "See balance"
    TWO = "Withdraw"
    THREE = "Deposit"
    FOUR = "See number of withdrawal transactions"
    FIVE = "See number of deposit transactions"
    SIX = "Quit"

    # def __init__(self):
    #     Account.show_info(self)
    #     Account.withdraw(self)
    #     Account.deposit(self)

    def show_options():
        print("Thank you for creating your bank account")
        print("Please choose from the below options:")
       
        for count, option in enumerate(Options):
            print(count +1, option.value)

    def choose_option():

        while True:
            Options.show_options()
            option_choice = int(input())
            if option_choice == 1:
                print(Account.show_info())
            elif option_choice == 2:
                print(Account.withdraw())
            elif option_choice == 3:
                print(Account.deposit())
            elif option_choice == 4:
                print(f"There have been {Account.total_withdrawals} withdrawals")
            elif option_choice == 5:
                print(f"There have been {Account.total_deposits} deposits")
            elif option_choice == 6:
                print("Thank you for using Neko Bank")
                return False
                break
            else:
                print("Please choose a number from 1-6: ")