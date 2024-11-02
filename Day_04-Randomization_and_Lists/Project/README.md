# Day 4: Rock Paper Scissors Game

## Description:
A classic Rock, Paper, Scissors game where the player competes against the computer. The program will randomly select one of the options (Rock, Paper, or Scissors) for the computer, and you’ll input your choice to see who wins.

## Skills Practiced:
  * Using the random module for choice selection
  * Implementing conditional logic to determine the winner
  * Practicing game loops and input handling

## Expected Behavior:
  * The program will prompt you to enter “Rock,” “Paper,” or “Scissors.”
  * It will display the computer’s choice and show if you won, lost, or tied.
  * The game can be repeated by rerunning the script.

## Sample Interaction:
```plaintext
What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors.
2
Your choice:

    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)

Computer's choice:

    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)

It's a draw
```
## Key Code Concepts:
  * **Random Choice:** The program uses Python’s random.choice() function to select an option for the computer, simulating randomness in gameplay.
  * **Conditional Statements:** The game logic uses if and elif statements to compare choices and determine the winner.
  * **ASCII Characters:** How to use ASCII characters to display images in a text based program

## How to Run:
```bash
python rock_paper_scissors.py
```

© 2024 Greg Garrett. All rights reserved.
