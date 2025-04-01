# Day 9: Secret Auction

## Description:
    A Secret Auction program where multiple users can bid on an item, and the highest bid is revealed at the end. The program allows users to input their bids and names, and only the highest bid is selected as the winner.

## Objective: 
    To implement a bidding system where users can enter their bids and names, and the program identifies the highest bidder using control flow and loops.

## Skills Practiced:
  * Using loops to gather input from multiple users
  * Managing data with dictionaries to store user names and bids
  * Implementing control flow to determine the highest bid
  * Writing functions for input collection and determining the winner

## Expected Behavior:
    The program will start by generating a random item for the bid, then continuously prompt users to enter their name and bid. After each bid is placed, the program asks if another user wants to place a bid. The program will then determine and print the highest bidder at the end.

## Example Run:
```plaintext
 
                        _____________
                         \         /
                          )_______(
                          |"""""""|_.-._,.---------.,_.-._
                          |       | | |               | | ''-.
                          |       |_| |_             _| |_..-'
                          |_______| '-' `'---------'` '-'
                          )"""""""(
                         /_________\
                         `'-------'`
                       .-------------.
                      /_______________\


Welcome to the Silent Auction
For today's auction we have High-end luggage set
What is your name?
Greg
What would you like to bid?
500
Is there another person to bid? Type 'yes' or 'no'
no
```

## Key Code Concepts:

  * **Dictionary for Storing Bids:** Collecting the user name and bid into a dictionary to compare and find the highest bid.
  * **Control Flow and Loops:** Using loops to repeatedly collect input from users and making decisions based on that input (e.g., checking if another user will bid).
  * **Functions for Reusability:** Breaking the program into smaller functions to collect bids and determine the winner.
  * **How to Run:** Navigate to the Day 9 folder and run:
```bash
python secret_autcion.py
```
## What I Learned: 
    This project taught me how to implement a bidding system and apply control flow to determine a winner. It also enhanced my ability to handle user input and dynamically manage data through dictionaries and loops.

© 2024 Greg Garrett. All rights reserved.