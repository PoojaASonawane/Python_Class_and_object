""" 3. Create classes that capture bank customers and bank accounts.
A customer has a first and last name. An account has a customer and a balance.
Make objects for two accounts held by the same customer."""
"""
class Customer:
    def __init__(self,f,l,b):
        self.fname=f
        self.lname=l
        self.balance = b
    def display(self):
        self.name=self.fname+self.lname

        print("Account holder name", self.name)
        print("Account balance", self.balance)


c1=Customer("pooja","sonawane",30000)
c2=Customer("pooja","sonawane",50000)
c1.display()
c2.display()
"""
class Customer:
    def __init__(self,fname,lname):
        self.f=fname
        self.l=lname
    def display(self):
        self.name=self.f+" "+self.l
        print("Customer Name: ", self.name)
        print("Account Details: ".center(50, "*"))
class Account:
    i=0
    def __init__(self,balance):
        Account.i+=1
        self.b=balance
    def print(self):
        # print("Account Details: ".center(50,"*"))
        print("Account",Account.i,"Balance: ",self.b)
o1=Customer("pooja","sonawane")
c1=o1.display()
o2=Account(30000)
o2.print()
o2=Account(50000)
o2.print()
