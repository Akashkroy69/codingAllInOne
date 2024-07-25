from abc import ABC, abstractmethod

# Abstract class for shapes
class Shape(ABC):
    @abstractmethod
    def area(self):
        pass

# Concrete class: Circle
class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        return 3.14 * self.radius**2

# Concrete class: Rectangle
class Rectangle(Shape):
    def __init(self, width, height):
        self.width = width
        self.height = height

    def area(self):
        return self.width * self.height

# List of shapes
shapes = [Circle(5), Rectangle(4, 6), Circle(3)]

# Tuple of dimensions
dimensions = ((3, 4), (1, 2), (5, 5))

# Set of unique names
names = {"Alice", "Bob", "Charlie", "Alice"}

# Dictionary of students
students = {
    "Alice": {"age": 16, "grade": "A"},
    "Bob": {"age": 17, "grade": "B"},
    "Charlie": {"age": 16, "grade": "A"},
}

# Polymorphism in action
for shape in shapes:
    print(f"Area of the shape: {shape.area()}")

# Accessing a tuple
print(f"Dimensions of the first object: {dimensions[0]}")

# Iterating through a set
print("Names of students:")
for name in names:
    print(name)

# Accessing dictionary values
print("Student Information:")
for student, info in students.items():
    print(f"{student}: Age {info['age']}, Grade {info['grade']}")
