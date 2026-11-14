# Task 3 — IP Address Validator

## Student Information
- Name: [samuel moses]
- Campus: [lanarkshire]
- Banner ID: [B01808645]
- Module: Programming for Cyber Security

## Introduction
This Python program checks whether a user-entered address follows basic IPv4 formatting rules.

## Features
- Accepts an IP address from the user
- Removes surrounding spaces
- Checks for four sections separated by dots
- Checks that every section contains numbers
- Checks that each number is between 0 and 255
- Displays whether the address is valid or invalid

## How to Run
Open the terminal and enter:

`py ip_address_validator.py`

## Testing

### Valid IP Address
Example input: `192.168.1.1`

Expected output: `Valid IP address`

![Valid IP](screenshots/valid_ip.png)

### Invalid IP Address
Example input: `192.168.1.300`

Expected output: `Invalid IP address`

![Invalid IP](screenshots/invalid_ip.png)

## Python Concepts
Functions, lists, loops, strings, conditional statements and type conversion.

## Limitations
This program performs basic validation rather than checking every strict IPv4 formatting convention.

## Conclusion
This task demonstrates how Python can check user input against basic IP address requirements.
