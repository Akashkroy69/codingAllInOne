# Define a base class called 'Employee'
class Employee:
    # Constructor to initialize common attributes
    def __init__(self, name, employee_id, salary):
        self.name = name
        self.employee_id = employee_id
        self.salary = salary

    # Method to display employee information
    def display_info(self):
        return f"Name: {self.name}\nEmployee ID: {self.employee_id}\nSalary: ${self.salary}"

# Define a subclass 'Manager' that inherits from 'Employee'
class Manager(Employee):
    # Constructor for 'Manager' with additional attribute 'department'
    def __init__(self, name, employee_id, salary, department):
        # Call the constructor of the base class 'Employee'
        super().__init__(name, employee_id, salary)
        self.department = department

    # Override the 'display_info' method to include 'department'
    def display_info(self):
        # Call the 'display_info' method of the base class 'Employee'
        return super().display_info() + f"\nDepartment: {self.department}"

# Define a subclass 'Programmer' that inherits from 'Employee'
class Programmer(Employee):
    # Constructor for 'Programmer' with additional attribute 'programming_language'
    def __init__(self, name, employee_id, salary, programming_language):
        super().__init__(name, employee_id, salary)
        self.programming_language = programming_language

    def display_info(self):
        return super().display_info() + f"\nProgramming Language: {self.programming_language}"

# Define a subclass 'Tester' that inherits from 'Employee'
class Tester(Employee):
    def __init__(self, name, employee_id, salary, testing_tools):
        super().__init__(name, employee_id, salary)
        self.testing_tools = testing_tools

    def display_info(self):
        return super().display_info() + f"\nTesting Tools: {self.testing_tools}"

# Define a subclass 'Designer' that inherits from 'Employee'
class Designer(Employee):
    def __init__(self, name, employee_id, salary, design_tool):
        super().__init__(name, employee_id, salary)
        self.design_tool = design_tool

    def display_info(self):
        return super().display_info() + f"\nDesign Tool: {self.design_tool}"

# Create instances of different employees
manager = Manager("John Smith", "M001", 80000, "IT")
programmer = Programmer("Alice Johnson", "P001", 70000, "Python")
tester = Tester("Bob Davis", "T001", 65000, "Selenium")
designer = Designer("Eva White", "D001", 75000, "Photoshop")

# man1 = Manager(9000,"Ando")

# Display information about each employee
employees = [manager, programmer, tester, designer]

# Iterate through the employees and display their info
for employee in employees:
    print(employee.display_info())
    print("-----------------------")
