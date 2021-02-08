"""
Iterable - __iter__() or __getitem__()
Iterator - __next__()
Iteration -

"""

def geb(n):
    for i in range(n):
        yield i

a = geb(4)
print(a.__next__())
print(a.__next__())
print(a.__next__())

# int cannot be iterated
# h = 546546
# ier = iter(h)
# print(ier.__next__())
# print(ier.__next__())
# print(ier.__next__())


#fibonacci using generator
def fibo(n):
    a,b = 0,1
    