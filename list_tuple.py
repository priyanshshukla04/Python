numbers=[4,2,5,3,7]
numbers.sort()
numbers.reverse()
print(numbers)
print(numbers[::2])   #will skip one number every time
print(numbers[::-1])   #will reverse the string,don't take any number smaller than -1
print(len(numbers))
print(max(numbers))
print(min(numbers))
numbers.insert(1,54)    #to insert at particular location as append() is used to add at the end
print(numbers)
numbers.remove(2)       #to remove an element
print(numbers)
numbers.pop()
print(numbers)      #to remove the last element of the list

#to swap the values of two numbers in python we use
a=5
b=19
a,b=b,a
print(a,b)
