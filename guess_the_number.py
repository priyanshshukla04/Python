# guess the number
# no of guesses left and no of guesses he took to win
# total guess 9
# game over
import pyttsx3

speak = pyttsx3.init()
speak.say("When you ready press y")
speak.runAndWait()
n = 16
guess = 0
guess_left = 0
user_input = input("When you ready press y")
if (user_input == 'y'):
    while (guess <= 7):
        speak.say("guess the number between 1 to 50: ")
        speak.runAndWait()
        number = int(input("guess the number between 1 to 50: "))
        if (number == n):
            print("Congrats! You won\n")
            speak.say("You won")
            speak.runAndWait()
            guess = guess + 1
            print("Guesses you took: ", guess)
            break
        elif (number < n):
            speak.say("Enter a higher number")
            speak.runAndWait()
            print("Enter a higher number", end=" ")
            guess = guess + 1
            guess_left = 6 - guess
            print("\nGuesses left: ", guess_left)
        elif (number > n):
            print("Enter a smaller number", end=" ")
            speak.say("Enter a smaller number")
            speak.runAndWait()
            guess = guess + 1
            guess_left = 6 - guess
            print("\nGuesses left: ", guess_left)
        if (guess == 9):
            speak.say("Oops! game over, you lost")
            speak.runAndWait()
            print("game over, you lost")
            speak.say("The answer was 16")
            speak.runAndWait()
            print("The answer was:", n)
            break
