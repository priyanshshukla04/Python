def sum():
    a = 10  # local variable cannot be accessed outside the function
    b = 20
    sum = a + b
    print(sum)


#print(a)  # this gives an error







a=1  #global variable

#def print_Number():

            #a=a+1;   #to change the value we have to define global keyword
            #print(a)

#print_number()




# l = 10 # Global
#
# def function1(n):
#     # l = 5 #Local
#     m = 8 #Local
"""This gives the permission to change the value of global variable
printing this even outside will change the value of this variable"""
#     global l
#     l = l + 45
#     print(l, m)
#     print(n, "I have printed")
#
# function1("This is me")
# # print(m)
#print(l)


x = 89
def harry():
    x = 20
    def rohan():
        global x
        x = 88

    print("before calling rohan()", x)
    rohan()
    print("after calling rohan()", x)


harry()
print(x)






