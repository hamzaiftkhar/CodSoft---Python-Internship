import random

def determine_winner(user_choice, computer_choice):
    if user_choice == computer_choice:
        return "It's a tie!", 0, 0
    elif (
        (user_choice == "rock" and computer_choice == "scissors") or
        (user_choice == "scissors" and computer_choice == "paper") or
        (user_choice == "paper" and computer_choice == "rock")
    ):
        return "You win!", 1, 0
    else:
        return "Computer wins!", 0, 1

def main():
    user_score = 0
    computer_score = 0
    
    print("Welcome to Rock-Paper-Scissors Game!")

    while True:
        print("\nChoose: rock, paper, or scissors (or 'quit' to exit)")
        user_choice = input("Your choice: ").lower()

        if user_choice == 'quit':
            break

        if user_choice not in ["rock", "paper", "scissors"]:
            print("Invalid choice. Please choose 'rock', 'paper', or 'scissors'.")
            continue

        computer_choice = random.choice(["rock", "paper", "scissors"])
        
        result, user_increment, computer_increment = determine_winner(user_choice, computer_choice)
        user_score += user_increment
        computer_score += computer_increment

        print(f"\nYou chose: {user_choice}")
        print(f"Computer chose: {computer_choice}")
        print(result)
        print(f"Your Score: {user_score}, Computer Score: {computer_score}")

    print("\nThanks for playing!")

if __name__ == "__main__":
    main()
