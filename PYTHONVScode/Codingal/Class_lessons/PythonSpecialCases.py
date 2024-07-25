print("-------Print and different cases---------")
#print
print("Hello Muskan") #Prints hello muskan

print("Muskan is a good girl. \nShe likes to read.") # \n breaks the line

name = "Muskan" # Creating a string "Muskan" and storing in variable name

print("Hello, " + name)  # String concatanation: We can add 2 or more strings using + operator

newString = name + " Loves mom." #Example 2 for String concatanation
print(newString)

print(3 * name) #prints the string value 3 times



print("\n--------Variables and Data Types------------------\n")
# Variable is like a box (space in memory) where we store different types of Data. Data Types: Integer, Floats, Strings, Boolean

#Integer exapmle 1
score = 85
double_score = score * 2
print("Your score doubled:", double_score)

# Integers example 2
age = 16
print("Your age is:", age)

# Floating-Point Numbers or flots: decimal values
temperature = 27.5
print("The temperature is:", temperature)

# Strings: names, sentences or characters
name = "Muskan"
print("Your name is:", name)

# Booleans: either True or False
is_raining = True
print("Is it raining?", is_raining)

print("\n-----------------Operators-------------------------\n")

#operators: Arithmetic and conditional
x = 5
y = 3

print("x:",x,"y:",y)
print("ARITHMETIC OPERATIONS:")
print("\nAddition:", x + y)       # Output: 8
print("\nSubtraction:", x - y)    # Output: 2
print("\nMultiplication:", x * y) # Output: 15
print("\nDivision:", x / y)       # Output: 1.6666666666666667
print("\nFloor Division:", x // y)  # Output: 1
print("\nModulo(Remainder):", x % y) # Output: 2
print("\n X ^ Y:", x ** y) # Output: 125

print("\nConditional OPERATIONS:")
print("\nEqual to:", x == y)          # Output: False
print("Not equal to:", x != y)      # Output: True
print("Greater than:", x > y)       # Output: True
print("Less than:", x < y)          # Output: False
print("Greater than or equal to:", x >= y)  # Output: True
print("Less than or equal to:", x <= y)     # Output: False