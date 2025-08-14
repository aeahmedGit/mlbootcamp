import random


# List of possible plays
options = ["rock", "paper", "scissors"]

# Computer randomly chooses a play
computer_choice = random.choice(options)

# Player input
player_choice = input("Enter rock, paper, or scissors: ").lower()

# Check if input is valid
if player_choice not in options:
    print("Error: Invalid choice. Please enter 'rock', 'paper', or 'scissors'.")
else:
    print(f"Computer chose: {computer_choice}")
    print(f"You chose: {player_choice}")

    # Compare choices and determine winner
    if player_choice == computer_choice:
        print("It's a tie!")
    elif (player_choice == "rock" and computer_choice == "scissors") or \
         (player_choice == "paper" and computer_choice == "rock") or \
         (player_choice == "scissors" and computer_choice == "paper"):
        print("You win!")
    else:
        print("You lose!")