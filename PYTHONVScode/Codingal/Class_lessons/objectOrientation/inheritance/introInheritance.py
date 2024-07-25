# Inheritance is a fundamental concept in object-oriented programming (OOP) 
# that allows you to create a new class (called a subclass or derived class) 
# by inheriting attributes and behaviors from an existing class
#  (called a superclass or base class)

# 1. Superclass and Subclass:

#     The superclass (or base class) is the class whose attributes and methods are inherited.
#     The subclass (or derived class) is the new class that inherits from the superclass.
#-----------------------------
# class Superclass:
#     # Superclass attributes and methods
#     print("this is super class")

# class Subclass(Superclass):
#     # Subclass attributes and methods
#     print("this is subclass")
#-----------------------------#
class Animal:
    def __init__(self, name, species):
        self.name = name
        self.species = species

    def speak(self):
        pass

class Dog(Animal):
    # pass
    def speak(self):
        return f"{self.name} the {self.species} says Woof!"
    def sleep(self,hours):
        self.hours = hours
        print(f"{self.name} sleeps {self.hours} hrs")

class Cat(Animal):
    def speak(self):
        return f"{self.name} the {self.species} says Meow!"

class Bird(Animal):
    def speak(self):
        return f"{self.name} the {self.species} says Chirp!"

# Create instances of different animals
dog = Dog("Buddy", "Dog")
cat = Cat("Whiskers", "Cat")
bird = Bird("Tweety", "Bird")

#testing
dog.sleep(8)
anim = Animal("A","cat")
anim.sleep()

# Put the animals in a list
zoo = [dog, cat, bird]

# Make the animals speak
for animal in zoo:
    print(animal.speak())
