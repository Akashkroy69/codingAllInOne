# In Python, there's a module called array that provides an alternative to using lists for creating arrays. 
# The array module allows you to work with arrays that are more memory-efficient and can contain elements 
# of the same data type.  Here's a basic introduction to using the array module:

# First, you need to import the array module to use it:
import array

# Creating an Array:

# To create an array using the array module, you need to specify the type code for the elements 
# it will contain. The type code determines the data type of the elements in the array. Common type codes include:

#     'i': Signed integer (e.g., array('i', [1, 2, 3]))
#     'f': Floating-point (e.g., array('f', [1.0, 2.0, 3.0]))
#     'd': Double-precision floating-point (e.g., array('d', [1.0, 2.0, 3.0]))
#     'l': Signed long (e.g., array('l', [1, 2, 3]))

# Creating an integer array
int_array = array.array('i', [1, 2, 3, 4, 5])
#buuferinfo, typecode

# Accessing elements
first_element = int_array[0]  # Retrieves the first element (1)
second_element = int_array[1]  # Retrieves the second element (2)
# Modifying elements
int_array[0] = 10  # Changes the first element to 10



# The array module provides various methods for working with arrays. Some common methods:

#     append(): Adds an element to the end of the array.
#     extend(): Appends elements from an iterable to the end of the array.
#     insert(): Inserts an element at a specified position.
#     remove(): Removes the first occurrence of a specified element.
#     pop(): Removes and returns the element at a specified position.
#     index(): Returns the index of the first occurrence of a specified element.
#     count(): Returns the number of occurrences of a specified element.
#     reverse(): Reverses the order of elements in the array.
#     tofile() and fromfile(): Write the array to a file or read an array from a file.

# Creating an array of integers
int_array = array.array('i', [1, 2, 3, 4, 5])

# Appending an element
int_array.append(6)
print(int_array)

# Extending with elements from another iterable
int_array.extend([7, 8])
print(int_array)

# Inserting an element at a specific position
int_array.insert(2, 99)
print(int_array)

# Removing an element
int_array.remove(4)
print(int_array)

# Reversing the array
int_array.reverse()
print(int_array)

print(int_array)  # Output: array('i', [8, 7, 99, 3, 2, 1, 6, 5])
