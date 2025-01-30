import json
class BankAccount:
    def __init__(self, a_n, a_h):
        try:
            with open("data.json", "r") as file:
                file = file.readlines()
        except FileNotFoundError:
            with open("data.json", "x"):
                pass
            self.a_n, self.a_h, self.bal, self.history = a_n, a_h, 0, []
        else:
            new = []
            for item in file: new.append(item)
            for i in range(len(new)): new[i] = json.loads(new[i])
            try:
                self.a_n, self.a_h, self.bal, self.history = a_n, a_h, new[0][str(a_n)][0], new[0][str(a_n)][1]
            except Exception:
                self.a_n, self.a_h, self.bal, self.history = a_n, a_h, 0, []
            del file, new
        del a_n, a_h

    def deposit(self, num):
        self.bal += num
        self.history.append("Deposit: "+str(num))

    def withdraw(self, num):
        if self.bal >= num:
            self.bal -= num
            self.history.append("Withdrawal: "+str(num))
        else:
            return "Overdrafts are not authorised for this account"
while True:
    try:
        account, user = BankAccount(int(input("Enter account number: ")), str(input("Enter account holder's name: "))), False
    except TypeError:
        print("Invalid input")
    else:
        break

while True:
    print(account.a_h+", ID: "+"*"*(len(str(account.a_n))-2)+str(account.a_n)[-2]+str(account.a_n)[-1]+"\n"
          "\n"
          "Deposit"+"\n"
          "Withdraw"+"\n"
          "Check balance"+"\n"
          "Transaction history"+"\n"
          "Log out"+"\n")
    user = False
    while user != True:
        user = input()
        if user.upper() == "DEPOSIT":
            print("How much would you like to deposit?: ")
            while True:
                user = input()
                try:
                    user = int(user)
                except TypeError:
                    print("Invalid amount")
                else:
                    account.deposit(user)
                    user = True
                    break
        elif user.upper() == "WITHDRAW":
            print("How much would you like to withdraw?: ")
            while True:
                user = input()
                try:
                    user = int(user)
                except TypeError:
                    print("Invalid amount")
                else:
                    account.withdraw(user)
                    user = True
                    break
        elif user.upper() == "CHECK BALANCE":
            print("Current balance: "+str(account.bal))
        elif user.upper() == "TRANSACTION HISTORY":
            print("Transaction history for "+account.a_h+":\n")
            for item in account.history: print(item)
        elif user.upper() == "LOG OUT":
            with open("data.json", "w") as file:
                data = {str(account.a_n):[account.bal, account.history]}
                file.writelines(json.dumps(data))
            raise KeyboardInterrupt
        continue
 
