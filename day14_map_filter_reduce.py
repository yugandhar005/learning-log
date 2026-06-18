# ===== map() =====
numbers = [1, 2, 3, 4, 5]
squares = list(map(lambda n: n ** 2, numbers))
print(squares)


# ===== filter() =====
numbers2 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
even_numbers = list(filter(lambda n: n % 2 == 0, numbers2))
print(even_numbers)


# ===== reduce() =====
from functools import reduce

numbers3 = [1, 2, 3, 4, 5]
total = reduce(lambda a, b: a + b, numbers3)
print(total)

cart = [
    {"item": "apple", "price": 50},
    {"item": "banana", "price": 30},
    {"item": "milk", "price": 60}
]

total_price = reduce(lambda total, item: total + item["price"], cart, 0)
print(total_price)