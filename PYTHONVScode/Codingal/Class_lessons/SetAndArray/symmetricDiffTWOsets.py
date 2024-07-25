# Define two sets
set1 = {1, 2, 3, 4, 5}
set2 = {4, 5, 6, 7, 8}

# Method 1: Using symmetric_difference() method
symmetric_diff1 = set1.symmetric_difference(set2)

# Method 2: Using the ^ operator
symmetric_diff2 = set1 ^ set2

# Display the symmetric differences
print("Symmetric Difference using method 1:", symmetric_diff1)
print("Symmetric Difference using method 2:", symmetric_diff2)
