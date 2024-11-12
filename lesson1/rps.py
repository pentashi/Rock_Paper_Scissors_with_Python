import random
import sys
from enum import Enum

# Define Enum for choices
class Choice(Enum):
    ROCK = 1
    PAPER = 2
    SCISSORS = 3

def get_choice_name(choice):
    return choice.name.capitalize()

print("")
playerchoice = input("Enter ...\n1 for Rock,\n2 for Paper, or \n3 for Scissors:\n\n")
player = int(playerchoice)

if player < 1 or player > 3:
    sys.exit("You must enter 1, 2, or 3.")

player_choice = Choice(player)

computer_choice = random.choice(list(Choice))

print("")
print(f"You chose {get_choice_name(player_choice)}.")
print(f"Python chose {get_choice_name(computer_choice)}.")
print("")

if (player_choice == Choice.ROCK and computer_choice == Choice.SCISSORS) or \
   (player_choice == Choice.PAPER and computer_choice == Choice.ROCK) or \
   (player_choice == Choice.SCISSORS and computer_choice == Choice.PAPER):
    print("You win!")
elif player_choice == computer_choice:
    print("Tie game!")
else:
    print("Python wins!")
