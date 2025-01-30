#User inputs
number = float(input("Enter temperature: "))
scale = input("Enter a scale: ")
convert = input("And to convert it to what scale: ")

#Deciding what to convert it from
if scale == "K":
    #Converting from Kelvin
    if convert == "C":
        number = number - 273.15
    elif convert == "F":
        number = (number-273.15) * (9/5) + 32
elif scale == "F":
    #Converting from Fahrenheit
    if convert == "K":
        number = (number-32) * (5/9) + 273.15
    elif convert == "C":
        number = (number-32) * (5/9)
elif scale == "C":
    #Converting from Celsius
    if convert == "K":
        number = number + 273.15
    elif convert == "F":
        number = (number*(9/5)) + 32

#Prints the output to the screen
print(number)
