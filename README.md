# Task 5 — Reusable Cyber Security Utilities

## Student Information
- Name: [samuel moses]
- Campus: [lanarkshire]
- Banner ID: [B01808645]
- Module: Programming for Cyber Security

## Introduction
This Python program demonstrates how reusable security functions can be created in one Python module and imported into another program.

## Program Files

**security_tools.py**  this contains reusable security functions.

**main.py** imports the functions and interacts with the user.

## Features
- Password validation
- Minimum password length of eight characters
- Checks for letters, numbers and symbols
- Basic IPv4 address validation
- Random strong password generation
- Password lengths between 10 and 16 characters
- Uses the secrets module for random password generation

# How to Run
Make sure `security_tools.py` and `main.py` are in the same folder.

Open the terminal and enter:

`py main.py`

# Testing

# Strong Password
![Strong Password](screenshots/strong_password.png)

# Weak Password
![Weak Password](screenshots/weak_password.png)

# Valid IP Address
![Valid IP](screenshots/valid_ip.png)

### Invalid IP Address
![Invalid IP](screenshots/invalid_ip.png)

# Generated Password
![Generated Password](screenshots/generated_password.png)

# Python Concepts
Functions, modules, imports, loops, conditional statements, string operations and the secrets module.

# Limitations
The IP validation performs basic formatting checks. The program does not save passwords or user information.

# Conclusion
This task demonstrates how reusable Python functions can help organise security-related programs and reduce repeated code.
