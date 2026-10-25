import random

answer = random.randint(1, 50)

guesses = 0

print("Welcome to the number guessing game!")

while True:
    guess = input(("Choose a number between 1 and 50: "))
    if guess.isdigit():
        guess = int(guess)
        guesses += 1

        if guess == answer:
            print("Correct!")
            break
        elif guess > 50:
            print("Out of range, too high!")
        elif guess > answer:
            print("Too high!")
        elif guess < 1:
            print("Out of range, too low!")
        elif guess < answer:
            print("Too low!")

    else:
        print("Invalid input")

print(f"You guessed {guesses} times!")
print("Thanks for playing!")