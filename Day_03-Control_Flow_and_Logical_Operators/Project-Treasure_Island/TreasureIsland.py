print("""
  ____________________________________________________________________
 / \-----     ---------  -----------     -------------- ------    ----\
 \_/__________________________________________________________________/
 |~ ~~ ~~~ ~ ~ ~~~ ~ _____.----------._ ~~~  ~~~~ ~~   ~~  ~~~~~ ~~~~|
 |  _   ~~ ~~ __,---'_       "         `. ~~~ _,--.  ~~~~ __,---.  ~~|
 | | \___ ~~ /      ( )   "          "   `-.,' (') \~~ ~ (  / _\ \~~ |
 |  \    \__/_   __(( _)_      (    "   "     (_\_) \___~ `-.___,'  ~|
 |~~ \     (  )_(__)_|( ))  "   ))          "   |    "  \ ~~ ~~~ _ ~~|
 |  ~ \__ (( _( (  ))  ) _)    ((     \\//    " |   "    \_____,' | ~|
 |~~ ~   \  ( ))(_)(_)_)|  "    ))    //\\ " __,---._  "  "   "  /~~~|
 |    ~~~ |(_ _)| | |   |   "  (   "      ,-'~~~ ~~~ `-.   ___  /~ ~ |
 | ~~     |  |  |   |   _,--- ,--. _  "  (~~  ~~~~  ~~~ ) /___\ \~~ ~|
 |  ~ ~~ /   |      _,----._,'`--'\.`-._  `._~~_~__~_,-'  |H__|  \ ~~|
 |~~    / "     _,-' / `\ ,' / _'  \`.---.._          __        " \~ |
 | ~~~ / /   .-' , / ' _,'_  -  _ '- _`._ `.`-._    _/- `--.   " " \~|
 |  ~ / / _-- `---,~.-' __   --  _,---.  `-._   _,-'- / ` \ \_   " |~|
 | ~ | | -- _    /~/  `-_- _  _,' '  \ \_`-._,-'  / --   \  - \_   / |
 |~~ | \ -      /~~| "     ,-'_ /-  `_ ._`._`-...._____...._,--'  /~~|
 | ~~\  \_ /   /~~/    ___  `---  ---  - - ' ,--.     ___        |~ ~|
 |~   \      ,'~~|  " (o o)   "         " " |~~~ \_,-' ~ `.     ,'~~ |
 | ~~ ~|__,-'~~~~~\    \"/      "  "   "    /~ ~~   O ~ ~~`-.__/~ ~~~|
 |~~~ ~~~  ~~~~~~~~`.______________________/ ~~~    |   ~~~ ~~ ~ ~~~~|
 |____~jrei~__~_______~~_~____~~_____~~___~_~~___~\_|_/ ~_____~___~__|
 / \----- ----- ------------  ------- ----- -------  --------  -------\
 \_/__________________________________________________________________/"
""")
print("\nWelcome to Treasure Island!\nYour mission is to find the treasure...Good luck!")

print("Following the trail into the jungle from the beach, you arrive at a cross road. Which road do you take?")
first_choice = input("Which road do you take? Type 'left' or 'right'.\n")
not_an_option = "I'm sorry, that wasn't an option. Game Over."

# Takes the user through choices to find the treasure 
if first_choice.lower() == "right":
    print("You fall down into a pool of lava. \n\n Game Over")
elif first_choice.lower() == "left":
    print("You arrive at a large river with a weatherd looking dock. \n Do you swim across or wait for a boat?")
    second_choice = input("Type 'swim' or 'wait'. \n")
    if second_choice.lower() == "swim":
        print("Something swims by your legs. It's a crocodile! \n\n Game Over!")
    elif second_choice.lower() == "wait":
        print("Night starts to descend and a rickety canoe arrives to take you across the river.")
        print("You travel most of the night and at daybreak arrive at an abandoned castle. \n Within the castle there are three doors - Red, Yellow, and Blue.")
        final_choice = input("Which door will you choose? \n Type 'red', 'yellow', or 'blue'.\n")
        if final_choice.lower() == "red":
            print("You walk through a hallway covered in thick, sticky strands of spider web - only to get stuck, too late to realize you've become something else's dinner.  \n Game Over!")
        elif final_choice.lower() == "blue":
            print("You see what appears to be a half opened treasure chest at the end of the hall. \n As you approach, you hear a quite 'click' sound coming from under your feet. \n You activated a booby trap! \n Game Over!")
        elif final_choice.lower() == "yellow":
            print("The doorway takes you through dark and seemingly endless maze. \nJust when you were about to loose hope, a soft light reaches your senses. \n There it is! You found it at last. \n Congradulations Treasure Hunter! \n\n You Win!")
        else:
            print(not_an_option)
    else:
        print(not_an_option)
else:
    print(not_an_option)