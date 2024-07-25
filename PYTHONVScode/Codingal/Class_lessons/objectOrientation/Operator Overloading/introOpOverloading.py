a  = 5
c = 10
b  = "hi"
print("hello" + b)
# print(a + b) is giving error

#  behind the scene
print(a + c)
print(int.__add__(a,c))
sum = a+ c
d ="hello"
print(b+d)
print(str.__add__(b,d))