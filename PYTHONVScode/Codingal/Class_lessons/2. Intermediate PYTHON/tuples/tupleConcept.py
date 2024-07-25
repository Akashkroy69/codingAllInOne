# TUPLES are a data structure similar to lists, but with some key differences.

# A tuple is an ordered and immutable collection of elements. "Immutable" means once you create a tuple, 
# you cannot change its contents (add, remove, or modify elements).
#DEFINITION----------
# Tuples are defined using parentheses () or by simply separating elements with commas. 
my_tuple = (1, 2, 3)
another_tuple = 4, 5, 6  # Parentheses are optional
print(type(my_tuple),my_tuple)

#CONFUSION-----
tupleVsVar = (1)
print(type(tupleVsVar),tupleVsVar)
tupleVsVar2 = (1,)
print(type(tupleVsVar2),tupleVsVar2)

#ACCESSING THE ELEMENTS------------
first_element = my_tuple[0]  # Accesses the first element (1)
print(first_element)
#negative indexing
print(my_tuple[-1])


# Immutability:---------------
try:
   my_tuple[0] = 10  # This will raise an error (TypeError)
except Exception as e:
   print("ERROR: Tuples are immutable. You can't add/change value in TUPLEs, ",e )

#Tuple Packing and Unpacking:-----------
# Tuple packing is when you create a tuple by packing multiple values into a single tuple.
# Tuple unpacking is the opposite; you extract values from a tuple and assign them to separate variables.
my_tuple = 1, 2, 3  # Tuple packing
a, b, c = my_tuple  # Tuple unpacking
print(a,b,c)


# Tuple Methods:--------------------
# tuples have fewer built-in methods compared to lists because they are immutable. Common methods include count() 
# to count occurrences of an element and index() to find the index of an element.
my_tuple2 = (1, 2, 2, 3, 4)
count_2 = my_tuple2.count(2)  # Counts occurrences of 2 (2 times)
index_3 = my_tuple2.index(3)  # Finds the index of 3 (index 3)


#Iterating Over Tuples:----------
my_tuple = (1, 2, 3)
for item in my_tuple:
    print(item)

# nested tuple
nestedTuple = (1,2,3,(4,5),[6,"akash","alsan",10])
print("Value in Nested: ",nestedTuple[3][0])
print("nested Tuple Length: ",len(nestedTuple))



