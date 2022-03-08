""" 5. Design a class ‘Complex ‘with data members for real and imaginary part.
Provide default and Parameterized constructors. Write a program to perform arithmetic operations
of two complex numbers."""

class Complex:
    def __init__(self,r,i):
        self.real=r
        self.imaginary=i
    def add(self):
        self.add=self.real+self.imaginary
        return self.add
        #print("Addition is ",self.add)
o1=Complex(2,3j)
o2=Complex(3,5j)
a=o1.add()
b=o2.add()
c=a+b
print(c)