d1={"priyansh":"healthy","saumya":"junk","aashi":{"day":"junk","night":"junk"}}
print(d1)
print(d1["aashi"])    #to print the nested dictionary
print(d1["aashi"]["day"])   #to print a value of a nested dictionary
#to add elements in a dictionry
d1["vansh"]="junk food"
d1[20]="healthy"
#other way to add elements in a dict is
d1.update({"nanhi":"junk food"})
print(d1)
print(d1)
del d1[20]     #to delete an element
print(d1)
d2=d1.copy()     #it copies the dictionary and makes a new one. If we use d2=d1 to form a new dict then it will not create a new dict but will return the refernece of the same dict. Any  changes made to new one will effect the original dict
print(d2)
print(d2.get("priyansh"))
print(d2.items())     #to print all key-value pairs
print(d2.keys())     #to get all keys
print(d2.values())
