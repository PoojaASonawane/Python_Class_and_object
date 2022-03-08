class Test:
    j=0
    def __init__(self,x):
        self.i=x          #instance variable
        Test.j+=1         #class variable
    def show(self):
        print(self.i,Test.j)
t1=Test(10)
t2=Test(20)
t3=Test(30)
t1.show()
t2.show()
t3.show()