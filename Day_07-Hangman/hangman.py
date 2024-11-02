import random

from hangman_words import word_list
from hangman_art import gallows_ascii
from hangman_logo import logo

print(logo)

chosen_word = random.choice(word_list).lower()

placeholder = ''
for letter in chosen_word:
    if letter == ' ':
        placeholder += ' '
    else:
        placeholder += '_'
print('Animal: ' + placeholder)
print(gallows_ascii[6])

game_over = False
correct_guess = []
lives = 6
incorrect_guesses = []
gallows = ()
guess = ()
already_guessed_message = f"\n You already guessed {guess}, try again"

while not game_over and lives > 0:
    print(f'****************************** {lives}/6 LIVES LEFT ******************************')
   
    display = ''
    
    guess = input('Guess a letter: ').lower()
    incorrect_message = f"\n You guessed {guess}, that's not in the word. You lose a life"
    
    # Handles letters not in the chosen word
    if guess not in chosen_word:
        if guess not in chosen_word and guess in incorrect_guesses:
            lives == lives
            print(already_guessed_message)
        elif guess not in chosen_word or guess not in incorrect_guesses:
            incorrect_guesses.append(guess)
            lives -= 1
            print(incorrect_message)
        gallows = gallows_ascii[lives]     

    # Handles letters in the chosen word
    for letter in chosen_word:
        if letter == guess:
            display += letter
            correct_guess.append(guess)
            gallows = gallows_ascii[lives]            
        elif letter == ' ':
            display += ' '
        elif letter in correct_guess:
            display += letter
        else:
            display += '_'
            
    # Displays game to the user        
    print('\n Animal: ', display)
    print('\n', gallows)
    print(f'\n Incorrect guesses: {incorrect_guesses} \n')

    # Endgame messages
    if '_' not in display:
        game_over = True
        print('\n************************ Congratulations! You Win! *************************')
    elif lives == 0:
        print('\n*************************** Game Over. You lose! ***************************')
        print(f'\n********************* The animal was a {chosen_word} ***********************')



