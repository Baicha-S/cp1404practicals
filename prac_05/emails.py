""""Emails Program"""


def main():
    """store name according to user's email and display name with email."""
    email_to_name = {}
    email = input("Email: ")
    while email != "":
        name = extract_name(email)
        name_check = input(f"Is your name {name}? (Y/n) ").upper()
        if name_check != "Y" and name_check != "":
            name = input("Name: ")
        email_to_name[email] = name
        email = input("Email: ")
    print()

    for email in email_to_name:
        print(f"{email_to_name[email]} ({email})")


def extract_name(email):
    """Extract name from email."""
    name_split = email.split("@")[0]
    name_parts = name_split.split(".")
    name = " ".join(name_parts).title()
    return name


main()

