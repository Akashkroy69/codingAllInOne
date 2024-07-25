# Encapsulation is one of the fundamental principles of object-oriented programming (OOP) and 
# involves bundling the data (attributes) and the methods (functions) that operate on the data into 
# a single unit, known as a class. The concept of encapsulation helps in hiding the internal state of 
# an object and restricting direct access to some of its components. It promotes data hiding, abstraction,
#  and modularity.

# Here's a simple example in Python to illustrate encapsulation:


class Car:
    def __init__(self, make, model, year):
        self.__make = make  # Private attribute
        self.__model = model  # Private attribute
        self.__year = year  # Private attribute
        self.__is_engine_on = False  # Private attribute

    # Public method to start the engine
    def start_engine(self):
        if not self.__is_engine_on:
            print("Engine starting...")
            self.__is_engine_on = True
        else:
            print("Engine is already running.")

    # Public method to stop the engine
    def stop_engine(self):
        if self.__is_engine_on:
            print("Engine stopping...")
            self.__is_engine_on = False
        else:
            print("Engine is already off.")

    # Public method to get the car information
    def get_car_info(self):
        return f"{self.__year} {self.__make} {self.__model}, Engine Status: {'On' if self.__is_engine_on else 'Off'}"


# Creating an instance of the Car class
my_car = Car(make="Toyota", model="Camry", year=2022)

# Accessing public methods to interact with the object
my_car.start_engine()
my_car.stop_engine()

# Accessing a private attribute directly (will result in an error)
# print(my_car.__make)  # Uncommenting this line will raise an AttributeError

# Accessing information through a public method
print(my_car.get_car_info())

# In this example:

# - The class `Car` has private attributes (`__make`, `__model`, `__year`, and `__is_engine_on`) denoted by
#  the double underscores (`__`). These attributes are not intended to be accessed directly from outside the class.

# - Public methods (`start_engine`, `stop_engine`, and `get_car_info`) provide controlled access to the 
# private attributes. These methods encapsulate the internal workings of the class.

# - Attempting to access a private attribute directly from outside the class 
# (e.g., `my_car.__make`) will result in an `AttributeError`. This demonstrates encapsulation by preventing direct access to internal details.

# Encapsulation is beneficial because it allows the internal implementation of a class to change without
#  affecting the code that uses the class. It provides a clear interface for interacting with objects while
#  hiding the complexity of their implementation.