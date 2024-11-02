import random
# lists of all alphanumeric + symbols that can be used to create password
letters = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','y','v','w','x','y','z']
letters_uppercase = [letter.upper() for letter in letters]
numbers = ['0','1','2','3','4','5','6','7','8','9']
symbols = ['!','#','$','%','&','(',')','*','+']

#statements to be called in the application
welcome = "Welcome to the PyPassword Generator"
print(welcome)

password_type = (input("Would you like your password to be completly random? Please choose 'Y' or 'N'\n"))

# Generates a password based on the users criteria
while True:    
    if password_type.lower() == "y":
        number_characters_str = input("How many total characters do you want your password?\n")
        if number_characters_str.isdigit():
            number_characters = int(number_characters_str)
            while True:
                if number_characters > 0:
                    random_password_list = ""
                    while len(random_password_list) < number_characters:
                        random_password = ""
                        random_password_list += str(random.choice(letters + numbers + symbols + letters_uppercase))
                        for char in random_password_list:
                            random_password += char
                    print(random_password)
                    break
                else:
                    number_characters_str = input("Please enter a valid integer\n")
            break
    elif password_type.lower() == "n":
        num_letters = int(input("How many letters would you like in your password?\n"))
        num_capitalized = int(input("How many letters would you like capitalized\n"))
        num_numbers = int(input("How many numbers would you like in your password?\n"))
        num_symbols = int(input("How many symbols would you like in your password?\n"))
        password = ""
        for letter in range(num_letters):
            random_letter = random.randint(0, len(letters) - 1)
            password += letters[random_letter]

        for letter in range(num_capitalized):
            random_upper = random.randint(0, len(letters_uppercase) - 1)
            password += letters[random_upper]

        for symbol in range(num_symbols):
            random_symbol = random.randint(0, len(symbols) - 1)
            password += symbols[random_symbol]

        for number in range(num_numbers):
            random_number = random.randint(0, len(numbers) - 1)
            password += numbers[random_number]
        
        random_password = list(password)

        random.shuffle(random_password)
        print("Your password is: " + "".join(random_password))
    else:
        password_type = input("Please choose Y or N \n")