# Think of a class as a blueprint or a template or a plan

# Think of an object like something in the real world.

class Dog:
#     Think of __init__ as the "initialization" function for objects.
#     It's a special method that gets called automatically when you create a new object from a class.
#    __init__ is used to set up or initialize the attributes (characteristics) of an object.
#     It allows you to pass values to the object when you create it.
    def __init__(self, name, breed):
        self.name = name
        breed = 100
# In this example, when you create a Dog object, you pass the name and breed 
# as arguments, and __init__ sets these values as attributes for the object.

    def bark(self):
        return "Woof!"
    
    


dog1 = Dog("Buddy", "Golden Retriever")
dog2 = Dog("Max", "Labrador")

print(dog1.bark())  # Output: "Woof!"
print(dog2.bark())  # Output: "Woof!"


# So, in simple terms:

#     A class is like a plan for making objects.
#     Objects are like real things you can create from those plans.


