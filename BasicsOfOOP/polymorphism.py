class Shapes:
    def __init__(self):
      self.side=0

    def calcArea(self):
        pass

class Rectangle(Shapes):
    def __init__(self,length,width):
        self.length=length
        self.width=width
        self.side=4



    def calcArea(self):
        return (self.length * self.width)

class Circle(Shapes):
    def __init__(self,radius):
        self.radius=radius
        self.side=0
    def calcArea(self):
        return (3.14 * self.radius * self.radius)



obj=[Rectangle(4,5),Circle(7)]
print(obj[0].side)
print(obj[1].side)
print(obj[0].calcArea())
print(obj[1].calcArea())













