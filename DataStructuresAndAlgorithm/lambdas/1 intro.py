add = lambda x,y: x+y


print(add(10,12))

list1 = [1,2,3,4,5]
# map
print(list((map(lambda x : x**2,list1))))
# filter
print(list(filter(lambda x :(x%2==1),list1)))
# sorting
students = [("John", 80), ("Alice", 90), ("Bob", 75)]
print(sorted(students,key= lambda x: x[1]))

# comp list
squares = [i * i for i in range(5)]
print(squares)
# Output: [0, 1, 4, 9, 16]

# even nums
even_numbers = [i for i in range(10) if i % 2 == 0]
print(even_numbers)
# Output: [0, 2, 4, 6, 8]

# ---
labels = ["Even" if i % 2 == 0 else "Odd" for i in range(5)]
print(labels)
# Output: ['Even', 'Odd', 'Even', 'Odd', 'Even']

# nested
pairs = [(x, y) for x in range(3) for y in range(3)]
print(pairs)
# Output: [(0, 0), (0, 1), (0, 2), (1, 0), (1, 1), (1, 2), (2, 0), (2, 1), (2, 2)]

