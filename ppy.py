import random

number = random.randint(1, 100)
attempts = 0

print("Guess a number between 1 and 100!")

for attempts in range(1, 11):  # Give player 10 attempts
    guess = int(input(f"Attempt {attempts}: "))
    
    if guess < number:
        print("Too low!")
    elif guess > number:
        print("Too high!")
    else:
        print(f"Congratulations! You guessed it in {attempts} attempts!")
        break
else:
    print(f"Sorry, you're out of attempts. The number was {number}.")
