# Task 1 — Security Tool

## Student Information
- Name: [samuel moses]
- Campus: [lanarkshire]
- Banner ID: [B01808645]
- Module: Programming for Cyber Security

## Introduction
This Python program demonstrates basic security functions including login authentication, password checking and a brute-force simulation.

## Features
- Username and password login
- Maximum of three failed login attempts
- Simulated 24-hour account freeze message
- Four-option menu
- Ten-password security check
- Alert when more than 50% of passwords fail
- Brute-force simulation with a guess limit
- Exit option

## How to Run
Open the VS Code terminal and enter:

`py security_tool.py`

For this example, the demonstration credentials are `admin` and `Cyber123!`.

## Testing
Record your actual results and include screenshots.

### Successful Login
![Successful Login](screenshots/login_success.png)

### Security Alert
![Security Alert](screenshots/security_alert.png)

### Brute-Force Simulation
![Brute Force](screenshots/brute_force.png)

### Account Freeze
![Account Frozen](screenshots/account_frozen.png)

## Python Concepts
Functions, loops, conditional statements, variables and input validation.

## Limitations
The account freeze is simulated using a message. The program does not enforce a real 24-hour lockout or securely store passwords.

## Conclusion
This task demonstrates basic security checks and the importance of limiting authentication attempts.