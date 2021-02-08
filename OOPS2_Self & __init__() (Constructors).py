class Employee:
    no_leaves = 8
    pass

    # this is constructor in python created using __init__
    def __init__(self, aname, asalary):
        self.name = aname
        self.salary = asalary
        #print("hello")

    # this is a method where self is the name of the object that uses it
    def printdetails(self):
        return f"The name is {self.name}, salary is {self.salary} "

    @classmethod
    def change_leaves(cls, new_leaves):
        cls.no_leaves = new_leaves
    #alternate constructor
    @classmethod
    def from_dash(cls, string):
        return cls(*string.split("-"))
priyansh = Employee("Priyash", 100000)
Anshul = Employee.from_dash("Priyansh-100000")
print(Anshul.salary)
print(Anshul.name)

# priyansh.name = "Anshul"
# priyansh.salary = 100000
# print(priyansh.printdetails())
priyansh.change_leaves(20)
# print(priyansh.salary)
print(priyansh.no_leaves)
#classmethod can be called even by class
Employee.change_leaves(22)
print(Employee.no_leaves)
