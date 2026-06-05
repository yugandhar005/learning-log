# ===== login_required decorator =====

def login_required(func):
    def wrapper(*args, **kwargs):
        user_is_logged_in = True
        if not user_is_logged_in:
            return "Please login first"
        return func(*args, **kwargs)
    return wrapper

@login_required
def my_view(username):
    return f"Welcome {username}"

print(my_view("Yugandhar"))


# ===== timer decorator =====

import time

def timer(func):
    def wrapper(*args, **kwargs):
        current_time = time.time()
        res = func(*args, **kwargs)
        end_time = time.time()
        print(end_time - current_time)
        return res
    return wrapper

@timer
def slow_function():
    time.sleep(2)
    return "done"

print(slow_function())
