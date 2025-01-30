from random import choice
user = input("Rock, paper or scissors?: ")
computer = choice(["Rock", "Paper", "Scissors"])
if user == ("Rock" or "rock"):
    if computer == "Rock":
        print("Draw!")
    elif computer == "Paper":
        print("Computer wins!")
    elif computer == "Scissors":
        print("You win!")
elif user == ("Paper" or "paper"):
    if computer == "Rock":
        print("You win!")
    elif computer == "Paper":
        print("Draw!")
    elif computer == "Scissors":
        print("Computer wins!")
elif user == ("Scissors" or "Scissors"):
    if computer == "Rock":
        print("Computer wins!")
    elif computer == "Paper":
        print("You win!")
    elif computer == "Scissors":
        print("Draw!")
else:
    print("Bad input.")
