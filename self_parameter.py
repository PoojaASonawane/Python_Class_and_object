class Circle:
    def __init__(self,x):
        self.r=x
        self.a=0
    def calculateArea(self):
        self.a=self.r**2*3.14
        print('Area is',self.a)
t1=Circle(1.2)
t2=Circle(3.4)
t1.calculateArea()
t2.calculateArea()
