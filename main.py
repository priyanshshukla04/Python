name = input("Enter your name: ")
if name.isnumeric():
    raise print("Numbers are not allowed here")
age = int(input("enter your age: "))
if age < 18:
    raise print("You are not eligible to vote")

print(f"{name} Welcome to election commission of India")

name1 = input("Enter your name: ")
try:
    # print(name1)
    print(a)
except Exception as e:
    if name1 == name:
        raise print("You have already casted your vote")

    print("Exception handled")