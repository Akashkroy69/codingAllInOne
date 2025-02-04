# finding the first set bit

num = int(input("Enter a number: "))

count = 0

# 100
# 0001
while num > 0:
    count +=1
    if (num & 1) == 1:
        break
    num //=2


if count > 0 :
    print(f"set bit is found at {count} position")
else:
    print("not found")

