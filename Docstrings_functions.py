a=3
b=2
c=sum((a,b))   #this is a built in function. We used double brackets because sum function take a list or tuple as input.
print(c)

def function1():
    print("This is a function which does not return any value")

def function2(a,b):
    #this is called docstring means the first line inside the function
    """this returns the average of two numbers"""
    average=(a+b)/2
    return average

function1()
v=function2(6,8)
print(v)

#to print the docstring
print(function2.__doc__)


