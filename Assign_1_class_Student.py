#1. Create a class that captures students. Each student has a first name, last name,
# class year, and major.  Create two examples of students.

class Student:
    def __init__(self):
        self.fname=input("Enter first name.")
        self.lname=input("Enter last name:")
        self.year=int(input("Enter year"))

    def show(self):
        print("Student information".center(50,'*'))
        print("First name",self.fname)
        print("last name",self.lname)
        print("Class year",self.year)
        print("**********************************".center(50, '*'))

s1=Student()
s1.show()
s2=Student()
s2.show()