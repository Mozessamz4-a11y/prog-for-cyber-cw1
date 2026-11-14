
# TASK 3 - IP ADDRESS VALIDATOR

def validate_ip(ip_address):
    # Remove space at the beginning and end.
    ip_address = ip_address.strip()

    # Split the address into sections.
    parts = ip_address.split(".")

    # An IPv4 address must contain four sections.
    if len(parts) != 4:
        return False

    for part in parts:
        # Each section must contain numbers only.
        if not part.isdigit():
            return False

        # Each number must be between 0 and 255.
        number = int(part)

        if number < 0 or number > 255:
            return False

    return True


def main():
    ip_address = input("Enter an IP address: ")

    if validate_ip(ip_address):
        print("Valid IP address")
    else:
        print("Invalid IP address")


if __name__ == "__main__":
    main()

