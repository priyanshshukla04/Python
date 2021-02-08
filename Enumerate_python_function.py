#Syntax    enumerate(iterable, start=0)
#eg1
lis1 = ["Priyansh","Shukla"]
for index, val in enumerate(lis1):
    print(index,val)
#eg2
lis2 = ["Priyansh","Shukla","File"]
result = enumerate(lis2, 4)
print(list(result))