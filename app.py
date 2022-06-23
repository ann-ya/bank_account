from user import User
from account import Account
from options import Options

class App:

    def create_account(name):
        balance = float(input(f"{name.title()}, please confirm your initial deposit: "))
        return balance

    while True:
        print("Welcome to Neko Bank")
        name = input("Enter your name: ")
        age = int(input("Enter your age: "))
        user_one = User(name, age)
        user_one_balance = create_account(user_one.name)
        user_one_account = Account(user_one.name, user_one.age, user_one_balance)
        end_operations = Options.choose_option()
        if end_operations == False:
            break