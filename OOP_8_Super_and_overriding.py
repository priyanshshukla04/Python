class A:
    classvar = "I am class variable of class A"
    def __init__(self):
        self.var1 = "I am instance variable of class A"
        self.classvar = "I am instance variable of class A inside class A"
        self.special = "Special of class A"

    def simple(self):
        print("Hello of class A")
class B(A):
    classvar = "I am class variable of class B"
    def __init__(self):
        #allows to use class A instance variable
        super().__init__()
        self.var1 = "I am instance variable of class B"
        self.classvar = "I am instance variable of class B inside class B"
        #will override the instance variable of this class to class A's
        super().__init__()

    def simple(self):
        super().simple()
        print("Hello of class B")
        super().simple()
a = A()
b = B()
# print(b.var1)
# print(b.classvar)
# print(B.classvar)
# print(a.var1, a.classvar, A.classvar)
# print(b.special)
b.simple()
