class Account:
    def __init__(self):
        self.id=input("Enter Account No.")
        self.name=input("Enter Account holder name:")
        self.balance=int(input("Enter Balance"))
    def deposit(self):
        x=int(input("Enter amount to deposit"))
        self.balance+=x
        print("Balance after deposit",self.balance)
    def withdraw(self):
        x=int(input("Enter amount to withdraw"))
        self.balance-=x
        print("Balance after withdraw",self.balance)
    def print(self):
        print("Account information".center(50,'*'))
        print("Account No",self.id)
        print("Account holder name",self.name)
        print("Account balance",self.balance)
c1=Account()
c1.deposit()
c1.print()
c1.withdraw()
c1.print()