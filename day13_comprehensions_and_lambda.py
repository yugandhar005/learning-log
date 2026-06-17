# ===== List Comprehension =====
numbers = [1, 2, 3, 4, 5]
squares = [n ** 2 for n in numbers]
print(squares)

numbers2 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
even_squares = [n ** 2 for n in numbers2 if n % 2 == 0]
print(even_squares)


# ===== Dict Comprehension =====
square_dict = {n: n ** 2 for n in numbers}
print(square_dict)


# ===== Set Comprehension =====
numbers3 = [1, 1, 2, 2, 3, 3, 4, 4]
unique_squares = {n ** 2 for n in numbers3}
print(unique_squares)


# ===== Lambda =====
square = lambda n: n ** 2
print(square(5))

nums = [5, 2, 8, 1, 9, 3]
sorted_nums = sorted(nums, key=lambda x: -x)
print(sorted_nums)