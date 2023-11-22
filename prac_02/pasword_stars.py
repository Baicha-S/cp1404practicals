"""
CP1404/CP5632 - Practical
Password_stars program to print stars.
"""
PASSWORD_MINIMUM_LENGTH = 6


def main():
    """Main password_stars program."""
    password = get_password()
    print_asterisks(password)


def get_password():
    """Get user's password and validate password length."""
    password = input("Password: ")
    while len(password) < PASSWORD_MINIMUM_LENGTH:
        print("Password doesn't meet a minimum length")
        password = input("Password: ")
    return password


def print_asterisks(password):
    """Print asterisks as long as password length."""
    print("*" * len(password))


main()
