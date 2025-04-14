# check nth bit is set or not
num = 10
# 1010
# oth --> >>

place = 4

# print((num >> place -1)&1)
print(num & (1 << (place-1))) 


