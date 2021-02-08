from abc import ABC, abstractmethod
class Shape(ABC):
    @abstractmethod
    def printarea(self):
        return 0

class Rectangle(Shape):
    type = "rectangle"
    sides = 4
    def __init__(self):
        self.length = 3
        self.breadth = 4
        #removing this printarea method will give error as it is defined as abstractmethod
    def printarea(self):
        print(self.length*self.breadth)

rect1 = Rectangle()
rect1.printarea()
#this will give an error as method of abstract class cannot be made
# try = Shape()