# Day 7: Hangman Game

## Description:
    A Hangman game where the user guesses letters to reveal a hidden word. The game ends when the word is completely revealed or the player runs out of attempts.

## Objective: 
    To implement control flow with loops and conditionals while practicing string manipulation and list operations.

## Skills Practiced:
  * Using loops for repeated guesses
  * Updating display dynamically with lists
  * Managing game states and conditions
  * Import other python documents and essential modules 

## Expected Behavior:
    The user is prompted to guess letters, which are checked against the hidden word.
    Correct guesses reveal letters in the word, while incorrect guesses reduce the number of attempts.
    The game ends when the word is fully guessed or attempts reach zero.

## Example Run:
```plaintext
 _
| |
| |__   __ _ _ __   __ _ _ __ ___   __ _ _ __
| '_ \ / _` | '_ \ / _` | '_ ` _ \ / _` | '_ \
| | | | (_| | | | | (_| | | | | | | (_| | | | |
|_| |_|\__,_|_| |_|\__, |_| |_| |_|\__,_|_| |_|
                    __/ |
                   |___/
Animal: _____ ___
     _________
     |/      |
     |
     |
     |
     |
     |
  ___|______

****************************** 6/6 LIVES LEFT ******************************
Guess a letter:a

Guess a letter: b

 You guessed b, that's not in the word. You lose a life

 Animal:  _a__a _a_

      _________
     |/      |
     |      (_)
     |
     |
     |
     |
  ___|______


 Incorrect guesses: ['b']

****************************** 5/6 LIVES LEFT ******************************
Guess a letter:
```

## Key Code Concepts:

  * **Lists for Tracking Letters:** Stores guessed letters and updates display as letters are correctly guessed.
  * **Game State Management:** Uses counters and conditional logic to check win/lose conditions.
  * **How to Run:** Navigate to the Day 7 folder and run:
```bash
python hangman.py
What I Learned: This project taught me about game logic and managing state changes within a program, particularly how to track user input dynamically and update outputs in real time.
```
© 2024 Greg Garrett. All rights reserved.