
import random

rock = '''
    ______
---'   ___)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)_____
          _______)
       __________)
      (____)
---.__(___)
'''

# Number of choices to play and choose
choices = [rock, paper, scissors]

# User choice code
print("Type:\n0 for Rock\n1 for Paper\n2 for Scissors")
player = int(input("What do you choose?\n"))
while player > 2:
    print("You have typed invalid choice, you lose!\n")
    print("Type:\n0 for Rock\n1 for Paper\n2 for Scissors")
    player = int(input("What do you choose?\n"))
print("\nYour Choice: ")
player_choice = choices[player]
print(player_choice)

# Computer choice using random module
print("\nComputer Choice:\n")
computer = random.randint(0, 2)
computer_choice = choices[computer]
print(computer_choice)

if computer_choice == player_choice:
    print("Game is Tie")
elif (computer_choice == rock and player_choice == scissors) or (computer_choice == scissors and player_choice == paper) or (computer_choice == paper and player_choice == rock):
    print("You Lose the Game")
elif (computer_choice == scissors and player_choice == rock) or (computer_choice == paper and player_choice == scissors) or (computer_choice == rock and player_choice == paper):
    print("You Win the Game")
