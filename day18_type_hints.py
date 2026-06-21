from typing import Dict, List, Optional


# ===== Basic Type Hints =====
def add_user(name: str, age: int) -> str:
    return f"{name} is {age} years old"


print(add_user("Yugandhar", 22))


# ===== Optional Type =====
def get_user_email(user_id: int) -> Optional[str]:
    if user_id == 1:
        return "yugandhar@example.com"
    return None


print(get_user_email(1))
print(get_user_email(2))


# ===== List and Dict Type Hints =====
def get_active_users(users: List[str]) -> Dict[str, bool]:
    return {user: True for user in users}


result = get_active_users(["Yugandhar", "Prashik", "Rajesh"])
print(result)
