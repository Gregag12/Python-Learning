# Day 8: Caesar Cipher

## Description:
    The Caesar Cipher is a basic encryption tool that shifts each letter in the message by a specified number of positions. The program allows the user to encrypt or decrypt a message by entering a shift value.

## Objective: 
    To practice using functions for code modularity and to gain experience with character encoding and manipulation.

## Skills Practiced:
  * Modular programming with functions
  * Character encoding and shifting
  * Managing user input for encryption and decryption

## Expected Behavior:
  * The user is prompted to choose between encryption and decryption, input a message, and specify a shift number.
  * The program shifts each letter in the message according to the specified shift value and outputs the result.

## Example Run:
```plaintext
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
Go Bananas
Type your shift number:
3
Here is the encoded result: jr edqdqdv
Would you like to restart? Type 'yes' or 'no':
yes
Type 'encode' to encrypt or type 'decode' to decrypt:
decode
Type your message:
jr edqdqdv
Type your shift number:
3
Here is the decoded result: go bananas
Would you like to restart? Type 'yes' or 'no':
no
Thank you, goodbye
```

## Key Code Concepts:
  * **Functions:** Uses functions to handle encryption and decryption, enhancing modularity.
  * **Character Shifting:** Applies character manipulation techniques to create a basic cipher.

## How to Run: 
   * Navigate to the Day 8 folder and run:
```bash
python caesar_cipher.py
```

## What I Learned: 
  This project introduced me to encryption basics and the importance of modular functions to separate program functionality clearly and efficiently.

© 2024 Greg Garrett. All rights reserved.