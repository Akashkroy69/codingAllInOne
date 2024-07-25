
# What is a Dictionary?
# A dictionary in Python is like a real-world dictionary. It's 
# a collection of key-value pairs, where each key is a unique 
# identifier for a piece of data, and each key is associated with a value.

# Creating a dictionary of information about a person
person = {
    "name": "John",
    "age": 17,
    "city": "New York"
}
# print("***",person.name)

# Accessing values
print()
name = person["name"]
age = person["age"]
print(name)
print(age)

# Adding a new key-value pair
person["job"] = "Engineer"
print(person)

# Modifying a value
person["age"] = 20
print(person)

# Checking if a Key Exists:

# You can check if a key exists in a dictionary using the in keyword:
if "name" in person:
    print("Name exists in the dictionary.")

#----------LOOPING-----------------
# Looping through keys
for key in person:
    print(key)

# Looping through values
for value in person.values():
    print(value)

# Looping through key-value pairs
for key, value in person.items():
    print(key, ":", value)

#------------------
# ict.get(key, default): Returns the value associated with the given key, or the default value if the key is not found.
my_dict = {"name": "Alice", "age": 30, "city": "New York"}
name = my_dict.get("name", "Unknown")
occupation = my_dict.get("occupation", "Unemployed")
print(name)  # Output: 'Alice'
print(occupation)  # Output: 'Unemployed'
#-------------------
# dict.pop(key, default): Removes the key-value pair with the specified key and 
# returns the value. If the key is not found, it returns the default value 
# (or raises a KeyError if no default is provided).
age = my_dict.pop("age")
occupation = my_dict.pop("occupation", "Unemployed")
print(age)  # Output: 30
print(occupation)  # Output: 'Unemployed'
print(my_dict)
#---------------------------------------------
# ict.popitem(): Removes and returns an arbitrary (key, value) 
# pair from the dictionary as a tuple. This method is available in Python 3.7 and later.
my_dict = {"name": "Alice", "age": 30, "city": "New York"}
item = my_dict.popitem()
print(item)  # Output: ('city', 'New York')
#---------------------------------------------
# dict.update(other_dict): Updates the dictionary with key-value pairs from other_dict.
my_dict = {"name": "Alice", "age": 30}
additional_info = {"city": "New York", "occupation": "Engineer"}
my_dict.update(additional_info)
print(my_dict)
# Output: {'name': 'Alice', 'age': 30, 'city': 'New York', 'occupation': 'Engineer'}


