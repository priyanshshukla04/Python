class Employee:
    def __init__(self, fname, lname):
        self.fname = fname
        self.lname = lname

    def explain(self):
        return f"The name is {self.fname} {self.lname}"

    @property
    def email(self):
        if self.lname == None or self.lname == None:
            return f"email is not set"
        return f"{self.fname}.{self.lname}@gmail.com"

    @email.setter
    def email(self, string):
        print("setting.....")
        names = string.split("@")[0]
        self.fname = names.split(".")[0]
        self.lname = names.split(".")[1]

    @email.deleter
    def email(self):
        self.fname = None
        self.lname = None


a = Employee("Priyansh", "Shukla")
# print(a.explain())
# print(a.email())
# a.email = "anshul.shukla@gmail.com"
print(a.email)
a.email = "anshul.shukla@gmail.com"
print(a.fname)
del a.email
print(a.email)
a.email = "Harry.Perry@codewithharry.com"
print(a.email)