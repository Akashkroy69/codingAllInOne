class School:
  def __init__(self, class1, class2):
    self.class1 = class1
    self.class2 = class2

# overloading add function
  def __add__(self,other):
    class1 = self.class1 + other.class1
    class2 = self.class2 + other.class2
    newSchool = School(class1, class2)
    return newSchool
  


school1 = School(50,40)
school2 = School(60,60)
print(school1.class1)

school3 = school1 + school2   # what is happening here? School.__add__(school1.school2)

print(school3.class1)


# gt >, ge>=