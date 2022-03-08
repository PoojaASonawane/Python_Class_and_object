""" 2. Create a class that captures planets. Each planet has a name, a distance from the sun,
and its gravity relative to Earth’s gravity. For distance and gravity, use the type double
which captures real numbers.
Make objects for Earth and your favorite non-earth planet. """

class Planet:
    def __init__(self,name,dis,gravity):
        self.pname=name
        self.distance=dis
        self.gravity=gravity

    def show(self):
        print("Planet Details".center(50,'*'))
        print("Planet name",self.pname)
        print("Distance",self.distance)
        print("Gravity",self.gravity)
        print("**********************************".center(50, '*'))

p1=Planet("Earth",300000,9.8)
p1.show()