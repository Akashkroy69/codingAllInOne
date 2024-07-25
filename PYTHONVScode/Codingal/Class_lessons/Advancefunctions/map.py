# map Function:

# The map function is used to apply a given function to each item of an iterable
# (e.g., a list) and return a map object, which is an iterator containing the results. 
# You can convert the map object into a list, set, or another iterable type.

# Define a function that squares a number
def square(x):
    return x ** 2

# Create a list of numbers
numbers = [1, 2, 3, 4, 5]

# Use map to apply the square function to each number in the list
squared_numbers = map(square, numbers)

# Convert the result to a list
squared_numbers_list = list(squared_numbers)

print(squared_numbers_list)
# Output: [1, 4, 9, 16, 25]
