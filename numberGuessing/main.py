import random
import art

chance = 0
NUMBERS = []
for i in range(1, 101):
    NUMBERS.append(i)
value = random.choice(NUMBERS)


def check_answer(number):
    if number not in NUMBERS:
        print("NOTICE:\tYou have to guess the number only between 1 and 100.")
    else:
        if value > number:
            print("\tToo low.")
        elif value < number:
            print("\tToo high")
        elif value == number:
            print(f"\tYou got it! The answer was {value}")
            return 0


def exit_game():
    return 0


print(art.logo)
print("________________________________________________________")
print("         Welcome to the Number Guessing Game!           ")
print("--------------------------------------------------------")
print("I'm thinking of a number between 1 and 100.\n")
level = input("Choose a difficulty. Type 'easy' or 'hard':\t")

if level == "easy":
    chance += 10
elif level == "hard":
    chance += 5
else:
    exit_game()

while chance > 0:
    print(f"\nYou have {chance} attempts remaining to guess the number.")
    guess = int(input("Make a guess:\t"))
    ENDGAME = check_answer(guess)
    if ENDGAME == 0:
        chance = 0
    else:
        chance -= 1
        if chance > 0:
            print("Guess again.")
        else:
            print("Sorry! You are out of attempts.\n\t*** GAME OVER ***")
