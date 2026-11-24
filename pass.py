# Password Strength Checker

A simple Python program that checks password strength using basic security criteria and provides suggestions to improve it.


## Features

- Checks password length
- Detects lowercase letters
- Detects uppercase letters
- Detects numbers
- Detects special characters
- Displays a strength score out of 5
- Provides suggestions for weak passwords

## Technologies Used

- Python 3
- Regular Expressions (`re`)

## How to Run

1. Install Python 3.
2. Download or clone the repository.
3. Open the project folder in your terminal.
4. Run the following command:

```bash
python3 password_strength.py
```

## How It Works

The program checks the password against five criteria. Each satisfied criterion adds one point to the score.

- 5 points: Strong
- 3–4 points: Medium
- 0–2 points: Weak

If any criteria are missing, the program displays suggestions to improve the password.

## Note

This is a basic educational project. It checks password composition but does not measure real-world resistance to guessing or password cracking.
