# Prompt the user to enter a number
number = float(input("Enter a number: "))

# Check if the number is positive, negative, or zero
match number:
    case 0: print("The number is zero.")
    case x if x > 0: print("The number is positive.")
    case y if y < 0: print("The number is negative.")
    case _: print("Unexpected case! Something went wrong.")
