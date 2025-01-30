def ATM():
    balance = int(input("What is your balance?: "))
    amount = int(input("How much do you wish to withdraw?: "))
    return print(balance-amount) if (balance-amount)>=0 else print("Not sufficient")
ATM()
