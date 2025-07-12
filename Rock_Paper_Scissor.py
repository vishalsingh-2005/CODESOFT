import random

print("--------------------------------------------------")
print("**************************************************")
print("\t》》》ROCK PAPER SCISSOR GAME《《《")
print("**************************************************")
print("--------------------------------------------------\n")

def get_computer_choice():
    choices = ["rock", "paper", "scissor"]
    return random.choice(choices)

def determine_winner(user_choice, computer_choice):
    if user_choice == computer_choice:
        return "It's a tie!"
    elif (user_choice == "rock" and computer_choice == "scissor") or \
         (user_choice == "paper" and computer_choice == "rock") or \
         (user_choice == "scissor" and computer_choice == "paper"):
        return "You win!"
    else:
        return "You lose!"

def main():
    user_score = 0
    computer_score = 0
    play_again = "yes"

    while play_again.lower() == "yes":
        user_choice = input("Enter your choice (rock, paper, scissor): ").lower()

        while user_choice.lower() not in ["rock", "paper", "scissor"]:
            print("Invalid choice! Please choose rock, paper, or scissor.")
            user_choice = input("Enter your choice (rock, paper, scissor): ").lower()

        computer_choice = get_computer_choice()
        print(f"Computer chose: {computer_choice}")

        result = determine_winner(user_choice, computer_choice)
        print(result)

        if result == "You win!":
            user_score += 1
        elif result == "You lose!":
            computer_score += 1

        print(f"SCORE:\nYou :- {user_score}\tComputer:- {computer_score}")

        play_again = input("Do you want to play again? (yes/no): ").lower()
    
    if play_again not in ["yes", "no"]:
        print("Invalid input!")
    
    print("Thank you for playing! Goodbye!")

if __name__ == "__main__":
    main()