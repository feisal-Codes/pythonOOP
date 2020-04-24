import math


class Point:
    def __init__(self):
        """initiatilizes object attributes on creation"""
        self.move()

    def move(self, x=0, y=0):
        """sets object attributes and makes it optional"""
        self.x = x
        self.y = y

    def reset(self):
        """resets the point values to zero"""
        self.move(0,0)
    def __str__(self):
        """prints a string representation of the point"""
        return '%d %d ' %(p1.x,p1.y)

    def distance(self,other):
        """calculates the distance between two point objects
           takes one object as self and the second object as other"""
        return math.sqrt((self.x - other.x )**2 + (self.y - other.y)**2)

p1=Point()
p2=Point()
p2.move(3,4)
print(p1.x,p1.y)
print(p2)
print(p2.distance(p1))
