import random
def guessing_game():
   
    number_to_guess = random.randint(1, 100)
    attempts = 0
    guessed = False

    print("Welcome to the Number Guessing Game!")
    print("I have selected a number between 1 and 100. Try to guess it!")

    while not guessed:
        try:
          
            user_guess = int(input("Enter your guess: "))
            attempts += 1
            if user_guess < number_to_guess:
                print("Too low! Try again.")
            elif user_guess > number_to_guess:
                print("Too high! Try again.")
            else:
                print(f"Congratulations! You guessed the correct number in {attempts} attempts.")
                guessed = True
        except ValueError:
            print("Please enter a valid number.")


guessing_game()