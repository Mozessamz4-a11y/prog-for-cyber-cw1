
# TASK 5 - REUSABLE SECURITY FUNCTIONS

import secrets
import string


def validate_password(password):
    # Check password length.
    if len(password) < 8:
        return False

    # Check for letters, numbers and symbols.
    has_letter = any(char.isalpha() for char in password)
    has_number = any(char.isdigit() for char in password)
    has_symbol = any(not char.isalnum() for char in password)

    return has_letter and has_number and has_symbol


def validate_ip(ip_address):
    # Remove surrounding spaces.
    ip_address = ip_address.strip()

    # Split the IPv4 address.
    parts = ip_address.split(".")

    if len(parts) != 4:
        return False

    for part in parts:
        if not part.isdigit():
            return False

        number = int(part)

        if number < 0 or number > 255:
            return False

    return True


def generate_password():
    # Generate a random password between 10 and 16 characters.
    length = secrets.randbelow(7) + 10

    uppercase = string.ascii_uppercase
    lowercase = string.ascii_lowercase
    digits = string.digits
    symbols = "!@#$%^&*"

    all_characters = uppercase + lowercase + digits + symbols

    # Include at least one character from each group.
    characters = [
        secrets.choice(uppercase),
        secrets.choice(lowercase),
        secrets.choice(digits),
        secrets.choice(symbols)
    ]

    # Add more characters until the required length.
    for _ in range(length - len(characters)):
        characters.append(secrets.choice(all_characters))

    # Shuffle characters securely.
    secrets.SystemRandom().shuffle(characters)

    return "".join(characters)
