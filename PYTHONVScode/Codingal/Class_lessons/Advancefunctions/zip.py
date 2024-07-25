# zip Function:

# The zip function is used to combine two or more iterables (e.g., lists) element-wise into tuples. 
# It returns an iterator of tuples where the i-th tuple contains the i-th element from each of the input iterables.

# Here's a simple example of how zip works:


# Create two lists
names = ["Alice", "Bob", "Charlie"]
scores = [85, 92, 78]

length = (len(scores))
scores.remove(85)
print(scores)

# Use zip to combine the lists into pairs of (name, score)
name_score_pairs = zip(names, scores)

# Convert the result to a list
name_score_list = list(name_score_pairs)

print(name_score_list)
# Output: [('Alice', 85), ('Bob', 92), ('Charlie', 78)]


