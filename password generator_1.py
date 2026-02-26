import random
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

    password = ''.join(random.choices(pool, k=size))
    return password


def run():
    print("Welcome to the Password Creator")

    try:
        size = int(input("How long should the password be? (e.g., 12): "))
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