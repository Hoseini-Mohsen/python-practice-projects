import random


class RockPaperScissorsGame:
    def __init__(self):
        self.choices = ['rock', 'paper', 'scissors']
        self.user_score = 0
        self.computer_score = 0

    def get_user_choice(self):
        while True:
            user_input = input("Enter your choice (rock, paper, scissors) or 'exit' to quit: ").lower()
            if user_input == 'exit':
                print("You have exited the game!")
                exit()
            elif user_input not in self.choices:
                print("Invalid input. Please enter 'rock', 'paper', or 'scissors'.")
            else:
                return user_input

    def get_computer_choice(self):
        return random.choice(self.choices)

    def determine_winner(self, user_choice, computer_choice):
        if user_choice == computer_choice:
            print("It's a tie!")
        elif (user_choice == 'rock' and computer_choice == 'scissors') or \
             (user_choice == 'paper' and computer_choice == 'rock') or \
             (user_choice == 'scissors' and computer_choice == 'paper'):
            print("You win!")
            self.user_score += 1
        else:
            print("Computer wins!")
            self.computer_score += 1

def play_game():
    print("Welcome to the Rock-Paper-Scissors Game!")
    print("Type 'exit' to quit the game.")

    rps = RockPaperScissorsGame()
    while True:
        user_choice = rps.get_user_choice()
        computer_choice = rps.get_computer_choice()
        print(f"Computer chose: {computer_choice}")
        rps.determine_winner(user_choice, computer_choice)
        print(f"Score - You: {rps.user_score}, Computer: {rps.computer_score}")
        if rps.user_score == 3:
            print("Congratulations! You won the game!")
            break
        elif rps.computer_score == 3:
            print("Sorry! The computer won the game!")
            break

if __name__ == "__main__":
    play_game()