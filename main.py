
# TASK 5 - MAIN PROGRAM

# Import reusable functions from security_tools.py.
from security_tools import (
    validate_password,
    validate_ip,
    generate_password
)


def main():
    print("--- CYBER SECURITY UTILITIES ---")

    # Ask the user to enter a password.
    password = input("Enter a password: ")

    if validate_password(password):
        print("Password is valid.")
    else:
        print("Password is weak.")
        print("Suggested strong password:", generate_password())

    # Ask the user to enter an IP address.
    ip_address = input("\nEnter an IP address: ")

    if validate_ip(ip_address):
        print("Valid IP address.")
    else:
        print("Invalid IP address.")

    print("\nSecurity checks completed.")


if __name__ == "__main__":
    main()
