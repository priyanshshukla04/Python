class Employee:
    no_leaves = 8
    pass

    @classmethod
    def change_leaves(cls, new_leaves):
        cls.no_leaves = new_leaves
    #alternate constructor
    @classmethod
    def from_dash(cls, string):
        return cls(*string.split("-"))

    @staticmethod
    def static_use():
        print("This is static method which does not"
              "requires cls or self")


# Anshul = Employee.from_dash("Priyansh-100000")
# print(Anshul.salary)
# print(Anshul.name)


# Anshul.change_leaves(20)
# print(Anshul.no_leaves)
#classmethod can be called even by class
Employee.change_leaves(22)
print(Employee.no_leaves)

Anshul = Employee()
#staticmethod could be accessed by object and class both
Employee.static_use()
Anshul.static_use()
