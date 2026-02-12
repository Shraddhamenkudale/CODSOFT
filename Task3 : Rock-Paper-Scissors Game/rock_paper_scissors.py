# Rock Paper Scissors Game

import random
user_score = 0
computer_score = 0

choices = ["rock", "paper", "scissors"]
while True:
    print("\n--- Rock Paper Scissors Game ---")
    print("Choose one: rock, paper, scissors")

    user_choice = input("Your choice: ").lower()

    if user_choice not in choices:
        print("Invalid choice. Please choose rock, paper, or scissors.")
        continue

    computer_choice = random.choice(choices)

    print("Computer chose:", computer_choice)

    if user_choice == computer_choice:
        print("It's a tie!")
    elif (
        (user_choice == "rock" and computer_choice == "scissors") or
        (user_choice == "scissors" and computer_choice == "paper") or
        (user_choice == "paper" and computer_choice == "rock")
    ):
        print("You win this round!")
        user_score += 1
    else:
        print("Computer wins this round!")
        computer_score += 1

    print("Score -> You:", user_score, "| Computer:", computer_score)

    play_again = input("Do you want to play again? (yes/no): ").lower()
    if play_again != "yes":
        print("Game over. Thanks for playing!")
        break
