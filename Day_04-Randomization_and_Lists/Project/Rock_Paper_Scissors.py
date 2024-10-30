import random

# Rock
rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

# Paper
paper = '''
     _______
---'    ____)____
           ______)
          _______)
         _______)
---.__________)
'''

# Scissors
scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

# Choices
winner = "You Win"
loser = "You lose"
draw = "It's a draw"
options = [rock, paper, scissors]

# Get player choice
players_choice = int(input("What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors.\n"))

# Validate player choice
if players_choice < 0 or players_choice > 2:
    print("Invalid choice. Please enter 0, 1, or 2.")
else:
    # Generates computer choice
    computer_choice = random.choice(options)

    # Displays choices
    print("Your choice:")
    print(options[players_choice])
    print("Computer's choice:")
    print(computer_choice)

    # Determines the outcome
    if players_choice == 0:                    # Player chose Rock
        if computer_choice == scissors:
            print(winner)
        elif computer_choice == paper:
            print(loser)
        else:
            print(draw)
    elif players_choice == 1:                  # Player chose Paper
        if computer_choice == rock:
            print(winner)
        elif computer_choice == scissors:
            print(loser)
        else:
            print(draw)
    else:
        if computer_choice == paper:           # Player chose Scissors
            print(winner)
        elif computer_choice == rock:
            print(loser)
        else:
            print(draw)
    print("\n -")