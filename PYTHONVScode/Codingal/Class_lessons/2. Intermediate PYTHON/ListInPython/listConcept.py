# Lists are one of the fundamental data structures in Python.
# They are used to store collections of items, such as numbers, strings, or other objects. 

# Creating Lists:

# You can create a list by enclosing a comma-separated sequence of values within square brackets [ ]. Here's an example:

# Creating a list of numbers
my_list = [1, 2, 3, 4, 5]

# Creating a list of strings
fruits = ["apple", "banana", "cherry"]

# list in python is versatile, it can hold different data types
mixed_list = ["A",12,1.2]
# list with pair values
#-------has to explore----------
#====================1===================================

# Accessing List Elements:
first_item = my_list[0]  # Gets the first element (1)
second_item = fruits[1]  # Gets the second element ("banana")
last_item = fruits[-1] 


# Modifying elements in a list
my_list[0] = 100  # Replaces the first element with 100
fruits[2] = "strawberry"  # Replaces the third element with "strawberry"
#====================2===================================

# List Operations:
# Appending an element to the end of a list
fruits.append("orange")
print(fruits)
# Extending a list with another list
more_fruits = ["grape", "kiwi"]
fruits.extend(more_fruits)
print(fruits)
# Concatenating two lists
combined_list = my_list + [6, 7, 8]
print(combined_list)
print([1,2,3]*10)




# List Functions:
list_length = len(my_list)
maximum_value = max(my_list)
minimum_value = min(my_list)
total_sum = sum(my_list)




# Slicing a list
sublist = fruits[1:4]  # Gets elements at indices 1, 2, and 3



# Nested Lists:
# Creating a nested list
matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9,0]]
# Accessing elements in a nested list
element = matrix[1][2]  # Accesses the element at row 1, column 2 (6)




# List comprehension to create a list of squares
squares = [x**2 for x in range(1, 6)]
# Result: [1, 4, 9, 16, 25]

# negative indexing
# reverse



