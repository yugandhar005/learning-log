import copy

# ===== Reference =====
x = [1, 2, 3]
y = x
y.append(4)
print(x)  # [1, 2, 3, 4]

# ===== Shallow Copy =====
x = [[1, 2], [3, 4]]
y = copy.copy(x)
y[0].append(99)
print(x)  # [[1, 2, 99], [3, 4]]
print(y)  # [[1, 2, 99], [3, 4]]

# ===== Deep Copy =====
x = [[1, 2], [3, 4]]
y = copy.deepcopy(x)
y[0].append(99)
print(x)  # [[1, 2], [3, 4]]
print(y)  # [[1, 2, 99], [3, 4]]

# ===== Mutable Default Fix =====
def add_item(item, items=None):
    if items is None:
        items = []
    items.append(item)
    return items

print(add_item("apple"))
print(add_item("banana"))
print(add_item("cherry"))
# ['apple']
# ['banana']
# ['cherry']
