# to find number of 0s and 1s

num = 16
count1 = 0
count0 = 0
temp = num
while temp>0:
    if(temp&1 == 1):
        count1 +=1
    else:
        count0 +=1
    temp >>= 1

print(f"number of 0s {count0} and 1s {count1}")