class Cars:
    no_of_variety = 2

    def __init__(self, name, model, price):
        self.name = name
        self.model = model
        self.price = price

    @classmethod
    def class_car_method(cls, new_of_variety):
        cls.no_of_variety = new_of_variety

    @classmethod
    def dif_format(cls, data):
        return cls(*data.split("-"))

    @staticmethod
    def simple():
        print("This is car company")

class Customer(Cars):
    no_of_customers = 100

    def __init__(self,name, age, job, tenure):
        self.name = name
        self.age = age
        self.job = job
        self.tenure = tenure

    def simple_print(self):
        return f"The name is {self.name}"


lamborgini = Cars("Lamborgini", "A12", 200)
audi = Cars("Audi", "A123", 300)
# print(lamborgini.name)
lamborgini.class_car_method(3)
# print(lamborgini.no_of_variety)
# print(Cars.no_of_variety)
lamborgini = Cars.dif_format("lamborgini-a12-200")
# print(lamborgini.model)
lamborgini.simple()
# Cars.simple()

anshul = Customer("Anshul",21,"student",3)
# print(anshul.age)
priyansh = Customer("[Priyansh, Shukla]",21,"student",2)
# print(priyansh.name)
# print(anshul.no_of_variety)

