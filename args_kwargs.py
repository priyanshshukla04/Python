#We have seen that a function can only pass a certain number of arguments.
# The number of arguments has to be decided while defining the function,
# and it can not be changed while calling it. In simple terms, the number
# of arguments passed should be the same as the ones that are defined.
# If we dislike this restriction and do not want ourselves to be bound by certain limits,
# then we are lucky to have *args and **kwargs with us.

def function_name(a,b,c,d):
    print(a,b,c,d)
#adding or deleting records leads to change it in fucntion definition also which is tedious for large programs
function_name("Priyansh","Saumya","Vansh","Shubhansh")

def funargs(normal,*args,**kwargs):  #the order of normal, args and kwargs must be maintained
    print(normal)
    for i in args:
        print(i)
    print("Some use of kwargs")
    for k,v in kwargs.items():
        print(f"The key is {k} and the value is {v}")

normal = "This is use of args"
a_args = ["Priyansh","Saumya","Vansh","Shubhansh"]   #always pass tuple in argument to *args
b_kwargs = {"Priyansh":"Leader","Saumya":"Cook","Vansh":"Trainer","Shubhansh":"Gymnast"}
funargs(normal,*a_args,**b_kwargs)



