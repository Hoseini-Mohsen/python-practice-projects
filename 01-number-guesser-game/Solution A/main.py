import random

def get_user_guess():
    guess = input("Guess a number between 1 and 100: ")
    if guess.lower() == 'exit':
        print("You have exited the game!")
        exit()
    elif guess.lower() != 'exit' and not guess.isdigit():
        raise ValueError("Invalid input. Please enter a number between 1 and 100 or type 'exit' to quit.")
    elif int(guess) > 100 or int(guess) < 1:
        raise ValueError("Invalid input. Please enter a number between 1 and 100.")
    else:
        return int(guess)

def analyst(guess, correct_guess, score, iterations):
    if guess < correct_guess:
        print("Too low! Try again.")
        score -= 5
        if abs(guess - correct_guess) <= 5:
            score += 15
        elif abs(guess - correct_guess) <= 10:
            score += 10

    elif guess > correct_guess:
        print("Too high! Try again.")
        score -= 5
        if abs(guess - correct_guess) <= 5:
            score += 15
        elif abs(guess - correct_guess) <= 10:
            score += 10

    else:
        if iterations == 1:
            score += 100
        elif iterations == 2:
            score += 80
        else:
            guess_gif = max(0, 80 - (iterations - 2) * 5)
            score += guess_gif

        print("Greeting! You guessed the correct number!")
        print(f"Your score is: {score}")
        exit()

    return score

def play_game():
    # Welcome message and instructions
    print("Welcome to the Number Guesser Game!")
    print("if you want to exit the game, type 'exit'.")

    correct_guess = random.randint(1, 100)
    score = 200
    iterations = 0

    while True:
        guess = get_user_guess()
        iterations += 1
        score = analyst(guess, correct_guess, score, iterations)

if __name__ == "__main__":
    play_game()