num  = ['1','2',"3",'4']
vari = ','
print(vari.join(num))

lis = {"name": "Jack", "country": "America"}
separator = "_separator_"
print(separator.join(lis))

#this gives an error
# inputlist = ["Test1",13,"Test2",24,"Test3",100,"Test4"]
# sep = '_'
# out = sep.join(inputlist)
# print(out)

lis1 = ["John", "cena", "Randy", "orton",
       "Sheamus", "khali", "jinder mahal"]
a = ", ".join(lis1)
print(a)