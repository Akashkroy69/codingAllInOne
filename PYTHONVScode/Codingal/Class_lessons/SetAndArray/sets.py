# A set is an unordered collection of unique elements. In Python, you can create a set by enclosing a 
# comma-separated sequence of values in curly braces {} or by using the set() constructor.

# Creating a set
fruits = {'apple', 'banana', 'cherry'} #In this example, fruits is a set containing three unique strings.

# Duplicate elements are automatically removed
colors = {'red', 'green', 'blue', 'red'}
# The 'colors' set will only contain 'red', 'green', and 'blue'

# using set constructor
my_list = [1, 2, 3, 2, 1]  # A list with duplicate elements
my_set = set(my_list)

#------------------------------------------------------------------

#You can perform set operations like union, intersection, and difference:
set1 = {1, 2, 3}
set2 = {3, 4, 5}

# Union
union_result = set1.union(set2)  # {1, 2, 3, 4, 5}

# Intersection
intersection_result = set1.intersection(set2)  # {3}

# Difference
difference_result = set1.difference(set2)  # {1, 2}

#--------------------------------------------------------------------
# Adding elements to a set
fruits.add('orange')      # Add a single element
fruits.update({'pear', 'kiwi'})  # Add multiple elements
# Removing elements from a set
fruits.remove('banana')  # Remove a specific element
fruits.discard('kiwi')   # Remove an element if it exists (no error if it doesn't)
removed_fruit = fruits.pop()  # Remove and return an arbitrary element
#=================================================================
fruits.clear()      # Remove all elements from the set
fruits_copy = fruits.copy()  # Create a shallow copy of the set
is_subset = set1.issubset(set2)  # Check if set1 is a subset of set2
is_superset = set1.issuperset(set2)  # Check if set1 is a superset of set2
set1.difference_update(set2)  # Update set1 with the difference (in-place)
#----------------FROZEN SET------------------------------
# Frozen Sets:

# Python also provides a special type of set called a "frozenset." A frozenset is immutable, 
# meaning its elements cannot be changed after creation. You can create a frozenset using the frozenset() 
# constructor.
frozen_set = frozenset([1, 2, 3])

#--------------------------------------------------------------------
# Sets are commonly used when you need to work with a collection of unique elements, 
# such as finding unique values in a list or checking for membership without duplicates.
# Using a set to find unique elements in a list
numbers = [1, 2, 2, 3, 3, 4, 5, 5]
unique_numbers = set(numbers)
print(unique_numbers)  # {1, 2, 3, 4, 5}


