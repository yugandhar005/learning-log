# ===== *args =====
def my_function(*args):
    print(args)
    print(type(args))

my_function(1, 2, 3, 4, 5)


# ===== **kwargs =====
def my_function2(**kwargs):
    print(kwargs)
    print(type(kwargs))

my_function2(name="Yugandhar", age=22, city="Mumbai")


# ===== student_info =====
def student_info(name, *grades, **details):
    print(f"Name: {name}")
    print(f"Grades: {grades}")
    print(f"Details: {details}")

student_info("Yugandhar", 85, 90, 95, city="Mumbai", course="Python")
