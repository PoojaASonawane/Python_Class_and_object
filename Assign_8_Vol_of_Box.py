""" 8. Write a class “Box” that with three member-variables “height”, “width”
and “breadth”. Write suitable constructors to initialize them. Add functions
like “getVolume” and “getArea” that will return volume and surface area respectively.
Create object of boxes and then print their volume and surface area."""

class Box:
    def __init__(self,h,w,b):
        self.height = h
        self.width = w
        self.breadth = b
        self.v = 0
        self.a = 0
    def getVolume(self):
        self.v=self.height*self.width*self.breadth
        return self.v
    def getArea(self):
        self.a=2*(self.height*self.breadth+self.breadth*self.width+self.width*self.height)
        return self.a
o1=Box(5,6,4)
area=o1.getArea()
volume=o1.getVolume()
print("Volume is: ",volume)
print("Area is: ",area)