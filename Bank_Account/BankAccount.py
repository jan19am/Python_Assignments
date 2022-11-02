class BankAccount:
    def __init__(self, int_rate = 0.00, balance = 0): 
        self.int_rate = int_rate
        self.balance = balance

    def deposit(self, amount):
        self.amount = amount
        self.balance = self.balance + amount
        print(f"Balance: {self.balance}")
        return self

    def withdraw(self, amount):
        self.amount = amount
        self.balance = self.balance - amount
        print(f"Balance: {self.balance}")
        if self.balance <= 0:
            print("Insufficient funds: Charging a $5 fee")
            self.balance = self.balance - 5
            print(f"Balance: {self.balance}")
        return self

    def display_account_info(self):
        print(f"Balance: {self.balance}")
        return self

    def yield_interest(self):
        self.balance = (self.balance * self.int_rate) + self.balance
        print(f"Balance: {self.balance}")
        return self


BofA = BankAccount(0.01, 300)
NavyFed = BankAccount(0.05, 200)

# Deposit Example
# BofA.deposit(20)
# print(BofA.balance)

# # Withdraw Example
# BofA.withdraw(20)
# # print(BofA.balance)

# # Display Example
# BofA.display_account_info()

# # Yield Example
# BofA.yield_interest()


# 1st Account
(
    BofA.deposit(20)
        .deposit(12)
        .deposit(20)
        .withdraw(52)
        .yield_interest()
        .display_account_info()
)

# 2nd Account
(
    NavyFed.deposit(200)
            .deposit(25)
            .withdraw(25)
            .withdraw(100)
            .withdraw(35)
            .withdraw(65)
            .yield_interest()
            .display_account_info()
)

