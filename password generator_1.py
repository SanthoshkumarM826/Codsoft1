import secrets
import string


def create_password(size=12, upper=True, lower=True, nums=True, special=True):
    pool = ""

    if upper:
        pool += string.ascii_uppercase
    if lower:
        pool += string.ascii_lowercase
    if nums:
        pool += string.digits
    if special:
        pool += string.punctuation

    if not pool:
        print("Choose at least one character type.")
        return None

    if size <= 0:
        print("Password length must be greater than 0.")
        return None

    selected_types = sum([upper, lower, nums, special])
    if size < selected_types:
        print(f"Password length must be at least {selected_types} for chosen options.")
        return None

    password_chars = []

    if upper:
        password_chars.append(secrets.choice(string.ascii_uppercase))
    if lower:
        password_chars.append(secrets.choice(string.ascii_lowercase))
    if nums:
        password_chars.append(secrets.choice(string.digits))
    if special:
        password_chars.append(secrets.choice(string.punctuation))

    password_chars += [secrets.choice(pool) for _ in range(size - len(password_chars))]
    secrets.SystemRandom().shuffle(password_chars)

    password = ''.join(password_chars)
    return password


def run():
    print("Welcome to the Password Creator")

    try:
        size = int(input("How long should the password be? (e.g., 12): "))
        if size <= 0:
            print("Length must be greater than 0.")
            return
    except ValueError:
        print("Please enter a valid number.")
        return

    upper = input("Add uppercase letters? (y/n): ").lower() == 'y'
    lower = input("Add lowercase letters? (y/n): ").lower() == 'y'
    nums = input("Add numbers? (y/n): ").lower() == 'y'
    special = input("Add special characters? (y/n): ").lower() == 'y'

    password = create_password(size, upper, lower, nums, special)

    if password:
        print(f"\nHere is your new password: {password}")


if __name__ == "__main__":
    run()
