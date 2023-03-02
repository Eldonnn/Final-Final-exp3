
import random

# generate a random integer between 1 and 100
random_number = random.randint(1, 100)

# set the maximum number of chances
max_chances = 10

# loop for the user's guesses
for i in range(max_chances):
    # get the user's guess
    guess = int(input("Guess the number (between 1 and 100): "))

    # check if the guess is correct
    if guess == random_number:
        print(f"Congratulations! You guessed the number in {i+1} tries.")
        break
    # check if the guess is too low
    elif guess < random_number:
        print("Your guess is too low. Try again.")
    # check if the guess is too high
    else:
        print("Your guess is too high. Try again.")

# if the user has used all their chances and did not guess the number
else:
    print(f"Sorry, you did not guess the number in {max_chances} tries.")
    print(f"The correct number was {random_number}.")
