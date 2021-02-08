f = open("priyansh.txt")
f.seek(11)      #it sets the pointer to the mentioned location
print(f.tell())      #it tell the position of pointer
print(f.readline())   #it reads line in a file one line at a time
# print(f.tell())

print(f.readline())
# print(f.tell())
f.close()


"""This with keyword is used to replace open() and close() file as it automatically opens and closes the file
on exiting the with block"""
# with open("harry.txt") as f:
#     a = f.readlines()
#     print(a)

#readlines() is used to access all lines in a file as a list

"""To access two files simultaneously"""
#With open(“file1txt”) as f, open(“file2.txt”) as g