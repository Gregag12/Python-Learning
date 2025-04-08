# Day 10: Calculator

## Description:
    A calculator app that performs basic arithmetic operations (+, -, *, /) with an interactive command-line interface. Users can perform chained calculations or start a new calculation after each result.

## Objective: 
    To create a simple calculator that allows users to perform operations between numbers and continue using the result or start over, all while reinforcing function usage and control flow.

## Skills Practiced:
  * Writing and calling functions
  * Returning values from functions
  * Using dictionaries to map operations to functions
  * Applying loops and conditional logic for user interaction

## Expected Behavior:
    The program prompts the user to enter a number, select an operation, and enter another number. It then performs the calculation and displays the result. Users can continue calculating with the current result or start a new calculation. The loop continues until the user chooses to exit.

## Example Run:
```plaintext
   ______________________
  |  _________________  |
  | | 1234567890.     | |
  | |_________________| |
  |  ___ ___ ___   ___  |          ____      _            _       _
  | | 7 | 8 | 9 | | + | |         / ___|__ _| | ___ _   _| | __ _| |_ ___  _ __
  | |___|___|___| |___| |        | |   / _` | |/ __| | | | |/ _` | __/ _ \| '__|
  | | 4 | 5 | 6 | | - | |        | |__| (_| | | (__| |_| | | (_| | || (_) | |
  | |___|___|___| |___| |         \____\__,_|_|\___|\__,_|_|\__,_|\__\___/|_|
  | | 1 | 2 | 3 | | x | |
  | |___|___|___| |___| |
  | | . | 0 | = | | ÷ | |
  | |___|___|___| |___| |
  |_____________________|

Welcome to the calculator app
What is your first number
3
what operation would you like to perform?
+
-
*
/
+
what is your second number?
37
40.0

Woulld you like to continue using the calculator?
Type 'Yes' to continue using the same number
Type 'No' to start over with new numbers
Type 'Quit' to exit
Quit
Thank you, Goodbye
```

## Key Code Concepts:

  * **Dictionaries as Operation Maps:** Using a dictionary to map string symbols ('+', '-', '*', '/') to their corresponding functions.
  * **Function Return Values:** Using return to send back results from arithmetic functions for reuse.
  * **Recursive Design:** Using recursion to allow restarting the calculator when the user chooses to begin again.
  * **How to Run:** Navigate to the Day 9 folder and run:
```bash
python python calculator.py
```
## What I Learned: 
    This project strengthened my understanding of function structure, return statements, and user input flow. It also showed me how to use dictionaries to simulate switch/case logic and introduced me to the concept of recursion to simplify restarts.

© 2025 Greg Garrett. All rights reserved.