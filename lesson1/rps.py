import random
from enum import Enum

# Define Enum for choices
class Choice(Enum):
    ROCK = 1
    PAPER = 2
    SCISSORS = 3

def get_choice_name(choice):
    return choice.name.capitalize()

def get_player_choice():
    while True:
        try:
            player_choice = int(input("Enter ...\n1 for Rock,\n2 for Paper, or \n3 for Scissors:\n\n"))
            if player_choice in [1, 2, 3]:
                return Choice(player_choice)
            else:
                print("Invalid choice. Please enter 1, 2, or 3.")
        except ValueError:
            print("Invalid input. Please enter a number.")

def determine_winner(player_choice, computer_choice):
    if (player_choice == Choice.ROCK and computer_choice == Choice.SCISSORS) or \
       (player_choice == Choice.PAPER and computer_choice == Choice.ROCK) or \
       (player_choice == Choice.SCISSORS and computer_choice == Choice.PAPER):
        return "player"
    elif player_choice == computer_choice:
        return "tie"
    else:
        return "computer"

def main():
    player_score = 0
    computer_score = 0
    rounds_played = 0

    while True:
        print("\nRock, Paper, Scissors - Shoot!")
        player_choice = get_player_choice()
        computer_choice = random.choice(list(Choice))

        print(f"\nYou chose {get_choice_name(player_choice)}.")
        print(f"Python chose {get_choice_name(computer_choice)}.\n")

        winner = determine_winner(player_choice, computer_choice)

        if winner == "player":
            print("You win this round!")
            player_score += 1
        elif winner == "computer":
            print("Python wins this round!")
            computer_score += 1
        else:
            print("It's a tie!")

        rounds_played += 1

        print(f"\nScores: Player {player_score} - Python {computer_score}")
        print(f"Rounds played: {rounds_played}")

        play_again = input("Do you want to play again? (yes/no): ").strip().lower()
        if play_again != "yes":
            break

    print("\nThanks for playing! Final scores:")
    print(f"Player: {player_score}")
    print(f"Python: {computer_score}")

if __name__ == "__main__":
    main()
