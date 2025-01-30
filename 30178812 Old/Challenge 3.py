year = int(input("Enter year: "))
d4 = year/4
d100 = year/100
d400 = year/400
if not d4.is_integer():
    print("Not leap year")
elif d100.is_integer():
    if d400.is_integer():
        print("Leap year")
    else:
        print("Not leap year")
else:
    print("Leap year")
