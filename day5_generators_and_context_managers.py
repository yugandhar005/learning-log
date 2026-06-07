# ===== Generators =====

def even_numbers(limit):
    for i in range(0, limit + 1):
        if i % 2 == 0:
            yield i

for num in even_numbers(10):
    print(num)


def infinite_counter():
    i = 0
    while True:
        yield i
        i += 1


# ===== Context Managers =====

class ManagedResource:
    def __enter__(self):
        print("Resource opened")
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        print("Resource closed")

with ManagedResource() as r:
    print("Doing work...")
