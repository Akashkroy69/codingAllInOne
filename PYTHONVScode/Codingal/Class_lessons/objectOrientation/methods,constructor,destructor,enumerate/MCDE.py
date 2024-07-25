# 1. Methods:

# What are Methods? Methods are like actions or behaviors that objects can perform. 
# They are functions defined inside a class that define what an object can do.
class Dog:
    def bark(self):
        return "Woof!"


# 2. Constructors:

#     What is a Constructor? A constructor is a special method called __init__. 
#     It's used to initialize an object when it's created from a class. It sets up the object's initial state.

#     Example:

class Dog:
    def __init__(self, name):
        self.name = name
    def __del__(self):
        print("del called, obj deleted")
# In this example, __init__ is the constructor. It initializes a Dog object with a name attribute.

# 3. Destructors:

#     What is a Destructor? Python doesn't have a built-in concept of destructors like some other languages do. 
#     Python automatically manages memory, so you don't 
#     typically need destructors. Objects are automatically destroyed when they're no longer in use.

#---------------------
# 4. enumerate Function:

#     What is enumerate? enumerate is a built-in Python function used for looping through sequences (like lists, tuples, or strings) while keeping track of the index (position) of the current item.

#     Example:
fruits = ["apple", "banana", "cherry"]
obF = enumerate(fruits)
for index, fruit in obF:
    print(f"Index {index}: {fruit}")

dogOb1 = Dog("BABA")

# del Dog
l1 = ["eat", "sleep", "repeat"]
s1 = "geek"

obj1 = enumerate(l1)
obj2 = enumerate(s1)
print ("Return type:", type(obj1))
print (list(enumerate(l1)))

# changing start index to 2 from 0
print (list(enumerate(s1, 2)))

# del dogOb1






