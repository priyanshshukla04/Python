###############First###########
class Student:
    pass

harry = Student()
larry = Student()

harry.name = "Harry"
harry.std = 12
harry.section = 1
larry.std = 9
larry.subjects = ["hindi", "physics"]
print(harry.section, larry.subjects)


##########Second###########
class Employee:
    no_of_leaves = 8
    annual_turnover = 100000

priyansh = Employee()
Tiger = Employee()

priyansh.name = "Anshul"
priyansh.salary = 100000
Tiger.name = "Tiggu"
Tiger.salary = 0
#this does not change the class variable value but creates a new instance variable
priyansh.no_of_leaves = 10
print(priyansh.no_of_leaves)
print(priyansh.__dict__)
print(Employee.no_of_leaves)
print(Employee.__dict__)
Employee.no_of_leaves = 10
print(Employee.__dict__)
print(Employee.no_of_leaves)




