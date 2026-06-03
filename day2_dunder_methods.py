## Day 2 - dunder methods
- Learned Python Data Model
- __repr__ vs __str__ difference
- __add__, __len__, __getitem__

class Box:
    def __init__(self, value):
        self.value = value

    def __repr__(self):
        return f"Box({self.value})"

    def __str__(self):
        return f"A box containing {self.value}"

box = Box(10)
print(repr(box))
print(str(box))
print(box)


Output:
Box(10)
A box containing 10
A box containing 10
