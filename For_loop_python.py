list=("Priyansh","Saumya","Aashi")      #works with tuple
for i in list:
    print(i)

list1=[["Priyansh",3],["Saumya",3],["Aashi",4]]    #works with list
for z, u in list1:
    print(z,u)

dict=dict(list1)       #works with dictionary
print(dict)
for a,b in dict.items():
    print(a,b)

items = [int, float, "HaERRY", 5,3, 3, 22, 21, 64, 23, 233, 23, 6]
for s in items:
    if str(items).isnumeric and items>6:                    #to convert int nad float to string as they are keywords
        print(items)
