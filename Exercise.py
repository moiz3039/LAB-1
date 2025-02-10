                                             # Guess the num Game.
import random

num_to_guess = random.randint(1, 100)

# Total attempts
max_attempts = 5

print('Welcome to the Guess the Number Game')
print(f'You have {max_attempts} attempts to guess it.')

# Use a for loop to give the player a limited number of guesses
for attempt in range(1, max_attempts + 1):
    guess = int(input(f"Attempt {attempt}: Enter your guess: "))
    
    if guess < num_to_guess:
        print("Too low! Try again.")
    elif guess > num_to_guess:
        print("Too high! Try again.")
    else:
        print(f"Correct! You've guessed the number in {attempt} attempts.")
        break
else:
    print(f"Sorry, you didn't guess the number. The correct number was {num_to_guess}.")
