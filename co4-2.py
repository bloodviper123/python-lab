#co4-2

class bank:
    def __init__(self, acc_no, name, acc_type, balance):
        self.acc_no = acc_no
        self.name = name
        self.acc_type = acc_type
        self.balance = balance
    def deposit(self):
        amount = float(input("Enter amount to be deposited: "))
        self.balance = self.balance + amount
        print("Amount deposited:", amount)
        print("Current balance:", self.balance)
    def withdraw(self):
        amount = float(input("Enter amount to be withdrawn: "))
        if amount <= self.balance:
            self.balance = self.balance - amount
            print("Amount withdrawn:", amount)
            print("Current balance:", self.balance)
        else:
            print("Insufficient balance!")
    def display(self):
        print("\nAccount number:", self.acc_no)
        print("Account holder:", self.name)
        print("ACC type:", self.acc_type)
        print("Balance:", self.balance)

acc_no = int(input("Enter account number: "))
name = input("Enter name: ")
acc_type = input("Enter account type: ")
balance = float(input("Enter initial balance: "))

obj = bank(acc_no, name, acc_type, balance)

while True:
    print("\n1. Deposit")
    print("2. Withdraw")
    print("3. Display")
    print("4. Exit")

    ch = int(input("Enter your choice: "))

    if ch == 1:
        obj.deposit()
    elif ch == 2:
        obj.withdraw()
    elif ch == 3:
        obj.display()
    elif ch == 4:
        print("Thank you for using our bank!")
        break
    else:
        print("Invalid choice!")


        