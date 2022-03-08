""" 7. Write a program to implement a class “student” with the following members.
Name of the student. Marks of the student obtained in three subjects. Function to
assign initial values. Function to compute total average. Function to display the
student’s name and the total marks. Write an appropriate main() function to demonstrate
the functioning of the above."""

class Student:
    def __init__(self,name,math,history,physics):
        self.n=name
        self.m=math
        self.h=history
        self.p=physics
        # self.avg=0
        # self.marks=0
    def total_Avg(self):
        self.avg=(self.m+self.h+self.p)//3
        print("Average is: ",self.avg)
        self.marks=self.m+self.h+self.p
        print("Total marks: ",self.marks)


    def show(self):
        print("Student information".center(50,'*'))
        print("Name of the student",self.n)
        print("Total Marks",self.marks)

        print("**********************************".center(50, '*'))

s1=Student("pooja",80,90,100)
s1.total_Avg()
s1.show()