# def funct1():
#     print("This is Priyansh")
# func = funct1
# func()

#returning a function from a function as we returned print and sum fucntion
# def funct1(num):
#     if num == 0:
#         return print
#     elif num ==1:
#         return sum
# func = funct1
# print(func(0))

#decorators

def funct(fun1):
    def nowexe():
        print("This is Priyansh")
        fun1()
        print("Shukla")
    return nowexe

@funct
def priyansh():
    print("This is after executing")

#priyansh = funct(priyansh)
priyansh()
