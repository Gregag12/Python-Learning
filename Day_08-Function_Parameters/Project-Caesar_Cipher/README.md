# Day 8: Caesar Cipher

## Description:
    A Caesar Cipher program that encrypts and decrypts messages by shifting each letter of the text by a user-defined number of positions in the alphabet.

## Objective: 
    To implement encryption and decryption logic using control flow, loops, and string manipulation, while practicing functions and user input handling.

## Skills Practiced:
  * String manipulation to shift letters
  * Using loops to process each letter in the message
  * Writing functions for encryption and decryption
  * Handling user input and output dynamically

## Expected Behavior:
    The program prompts the user to either encrypt or decrypt a message, accepts the message and shift value, then processes it according to the Caesar Cipher rules.
   * Encryption shifts each letter of the message by the specified number of positions forward in the alphabet.
   * Decryption reverses the shift to return the original message.


## Example Run:
```plaintext
 _
  ______                                                            ______   __            __
 /      \                                                          /      \ |  \          |  \
|  $$$$$$\  ______    ______    _______   ______    ______        |  $$$$$$\ \$$  ______  | $$____    ______    ______  
| $$   \$$ |      \  /      \  /       \ |      \  /      \       | $$   \$$|  \ /      \ | $$    \  /      \  /      \ 
| $$        \$$$$$$\|  $$$$$$\|  $$$$$$$  \$$$$$$\|  $$$$$$\      | $$      | $$|  $$$$$$\| $$$$$$$\|  $$$$$$\|  $$$$$$\
| $$   __  /      $$| $$    $$ \$$    \  /      $$| $$   \$$      | $$   __ | $$| $$  | $$| $$  | $$| $$    $$| $$   \$$
| $$__/  \|  $$$$$$$| $$$$$$$$ _\$$$$$$\|  $$$$$$$| $$            | $$__/  \| $$| $$__/ $$| $$  | $$| $$$$$$$$| $$      
 \$$    $$ \$$    $$ \$$     \|       $$ \$$    $$| $$             \$$    $$| $$| $$    $$| $$  | $$ \$$     \| $$      
  \$$$$$$   \$$$$$$$  \$$$$$$$ \$$$$$$$   \$$$$$$$ \$$              \$$$$$$  \$$| $$$$$$$  \$$   \$$  \$$$$$$$ \$$      
                                                                                | $$
                                                                                | $$
                                                                                 \$$
Type 'encode' to encrypt or type 'decode' to decrypt:
encode
Type your message:
This is a message
Type your shift number:
5
Here is the encoded result: ymnx nx f rjxxflj
Would you like to restart? Type 'yes' or 'no':
no
Thank you, goodbye
```

## Key Code Concepts:

  * **String Manipulation:** Shifting letters in the alphabet by a specified amount using Python string methods.
  * **Loops and Functions:** Iterating over each character to apply the cipher, and using functions to separate the encryption and decryption logic.
  * **Handling User Input:** Taking input from the user for both the message and shift value, then processing that input dynamically.
  * **How to Run:** Navigate to the Day 8 folder and run:
```bash
python caesar_cipher.py
```
## What I Learned: 
    This project taught me how to implement a simple encryption algorithm in Python, understand basic concepts of cryptography, and work with loops, strings, and functions to process data efficiently.

© 2024 Greg Garrett. All rights reserved.