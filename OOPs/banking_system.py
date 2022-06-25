class Account:
    def __init__(self, title=None, balance=0):
        self.title_ = title
        self.balance_ = balance

    def withdrawal(self, amount):
        self.balance_ = self.balance_ - amount

    def deposit(self, amount):
        self.balance_ = self.balance_ + amount

    def getbalance(self):
        return self.balance_

class SavingsAccount(Account):
    def __init__(self, title=None, balance=0, interest_rate=0):
        Account.__init__(self, title, balance)
        self.interest_rate_ = interest_rate

    def interestAmount(self):
        return (self.balance_ * self.interest_rate_ / 100)

sachin = SavingsAccount("Sachin Tendulkar", 50000, 8)
print("Initial Balance: ", sachin.balance_)

sachin.withdrawal(10000)
print("Balance after withdrawal: ", sachin.balance_)

sachin.deposit(50000)
print("Balance after deposit: ", sachin.balance_)

print("Interest on the current balance: ", sachin.interestAmount())
