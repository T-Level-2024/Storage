print("1. Add task\n"
      "2. Edit a task\n"
      "3. Remove a task\n"
      "4. List tasks\n")
while True:
    x = input("Enter input: ")
    match x:
        case "1":
            print("Added task")
            break
        case "2":
            print("Edited task")
            break
        case "3":
            print("Removed task")
            break
        case "4":
            print("Listed tasks")
            break
        
