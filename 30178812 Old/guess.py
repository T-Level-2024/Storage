import random
mynumber = random.randint(1, 100)
while True:
    guess = int(input("Guess the number: "))
    if guess < mynumber:
        print("Higher")
    elif guess == mynumber:
        print("That's it!")
        break
    elif guess > mynumber:
        print("Lower")

