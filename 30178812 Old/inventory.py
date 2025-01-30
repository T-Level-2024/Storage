import sys
def inventory():
    try:
        logbook = open("logbook.json", "r+")
        logbooktemp, logbook = logbook.readlines(),  []
        for i in range(len(logbooktemp)-3):
            TEMP0 = logbooktemp[i+3].split("-")
            TEMP0, TEMP1 = TEMP0[0].strip(), int(TEMP0[1].split("units")[0])
            logbook.append({"name":TEMP0, "quantity":TEMP1})
    except FileNotFoundError:
        with open("logbook.json", "x") as logbook:
            logbook.writelines(["Inventory Management System:\n", "0 items\n", "\n"])
        logbook = []
    while True:
        print("Inventory Management System:\n"
              "1. Add Item\n"
              "2. View Inventory\n"
              "3. Edit Item\n"
              "4. Remove Item\n"
              "5. Exit\n")
        while True:
            user = input()
            if user == "1":
                while True:
                    try:
                        user = input("Enter item name:")
                        if user.strip() != "":
                            name = user.strip()
                            while True:
                                user = input("Enter quantity:")
                                try:
                                    if int(user) > 0:
                                        quantity = int(user)
                                        logbook.append({"name":name, "quantity":quantity})
                                        del name, quantity
                                except TypeError:
                                    pass
                                else:
                                    break
                            break
                    except KeyboardInterrupt:
                        break
                break
            elif user == "2":
                print("Current Inventory:\n"+
                      str(len(logbook))+" items\n")
                for item in logbook:
                    print(item["name"]+" - "+str(item["quantity"]))
                break
            elif user == "3":
                while True:
                    try:
                        user = name = input("Enter item name: ")
                        if user.strip() != "":
                            for item in logbook:
                                if name == item["name"]:
                                    break
                            else:
                                print("Item not found")
                                continue
                            while True:
                                user = input("Change item name or quantity?: ")
                                if user.strip().upper() == "ITEM NAME":
                                    while True:
                                        user = input("Enter new item name:")
                                        if user.strip() != "":
                                            for item in logbook:
                                                if name == item["name"]:
                                                    item["name"] = user.strip()
                                                    break
                                    break
                                if user.strip().upper() == "QUANTITY":
                                    while True:
                                        try:
                                            user = int(input("Enter new quantity: "))
                                        except TypeError:
                                            pass
                                        for item in logbook:
                                            if name == item["name"]:
                                                item["quantity"] = user
                                                break
                                        break
                                    break
                            break
                    except KeyboardInterrupt:
                        break
            elif user == "4":
                while True:
                    try:
                        user = input("Enter item name:")
                        if user.strip() != "":
                            TEMP0 = 0
                            for item in logbook:
                                if item["name"] == user.strip():
                                    print("Removed "+item["name"])
                                    logbook.pop(TEMP0)
                                    break
                                TEMP0 += 1
                            else:
                                print("Item not found")
                                continue
                            break
                    except KeyboardInterrupt:
                        break
            elif user == "5":
                if len(logbook) == 0:
                    with open("logbook.json", "w") as logbookIO:
                        logbookIO.writelines(["Inventory Management System:\n", "0 items\n" "\n"])
                else:
                    with open("logbook.json", "w") as logbookIO:
                        logbookIO.writelines(["Inventory Management System:\n", str(len(logbook))+" items\n", "\n"])
                        for item in logbook:
                            logbookIO.write(item["name"]+" - "+str(item["quantity"])+" units\n")
                sys.exit("Exited.")
          
    

inventory()
