class SavingAccount:
    def __init__(self):
        self.balance = 500

    def withdraw(self, amount):
        self.balance -= amount

    def deposit(self, amount):
        self.balance += amount


# Account 1
acc1 = SavingAccount()
print(f"before accout1 {acc1.balance}")
acc1.deposit(100)
print(f"After accout1 {acc1.balance}")

# Account 2
print("*" * 25)
acc2 = SavingAccount()
print(f"before accout2 {acc2.balance}")
acc2.deposit(200)
print(f"After accout2 {acc2.balance}")
