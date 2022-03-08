class Circle:
    def __init__(self,x=1.2):
        self.r = x
        self.a = 0

    def calculateArea(self):
        self.a = self.r ** 2 * 3.14
        print('Area is', self.a)
t1=Circle()
t1.calculateArea()
t2=Circle(3.4)
t2.calculateArea()