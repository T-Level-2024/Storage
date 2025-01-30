path = input("Enter file path: ")
with open(path) as file:
    contents = file.readlines()
    for item in contents:
        print(item)
