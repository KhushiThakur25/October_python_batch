try:
    def atm():
        total = 10000
        pin = input("Enter your PIN:")
        if pin == "1234":
            print("Login Successfully")
        else:
            raise ValueError("Login failed")
        amount = int(input("Enter the amount.."))
        if amount <= total:
            total -= amount
            print("Remaining amount is:",total)
        else:
            raise ValueError("Insufficient Balance..")

except ValueError as msg:
    print(msg)

atm()
