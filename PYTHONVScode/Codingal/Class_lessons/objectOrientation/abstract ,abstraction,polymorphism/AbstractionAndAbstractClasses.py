# 1. Abstraction:

# Abstraction is the process of simplifying complex reality by modeling classes based on the essential 
# attributes and behaviors of objects. 

# It allows you to hide the complex implementation details and expose only what's necessary for the user.

# Example:
# 
# Imagine you're designing a TV remote. Users don't need to know how the remote works internally; they only 
# need to know how to use the buttons. This simplification of the complex internals is abstraction.

#protocols:
# 1. Abstract classes are classes that cannot be instantiated.
# 2. they are designed to be base class for other classes.
# 3. Abstract classes define a common interface, which derived classes must implement. They often contain
#    abstract methods (methods without a body) that must be defined in the derived classes.

from abc import ABC, abstractmethod

class Shape(ABC):
    @abstractmethod
    def area(self):
        pass

class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius
    def area(self):
        return 3.14 * self.radius ** 2
    
# You can't create an object of Shape directly, but you can create objects of Circle and Rectangle.

# POLYMORPHISM: having many forms.
# Polymorphism is the ability of different classes to be treated as instances of the same class.

# Using the Shape abstract class example, polymorphism allows you to call the area() method on both 
# Circle and Rectangle objects, even though their implementations are different.

# Create objects
circle = Circle(5)
# rectangle = Rectangle(4, 6)

# Calculate areas
print("Circle Area:", circle.area())       # Output: Circle Area: 78.5
# print("Rectangle Area:", rectangle.area()) # Output: Rectangle Area: 24

# In this example, both Circle and Rectangle are treated as instances of the Shape class because
#  they share a common method interface (area()), allowing you to use polymorphism to calculate their areas.

# types: duck typyng, meth overloading/overriding, operator overloading


