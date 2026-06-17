# ===== Basic try/except =====
def divide(a, b):
    try:
        result = a / b
        return result
    except ZeroDivisionError:
        return "Cannot divide by zero"

print(divide(10, 2))  # 5.0
print(divide(10, 0))  # Cannot divide by zero


# ===== try/except/else/finally =====
def divide2(a, b):
    try:
        result = a / b
    except ZeroDivisionError:
        print("Cannot divide by zero")
    else:
        print(f"Success: {result}")
    finally:
        print("Division attempted")

divide2(10, 2) 
divide2(10, 0)
# Success: 5.0
# Division attempted
# Cannot divide by zero
# Division attempted

# ===== Custom Exception =====
class InsufficientFundsError(Exception):
    def __init__(self, balance, amount):
        self.balance = balance
        self.amount = amount
        super().__init__(f"Cannot withdraw {amount}. Balance is {balance}")

class BankAccount:
    def __init__(self, balance):
        self.balance = balance

    def withdraw(self, amount):
        if amount > self.balance:
            raise InsufficientFundsError(self.balance, amount)
        self.balance -= amount
        return self.balance

account = BankAccount(1000)

try:
    account.withdraw(500)
    print(f"Balance: {account.balance}")
    account.withdraw(800)
except InsufficientFundsError as e:
    print(f"Error: {e}")
# Balance: 500
# Error: Cannot withdraw 800. Balance is 500