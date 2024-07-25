# List Comprehensions:[expression for item in iterable if condition].
squares = [x ** 2 for x in range(10) if x % 2 == 0]
# Result: [0, 4, 16, 36, 64]


# Set Comprehensions:
text = "hello"
unique_chars = {char for char in text}
# Result: {'h', 'e', 'l', 'o'}

# Dictionary Comprehensions: {key: value for item in iterable if condition}
squares_dict = {x: x ** 2 for x in range(10) if x % 2 == 0}
# Result: {0: 0, 2: 4, 4: 16, 6: 36, 8: 64}

# tuple comprehension
tupleOriginal = (1,2,3,4,5)
tupleSquare = tuple(x**2 for x in tupleOriginal)
print(tupleSquare)

