user_input = int(input("Enter a number (1-3): "))

#Combined Mistakes
match user_input:
    case 1: print("One")
    case 2: print("Two")
    case 3: print("Three")
    case _: print("Invalid input")
