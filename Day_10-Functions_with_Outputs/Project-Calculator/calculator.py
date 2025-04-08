# Functionality
#     Program asks the user to type the first number
#     Program asks the user to type a mathematical operator (+, -, *, /)
#     Program asks the user to type a second number
#     Program performs the operation
#     Program asks if the user wants to continue working with the previous number
#     If yes, program loops to use the previous result as the first number and then repeats the calculation process
#     If no, program asks the user for the first number again and wipes all memory of previous calculations

# TODO: Write out the other 3 functions - subtract, multiple, and divide
# TODO: Add these 4 functions into a dictionary as the values. Keys = "+", "-", "*", "/"
# TODO: Use the dictionary operation to perform the calculations. Multiply 4 * 8 using the dictionary
from ascii_calculator import ascii_calc

print(ascii_calc)
print("Welcome to the calculator app")

calculating = True

def add(n1, n2):
    return n1 + n2

def subtract(n1, n2):
    return n1 - n2

def multiply(n1, n2):
    return n1 * n2

def divide(n1, n2):
    return n1 / n2

operations = {
    "+": add, 
    "-": subtract, 
    "*": multiply, 
    "/": divide
    }
n1 = float(input("What is your first number \n"))

while calculating:
    valid_operation = True
    print("What operation would you like to perform?")

    while valid_operation:
        for symbol in operations:
            print(symbol)
        operator = input()
        if operator not in operations:
            print(f"Invalid operator: Please choose from")
        else:
            valid_operation = False
    
    n2 = float(input("what is your second number? \n"))

    calc_value = operations[operator] (n1,n2)
    print(calc_value)

    should_continue = input(
        "\nWoulld you like to continue using the calculator?\n"
        "Type 'Yes' to continue using the same number\n"
        "Type 'No' to start over with new numbers\n"
        "Type 'Quit' to exit \n").lower()
    if should_continue == "yes":
        n1 = calc_value
    elif should_continue == "no":
        print(ascii_calc)
        n1 = float(input("What is your first number \n"))
    elif should_continue == "quit":
        calculating = False
        print("Thank you, Goodbye")
    else:
        print("That wasn't an option")
        n1 = calc_value
        should_continue = input("Woulld you like to continue using the same number? Type 'yes' or 'no' \n").lower()

        