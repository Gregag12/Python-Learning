from cc_logo import logo

alphabet = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']

print(logo)

# Decode and encode funtion
def caesar(text,shift_amount,encode_or_decode):
    output_text = ""

    if encode_or_decode == "decode":
        shift_amount *= -1
    elif encode_or_decode != "encode":
        print(f"You entered an invalid option.\n {direction}")
        return
    
    for letter in text:
        if letter in alphabet:
            shifted_position = (alphabet.index(letter) + shift_amount) % len(alphabet)
            output_text += alphabet[shifted_position]
        else:
            output_text += letter
    print(f"Here is the {encode_or_decode}d result: {output_text}")
    return output_text

# statements to be called in the application
direction = input("Type 'encode' to encrypt or type 'decode' to decrypt:\n").lower()
text = input("Type your message:\n").lower()
shift = int(input("Type your shift number:\n"))

output = caesar(text, shift_amount=shift, encode_or_decode=direction)

restart = input("Would you like to restart? Type 'yes' or 'no':\n").lower()

# Takes the user through the application to encrypt or decrypt messages
while restart == 'yes': 
    direction = input("Type 'encode' to encrypt or type 'decode' to decrypt:\n").lower()
    text = input("Type your message:\n").lower()
    shift = int(input("Type your shift number:\n")) 

    output = caesar(text, shift_amount=shift, encode_or_decode=direction)

    restart = input("Would you like to restart? Type 'yes' or 'no':\n").lower()

if restart == 'no':
    print("Thank you, goodbye")
else: 
    print("Your response wasn't valid. Goodbye and good luck!")