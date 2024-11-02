# Day 5: Password Generator

## Description:
    This program generates a random password based on user-defined criteria. You can specify the length of the password, as well as the inclusion of uppercase letters, lowercase letters, numbers, and symbols to create a secure and personalized password.

## Objective: 
    To practice generating random characters and strings while enhancing familiarity with list manipulation and loops.

## Skills Practiced:
  * Random selection with random module
  * Using lists to store different character sets
  * Shuffling elements in a list

## Expected Behavior:
The user is prompted to enter the desired number of letters, numbers, and symbols for the password.
The program generates a password using a randomized combination of the specified characters.

## Example Run:
  * **Randomly generated password**
```plaintext
Welcome to the PyPassword Generator
Would you like your password to be completly random? Please choose 'Y' or 'N'
Y
10
A8ey61eaJw
```

  * **User specified password**
```plaintext
Welcome to the PyPassword Generator
Would you like your password to be completly random? Please choose 'Y' or 'N'
n
How many letters would you like in your password?
6
How many letters would you like capitalized
2
How many numbers would you like in your password?
4
How many symbols would you like in your password?
3
Your password is: (!sa(6go18qbSY7
```
## Key Code Concepts:
  * **Random Selection and Shuffling:** Uses random.choice() and random.shuffle() to randomize characters and order.
  * **List Comprehension:** Efficiently builds lists of characters based on user input.

## How to Run:
  * Navigate to the Day 5 folder and run:
```bash
python password_generator.py
```
## What I Learned: 
    This project introduced me to list operations and randomness in Python, which are fundamental in many applications that require user-specific customization.

© 2024 Greg Garrett. All rights reserved.
