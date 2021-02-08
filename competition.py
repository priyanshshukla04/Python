test = int(input("Print the number of test cases:"))
for i in range(test):
    count = 0
    j = 0
    str=input("Enter the string:")
    length=len(str)
    for i in range(1,length):
        if (str[j+1] == str[j]):
            count += 1
            j = j+1
            #print(count)
        else:
            j=j+1
    print(count)