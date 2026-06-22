import itertools

# ===== zip() =====
names = ["Yugandhar", "Prashik"]
ages = [22, 30]
paired = list(zip(names, ages))
print(paired)


# ===== chain() =====
list1 = [1, 2, 3]
list2 = [4, 5, 6]
list3 = [7, 8, 9]
result = list(itertools.chain(list1, list2, list3))
print(result)


# ===== groupby() =====
users = [
    {"name": "Yugandhar", "dept": "IT"},
    {"name": "Prashik", "dept": "IT"},
    {"name": "Rajesh", "dept": "HR"},
    {"name": "Virat", "dept": "HR"},
]
users.sort(key=lambda u: u["dept"])
for dept, group in itertools.groupby(users, key=lambda u: u["dept"]):
    print(f"{dept}: {[u['name'] for u in group]}")


# ===== islice() =====
def infinite_counter():
    i = 0
    while True:
        yield i
        i += 1

first_10 = list(itertools.islice(infinite_counter(), 10))
print(first_10)