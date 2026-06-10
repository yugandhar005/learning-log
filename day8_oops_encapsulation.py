# ===== Basic Class =====

class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def greet(self):
        return f"Hi, I am {self.name} and I am {self.age} years old"

p1 = Person("Yugandhar", 22)
p2 = Person("Prashik", 30)

print(p1.greet())
print(p2.greet())


# ===== Encapsulation =====

class BankAccount:
    def __init__(self, balance):
        self.__balance = balance

    def deposit(self, amount):
        self.__balance += amount

    def get_balance(self):
        return self.__balance

account = BankAccount(1000)
account.deposit(500)
print(account.get_balance())
