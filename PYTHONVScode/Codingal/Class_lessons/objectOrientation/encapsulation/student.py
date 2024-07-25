class Student:
    def __init__(self,name,sch):
        self.name=name
        self.__sch=sch
    def display_info(self):
        print(self.__sch)



stud = Student("Akash","bvm")

print(stud.display_info)
