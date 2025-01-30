tasks = []
while True:
    print("1. Add task\n"
          "2. Edit a task\n"
          "3. Remove a task\n"
          "4. List tasks\n"
          "5. Exit\n")
    while True:
        x = input("Enter input: ")
        match x:
            case "1":
                while True:
                    x = input("Enter task to add: ")
                    if x.strip() != "":
                        tasks.append(x.strip())
                        break
                    else:
                        print("Invalid task name: "+str(x))
            case "2":
                b=False
                while b==False:
                    x = input("Enter task to edit: ")
                    for i in range(len(tasks)):
                        if tasks[i] == x:
                            new_name = input("Enter new name for task: ")
                            if new_name.strip() != "":
                                tasks[i] = new_name
                                b=True
                                break
                            else:
                                print("Invalid task name: ")
                    else:
                        print("No such task")
                    continue
                print("Edited task")
            case "3":
                x = input("Enter task to remove: ")
                for i in range(len(tasks)):
                    if tasks[i] == x:
                        tasks.pop(i)
                        break
                else:
                    print("No such task")
            case "4":
                print("Tasks: ")
                for item in tasks:
                    print(item)
            case "5":
                break
        
