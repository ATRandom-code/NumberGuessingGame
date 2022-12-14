# Import the random module to generate random numbers
import random

# Set the initial score to 0
score = 0

# Print the instructions for the game
print("Welcome to the number guessing game!")
print("I will think of a number between 1 and 10 and you have to guess it.")

# Generate a random number between 1 and 10
number = random.randint(1, 10)

# Start the game loop
while True:
  # Ask the player for their guess
  guess = int(input("Guess the number: "))

  # If the guess is correct, increase the score and generate a new random number
  if guess == number:
    score += 1
    print("Correct! Your score is now {}".format(score))
    number = random.randint(1, 10)

  # If the guess is incorrect, the game ends
  else:
    print("Sorry, that's not correct. The number was {}".format(number))
    print("Your final score is {}".format(score))
    break
