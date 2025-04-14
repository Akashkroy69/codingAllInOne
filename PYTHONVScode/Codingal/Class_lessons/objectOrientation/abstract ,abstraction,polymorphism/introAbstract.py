from abc import ABC, abstractmethod

class Animal(ABC):
    @abstractmethod
    def sound(self):
        pass

class Dog(Animal):
   
   def m1(self):
         print("Dog barks")

   def sound(self):
        return "Woof!"


dog = Dog()

dog.m1()  # Output: Dog barks