#Farhan Nawaz - Gamil (farhannwazofficial@gmail.com) - ID (22569) - GitHub (farhannawaz14)

import random

def number_guessing_game():
    # Function to play the Number Guessing Game

    # Load the high score from the file
    def load_high_score():
        try:
            with open("hiscore.txt", "r") as file:
                return int(file.read())
        except FileNotFoundError:
            return float('inf')

    # Save the high score to the file
    def save_high_score(score):
        with open("hiscore.txt", "w") as file:
            file.write(str(score))

    print("Welcome to the Number Guessing Game!")
    
    # Generate a random number between 1 and 100
    secret_number = random.randint(1, 100)
    
    # Initialize variables
    attempts = 0
    high_score = load_high_score()

    while True:
        # Get user input for the guess
        try:
            guess = int(input("Enter your guess (1-100): "))
        except ValueError:
            print("Invalid input. Please enter a number.")
            continue

        # Increment the number of attempts
        attempts += 1

        # Check if the guess is correct
        if guess == secret_number:
            print(f"Congratulations! You guessed the correct number in {attempts} attempts.")

            # Check and update high score
            if attempts < high_score:
                print("New High Score!")
                save_high_score(attempts)
            else:
                print(f"The current High Score is {high_score}.")

            break
        else:
            # Provide hints for incorrect guesses
            if guess < secret_number:
                print("Too low. Try again.")
            else:
                print("Too high. Try again.")

    print("Thanks for playing!")

# Run the game
number_guessing_game()
