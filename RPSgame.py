import random

# computer's choice
def computer__choice():
    choices = ["rock", "paper", "scissors"]
    return random.choice(choices)

# Determine the winner of the round
def winner(you_choice, computer_choice):
    if you_choice == computer_choice:
        return "It's a tie!"
    elif you_choice == "rock" and computer_choice == "scissors":
        return "You win! Rock beats Scissors."
    elif you_choice == "scissors" and computer_choice == "paper":
        return "You win! Scissors beat Paper."
    elif you_choice == "paper" and computer_choice == "rock":
        return "You win! Paper beats Rock."
    else:
        return "Computer wins!"

# game function
def game():
    print("Let's play Rock, Paper, Scissors!")
    
    while True:
        # Ask the user for their choice
        you_choice = input("Enter rock, paper, or scissors (or 'quit' to stop): ").lower()
        
        if you_choice == "quit":
            print("Thanks for playing!")
            break
        
        if you_choice not in ["rock", "paper", "scissors"]:
            print("Invalid choice! Try again.")
            continue
        
        # Get the computer's choice
        computer_choice = computer__choice()
        print(f"Computer chose: {computer_choice}")
        
        # who won
        result = winner(you_choice, computer_choice)
        print(result)

# Start the game
game()