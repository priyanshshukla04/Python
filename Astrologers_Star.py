def astrologers_star(n1,n2):
    if n2 == True:
        for i in range(n1):
            for j in range(i,n1):
                print("*",end=" ")
            print()
    elif n2 == False:
        for i in range(n1):
            for j in range(i+1):
                print("*",end=" ")
            print()


number1 = int(input("Enter the range of star: "))
number2 = int(input("Enter a number 1 or 0: "))
number3 = bool(number2)
print(number3)
astrologers_star(number1,number3)