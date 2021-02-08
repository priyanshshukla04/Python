"""This is a faulty calculator. If the numbers are 23 and 34 and operator is '+' then it will print the wrong output as 70
If the numbers are 30 and 12 and the operator is '/' then it will print 4.
If the numbers are 56 and 2 and the operator is '*' then it will print 100.
For all the other cases it will print the right output
"""
num1=int(input("Enter the first number: "))
num2=int(input("Enter the second number: "))
operator=input("Choose the operator : '+' for addition, '-' for substraction, "
                   "'/' for division, '*' for multiplication ")

if operator== "+":
    if num1==23 and num2==34:
        print("Sum is : 70")
    else:
        sum=num1+num2
        print("Sum is : ",sum)

if operator== "/":
    if num1==30 and num2==12:
        print("Answer is: 4")
    else:
        ans=num1/num2
        print("Answer is: ",ans)

if operator== "*":
    if num1==56 and num2==2:
        print("Multiplication is: 100")
    else:
        multi=num1*num2
        print("Multiplicatio is: ",multi)

if operator== "-":
    if num1>num2:
        subs=num1-num2
        print("Substraction is: ",subs)
    else:
        subs=num2-num1
        print("Substrcation is: ",subs)

print("Thank you")


