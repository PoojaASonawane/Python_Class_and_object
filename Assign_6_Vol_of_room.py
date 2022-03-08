""" 6. Create a class “Room” which will hold the “height”, “width” and
“breadth” of the room in three fields(variables). This class also has
a method “volume()” to calculate the volume of this room."""

class Room:
    def __init__(self,h,w,b):
        self.height=h
        self.width=w
        self.breadth=b
        self.v=0
    def calVol(self):
        self.v=self.height*self.width*self.breadth
        print("Volume of this room is: ",self.v)
o1=Room(5,6,4)
o1.calVol()