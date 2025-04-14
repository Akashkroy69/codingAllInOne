class Point:
    def __init__(self, x,y):
        self.x = x
        self.y = y
    def __add__(self, other):
        return Point(self.x +other.x, self.y +other.y)
    def __sub__(self, other):
        return Point(self.x -other.x, self.y -other.y)
    def __mul__(self, other):
        return Point(self.x *other.x, self.y *other.y)
    def __truediv__(self, other):
        return Point(self.x /other.x, self.y /other.y)
    

    def __str__(self):
        return f"(x: {self.x},y: {self.y})"
    

p1 = Point(2,3)
p2 = Point(4,5)
p3 = p1 + p2

print(p3)

p4 = p1 - p2
print(p4)

p5 = p1 * p2
print(p5)

p6 = p1 / p2
print(p6)

# __str__ method is used to define the string representation of the object
p1 = Point(2,3)
print(p1)
# print(p7)

# +	__add__
# -	__sub__
# *	__mul__
# /	__truediv__
# ==	__eq__
# <	__lt__

# >	__gt__
# <=	__le__
# >=	__ge__
# !=	__ne__
# %	__mod__
# **	__pow__
# //	__floordiv__
# &	__and__
# |	__or__
# ^	__xor__
# <<	__lshift__
# >>	__rshift__
# in-place operators

# +=	__iadd__
# -=	__isub__

# __str__ method is used to define the string representation of the object