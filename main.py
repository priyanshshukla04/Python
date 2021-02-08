# Health Management System
# 3 clients - Harry, Rohan and Hammad
# Total 6 files
# write a function that when executed takes as input client name
# One more function to retrieve exercise or food for any client

def getdate():
    import datetime
    return datetime.datetime.now()


def Priyansh_file_exercise():
    choice = int(input("Enter 1 for retrieving data and 2 for writing data: "))
    if (choice == 1):
        fhand = open("priyansh_exercise.txt")
        for i in fhand:
            print(i+"\n")
        fhand.close()
    elif (choice == 2):
        fhand = open("priyansh_exercise.txt", "a")
        exercise = input("Enter the exercise name: ")
        fhand.write(str(str[getdate()])+" :"+exercise+"\n")
        print("Write successful")
        fhand.close()
def Priyansh_file_diet():
    choice = int(input("Enter 1 for retrieving data and 2 for writing data: "))
    if (choice == 1):
        fhand = open("priyansh_diet.txt")
        for i in fhand:
            print(i + "\n")
        fhand.close()
    elif (choice == 2):
        fhand = open("priyansh_diet.txt", "a")
        diet = input("Enter the diet: ")
        fhand.write("[ "+ str(getdate())+" ] : "+diet+ "\n")
        print("Write successful")
        fhand.close()

def Shrey_file_exercise():
    choice = int(input("Enter 1 for retrieving data and 2 for writing data: "))
    if (choice == 1):
        fhand = open("shrey_exercise.txt")
        for i in fhand:
            print(i+"\n")
        fhand.close()
    elif (choice == 2):
        fhand = open("shrey_exercise.txt", "a")
        exercise = input("Enter the exercise name: ")
        fhand.write("[ " + str(getdate()) + " ] : " + exercise + "\n")
        print("Write successful")
        fhand.close()
def Shrey_file_diet():
        choice = int(input("Enter 1 for retrieving data and 2 for writing data: "))
        if (choice == 1):
            fhand = open("shrey_diet.txt")
            for i in fhand:
                print(i+"\n")
            fhand.close()
        elif (choice == 2):
            fhand = open("shrey_diet.txt", "a")
            diet = input("Enter the diet: ")
            fhand.write("[ " + str(getdate()) + " ] : " + diet + "\n")
            print("Write successful")
            fhand.close()

def Shwetank_file_exercise():
    choice = int(input("Enter 1 for retrieving data and 2 for writing data: "))
    if (choice == 1):
        fhand = open("shwetank_exercise.txt")
        for i in fhand:
            print(i+"\n")
        fhand.close()
    elif (choice == 2):
        fhand = open("shwetank_exercise.txt", "a")
        exercise = input("Enter the exercise name: ")
        fhand.write("[ " + str(getdate()) + " ] : " + exercise + "\n")
        print("Write successful")
        fhand.close()
def Shwetank_file_diet():
        choice = int(input("Enter 1 for retrieving data and 2 for writing data: "))
        if (choice == 1):
            fhand = open("shwetank_diet.txt")
            for i in fhand:
                print(i+"\n")
            fhand.close()
        elif (choice == 2):
            fhand = open("shwetank_diet.txt", "a")
            diet = input("Enter the diet: ")
            fhand.write("[ " + str(getdate()) + " ] : " + diet + "\n")
            print("Write successful")
            fhand.close()

def other_part():
    clear = input("Enter y if you want to clear the data of a file and n to exit: ")
    if (clear == "y"):
        option = input("Enter the name of the person whose file you want to erase: ")
        if (option == "Priyansh"):
            option1 = int(input("Enter 1 to clear exercise and 2 for diet file: "))
            if (option == 1):
                fhand = open("priyansh_exercise.txt", "w")
                fhand.close()
            elif(option == 2):
                fhand = open("priyansh_diet.txt", "w")
                fhand.close()
        elif (option == "Shrey"):
            option1 = int(input("Enter 1 to clear exercise and 2 for diet file: "))
            if (option == 1):
                fhand = open("shrey_exercise.txt", "w")
                fhand.close()
            elif (option == 2):
                fhand = open("shrey_diet.txt", "w")
                fhand.close()
        elif (option == "Shwtank"):
            option1 = int(input("Enter 1 to clear exercise and 2 for diet file: "))
            if (option == 1):
                fhand = open("shwetank_exercise.txt", "w")
                fhand.close()
            elif (option == 2):
                fhand = open("shwetank_diet.txt", "w")
                fhand.close()
    elif (clear == "n"):
        exit()

choice = int(input("Enter 1 for files and 2 for other options: "))
if (choice==1):
    name = input("Enter the name of person: ")
    if(name=="Priyansh"):
        operation = int(input("Enter 1 for exercise file and 2 for diet: "))
        if (operation == 1):
            Priyansh_file_exercise()
        elif (operation == 2):
            Priyansh_file_diet()
    elif (name == "Shrey"):
        operation = int(input("Enter 1 to exercise file and 2 for diet: "))
        if (operation == 1):
            Shrey_file_exercise()
        elif (operation == 2):
            Shrey_file_diet()
    elif (name == "Shwetank"):
        operation = int(input("Enter 1 to exercise file and 2 for diet: "))
        if (operation == 1):
            Shwetank_file_exercise()
        elif (operation == 2):
            Shwetank_file_diet()
elif(choice==2):
    other_part()

