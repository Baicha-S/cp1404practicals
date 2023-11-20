def main():
    password = get_password()
    print_asterisks(password)


def print_asterisks(password):
    print("*" * len(password))


def get_password():
    password = input("Password: ")
    password_minimum_length = int(input("Minimum Length: "))
    while len(password) < password_minimum_length:
        print("Password doesn't meet a minimum length")
        password = input("Password: ")
    return password


main()
