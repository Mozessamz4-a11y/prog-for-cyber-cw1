
# TASK 4 - SECURITY INCIDENT MANAGER

def main():
    # Create a dictionary containing incident information.
    incident = {
        "username": "admin",
        "ip_address": "192.168.1.10",
        "event_type": "Failed Login",
        "risk_level": "Medium"
    }

    # Display the username and IP address.
    print("--- ORIGINAL INCIDENT ---")
    print("Username:", incident["username"])
    print("IP Address:", incident["ip_address"])

    # Add a new field.
    incident["status"] = "Under Investigation"
    print("\nStatus added:", incident["status"])

    # Update the existing risk level.
    incident["risk_level"] = "High"
    print("Updated risk level:", incident["risk_level"])

    # Remove a field from the dictionary.
    removed_value = incident.pop("event_type")
    print("Removed event type:", removed_value)

    # Display the remaining dictionary.
    print("\n--- UPDATED INCIDENT ---")

    for key, value in incident.items():
        print(f"{key}: {value}")

    # Count the remaining fields.
    print("\nNumber of remaining fields:", len(incident))


if __name__ == "__main__":
    main()

