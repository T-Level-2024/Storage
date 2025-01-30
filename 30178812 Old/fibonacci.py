time = int(input("How many numbers?: "))
reference = []
for time in range(0, time):
    try:
        fibonacci = reference[-1] + reference[-2]
        reference.append(fibonacci)
        print(fibonacci)
    except IndexError:
        reference.append(1)
        print(1)
