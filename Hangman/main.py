import random
import hangman_words
import hangman_art

# For the logo to get printed welcome
print(hangman_art.logo)

display = []
lives = 6
chosen_word_list = []
guess_list = []

# Randomly picking up the word from the list and storing into a variable chosen_word containing string
chosen_word = random.choice(hangman_words.word_list)

# chosen_word_list is a list of chosen_word
for letter in chosen_word:
    chosen_word_list.append(letter)

# initially making the display filled with blanks
for i in range(len(chosen_word)):
    display.insert(i, '_')

print("\nYou need to guess all the blank letters to win and save the person from getting hanged\n")
print(f"{'  '.join(display)}\n")

# Accessing the user guessed letter
# Cross-check of guessed letter against chosen_word
# Updating display at each guessed letter
end_of_game = display == chosen_word_list
while not end_of_game:
    guess = input("Guess a Letter: ").lower()
    if guess in display:
        print(f"\nYou have already guessed \"{guess}\" ")

    # Checking the guessed letter in the chosen_word
    for index in range(len(chosen_word)):
        letter = chosen_word[index]
        if letter == guess:
            display[index] = letter
    print(f"\n{'  '.join(display)}\n")

    # if user guessed wrong
    if guess not in chosen_word:
        print(f"You guessed \"{guess}\", that's not in the word. You lose a life")
        print(f"You have {lives} lives remain")
        print(hangman_art.stages[lives])
        lives -= 1
        if lives == -1:
            print("You Lose..")
            print(f"Answer is: {'  '.join(chosen_word_list)}\n")
            end_of_game = True

    # if user guessed all the letters correctly
    if display == chosen_word_list:
        print("You Win!!")
        end_of_game = True
