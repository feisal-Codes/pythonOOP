from abc import ABC,abstractmethod as abs

"""
 
ABCs define a set of methods 
and properties that a class must implement 
in order to be considered a duck type instance 
of that class 

""" 

class Shape(ABC):

    @abs
    def area(self):
        pass
    @abs 
    def perimeter(self):
        pass


class Square(Shape):
    def __init__(self,side):
        self.side=side
    
    def area(self):
        return self.side * self.side
    
    def perimeter(self):
        return self.side * 4

sq=Square(5)
print(sq.area())
print(sq.perimeter())

















