from BankAccount import *

class User:
    def __init__(self, name, email):
        self.name = name
        self.email = email
        self.account = BankAccount(int_rate=0.02, balance=0)
    
    # other methods

    def make_deposit(self, amount):
        # your code here
        self.account.deposit(amount)
        return self

    def make_withdrawal(self, amount):
        # your code here
        self.account.withdraw(amount)
        return self

    def display_user_balance(self):
        # your code here
        self.account.display_account_info()
        return self

user1 = User("Jayke", "j@gmail.com")

user1.make_deposit(200)
user1.make_withdrawal(50)
user1.display_user_balance()





