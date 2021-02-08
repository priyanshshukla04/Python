########LIST_Cmprehension##############
# ls = []
# for i in range(100):
#     print(i)
#or use comprehension to do the same task
ls = [i for i in range(100) if i%3==0]
print(ls)

########DICTIONARY_Cmprehension##############
dict1 = {i:f"itme{i}" for i in range(100) if i%2==0}
print(dict1)
dict2 = {v:k for k,v in dict1.items()}
print(dict2)

########SET_Cmprehension##############
s = {i for i in ["anhsul","saumaya","anhsul","saumaya","anhsul","saumaya"]}
print(s)
print(type(s))

########GENERATOR_Cmprehension##############
evens = (i for i in range(10))
print(type(evens))
print(evens.__next__())

for i in evens:
    print(i)
