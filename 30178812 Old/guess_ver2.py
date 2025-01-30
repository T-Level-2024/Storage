import random
numbers = input("Enter a range: ").split("-")
mynumber, guesses = random.randint(int(numbers[0]), int(numbers[1])), 0
while True:
    guess = int(input("Guess the number: "))
    if not int(numbers[0]) <= guess <= int(numbers[1]):
        print("Out of range")
        continue
    else:
        guesses+=1
    if guess < mynumber:
        print("Higher")
    elif guess == mynumber:
        print("That's it! You guessed "+str(guesses)+" times.")
        break
    elif guess > mynumber:
        print("Lower")

