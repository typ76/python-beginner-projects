import random

options = ("rock", "paper", "scissors")
score = 0

while True:
    player = input("Rock, Paper, Scissors (q to quit): ").lower()
    if player == "q":
        break
    computer = random.choice(options)

    while player not in options:
        print("Ivalid choice")
        player = input("Rock, paper, or scissors: ").lower()
        if player == "q":
            break
    if player == "q":
        break
    if player == computer:
        print("It's a tie")
    elif player == "rock" and computer == "paper":
        score -= 1
        print("You lost!")
    elif player == "rock" and computer == "scissors":
        score += 1
        print("You won!")
    elif player == "paper" and computer == "rock":
        score += 1
        print("You won!")
    elif player == "paper" and computer == "scissors":
        score -= 1
        print("You lost!")
    elif player == "scissors" and computer == "rock":
        score -= 1
        print("You lost!")
    elif player == "scissors" and computer == "paper":
        score += 1
        print("You won!")



    print("---------------------------")
    print(f"Computer chose: {computer}")
    print(f"Player chose: {player}")
    print(f"Current score: {score}")
    print("---------------------------")




print("Thanks for playing")
print(f"Total score: {score}")