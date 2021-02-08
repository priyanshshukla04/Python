# Snake water gun
# Create a snake water gun game in Python!
# Search Snake water gun game in google if you need help on rules and how to play the game!
import random
i = 0
user_won = 0
computer_won = 0
chance = 10
lst = ["snake","water","gun"]
while(i<=chance):
    user_choice = input("Enter your choice from snake,water and gun: ")
    computer_choice = random.choice(lst)
    if(user_choice=="snake" and computer_choice=="snake" or user_choice=="water" and computer_choice=="water" or user_choice=="gun" and computer_choice=="gun"):
        print("It is a tie!")
        i += 1
        chance -= 1
        print(f"Number of chances left: {chance}")
    elif(user_choice == "snake" and computer_choice == "water"):
        print("User won this round")
        i = i+1
        user_won +=1
        chance -= 1
        print(f"Number of chances left: {chance}")
    elif(user_choice == "snake" and computer_choice == "gun"):
        print("Computer won this round")
        i += 1
        computer_won += 1
        chance -= 1
        print(f"Number of chances left: {chance}")
    elif(user_choice == "water" and computer_choice == "snake"):
        print("Computer won this round")
        i += 1
        computer_won += 1
        chance -= 1
        print(f"Number of chances left: {chance}")
    elif(user_choice == "water" and computer_choice == "gun"):
        print("User won this round")
        i = i + 1
        user_won += 1
        chance -= 1
        print(f"Number of chances left: {chance}")
    elif(user_choice == "gun" and computer_choice == "snake"):
        print("User won this round")
        i = i + 1
        user_won += 1
        chance -= 1
        print(f"Number of chances left: {chance}")
    elif(user_choice == "gun" and computer_choice == "water"):
        print("Computer won this round")
        i += 1
        computer_won += 1
        chance -= 1
        print(f"Number of chances left: {chance}")
    else:
        print("Invalid Input")
print("The final results after 10 rounds are")
if(user_won>computer_won):
    print("User won the round with final scores as")
    print("User score: ",+user_won)
    print("Computer score: ",+computer_won)
elif(user_won<computer_won):
    print("Computer won the round with final scores as")
    print("User score: ", +user_won)
    print("Computer score: ", +computer_won)
elif(user_won == computer_won):
    print("It is a tie!")








