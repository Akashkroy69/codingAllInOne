# hcf using recursion

# 12---> 2x3x2
#18--> 2x3x3
# 6

# i = 2
# def gcd(n1,n2,i):
#     if n1 == 0 or n2 ==0: return 1

#     if n1 % i == 0 and n2%i == 0: 
#         return i * gcd(n1//i,n2//i,i)
#     else:
#         return i * gcd(n1,n2,i+1)




# print(gcd(12,18,i))

def gcd(n1, n2):
    if n2 == 0:
        return n1
    else:
        return gcd(n2, n1 % n2)

# Example usage
print(gcd(12, 18))  # Output: 6

# euclidian algo