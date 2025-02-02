# write a program to check how many time a character is ocurring in a word
word = "akakskhh"

char_count = {}

# time complexity: O(n) * O(1)
for ch in word:
    if ch in char_count:
        char_count[ch] = (char_count[ch]+1)
    else:
        char_count[ch] = 1
for char,count in char_count.items():
    print(f"char {char} : {count} ocurrence")