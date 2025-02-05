# write a program to check how many time a character is ocurring in a word

# akash
# a --> 2
# k --> 3
word = "akakskh"
checkedChar = []
for i in  range(len(word)):
    count = 1
    if word[i] not in checkedChar:
      checkedChar.append(word[i])
      for j in range(i+1, len(word)):
        #   print(word[i],word[j],i,j,count)
          if word[i] == word[j]:
              count += 1
      if count >= 1:
          print(f"{word[i]} ocurred {count} times")

# i --> 0 
#   c=0, j=1-
