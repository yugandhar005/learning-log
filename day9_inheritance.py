class Animal:
    def __init__(self, name):
        self.name = name
        print(f"Animal created: {self.name}")

class Dog(Animal):
    def __init__(self, name, breed):
        super().__init__(name)  # Animal ka __init__ call karo
        self.breed = breed
        print(f"Dog created: {self.breed}")

d = Dog("Bruno", "Labrador")
print(d.name)
print(d.breed)
