import random

from auction_list import auction_items
from auction_ascii import gavel_art

print(gavel_art)
print("Welcome to the Silent Auction")
auction = {}

# Randmonly chooses auction items from a list
item_for_bid = random.choice(auction_items)
print(f"For today's auction we have {item_for_bid}")

continue_auction = True

def find_highest_bidder(bidding_dictionary):
    winner = ""
    highest_bid = 0
    for bidder in bidding_dictionary:
        bid_amount = bidding_dictionary[bidder]
        if bid_amount > highest_bid:
            highest_bid = bid_amount
            winner = bidder
    return winner, highest_bid

# Main loop to keep the auction running as long as it is needed
while continue_auction:
    name = input("What is your name? \n")
    bid = int(input("What would you like to bid? \n"))
    
    auction[name] = bid
    should_continue = input("Is there another person to bid? Type 'yes' or 'no' \n").lower()
    print("\n" * 100)
    if should_continue == "no":
        continue_auction = False

winner, highest_bid = find_highest_bidder(auction)

# Displays the winner and bid amount
print(f"And the winner is {winner} with a bid of {highest_bid}!")
