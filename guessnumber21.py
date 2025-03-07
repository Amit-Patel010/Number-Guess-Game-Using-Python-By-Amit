import random

def guessing_game():

    user_name = input("What's your name? ")
    print(f"Hello {user_name}, we are going to play a game!")
    print("I am thinking of a number between 1 and 100, and you have only 5 guesses to figure it out.")

    number_to_guess = random.randint(1, 100)
    attempts = 0
    max_attempts = 5

    while attempts < max_attempts:
        try:
            guess = int(input(f"Attempt {attempts + 1}/{max_attempts}: Guess a number between 1 and 100: "))
            attempts += 1

            if guess < 1 or guess > 100:
                print("Please guess a number between 1 and 100.")
            elif guess < number_to_guess:
                print("Too low! Try a higher number.")
            elif guess > number_to_guess:
                print("Too high! Try a lower number.")
            else:
                print(f"Congratulations {user_name}! You guessed the correct number {number_to_guess} in {attempts} attempts.")
                break
        except ValueError:
            print("Invalid input! Please enter a valid number.")

    if attempts == max_attempts and guess != number_to_guess:
        print(f"Sorry {user_name}, you didn't guess the number. The correct number was {number_to_guess}.")

    play_again = input("Do you want to play again? (yes/no): ").strip().lower()
    if play_again == "yes":
        guessing_game()
    else:
        print("Thanks for playing! Goodbye!")

if __name__ == "__main__":
    guessing_game()
