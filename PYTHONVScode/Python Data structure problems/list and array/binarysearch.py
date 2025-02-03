#       0   1  2  3 4  5  6  7  8
list = [12,34,13,15,16,18,76,77,89]
list.sort()
# 12,13,15,16,18,34
num = int(input("Enter the number to search: "))

first = 0
last = len(list) - 1
found = False
print(len(list))

while first <= last:
     midIndex = (first + last)//2
     if(list[midIndex] == num):
          found = True
          print(f"{num } is found at index {midIndex}")
          break
     else:
        if num < list[midIndex]:
          last = midIndex -1
        else:
           first = midIndex + 1

if found == False:
    print(f"num is not found")
        