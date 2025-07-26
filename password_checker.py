import re

def check_strength(password):
    strength = 0
    if len(password) >= 8:
        strength += 1
    if re.search(r"[A-Z]", password):
        strength += 1
    if re.search(r"[a-z]", password):
        strength += 1
    if re.search(r"\d", password):
        strength += 1
    if re.search(r"[@$!%*#?&]", password):
        strength += 1

    if strength <= 2:
        return "Weak"
    elif strength == 3 or strength == 4:
        return "Moderate"
    else:
        return "Strong"

if __name__ == "__main__":
    pwd = input("Enter a password to check its strength: ")
    print("Password Strength:", check_strength(pwd))
