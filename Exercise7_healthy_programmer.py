from pygame import mixer
from datetime import datetime
import time


def main_function_music(file_name, stop):
    mixer.init()
    mixer.music.load(file_name)
    mixer.music.set_volume(0.7)
    mixer.music.play()
    while True:
        user_input = input()
        if user_input == stop:
            mixer.music.stop()
            break


def water_log(msg):
    fhand = open("water.txt", "a")
    fhand.write(f"{msg} water at {datetime.now()}\n")
    fhand.close()


def eyes_log(msg):
    fhand = open("eyes.txt", "a")
    fhand.write(f"{msg} eyes exercise at {datetime.now()}\n")
    fhand.close()


def exercise_log(msg):
    fhand = open("exercise.txt", "a")
    fhand.write(f"{msg} exercise at {datetime.now()}\n")
    fhand.close()


if __name__ == '__main__':
    water_time = time.time()
    eyes_time = time.time()
    exercise_time = time.time()
    water_drinking_time = 30*60
    eyes_exercise_time = 40*60
    physical_exercise_time = 45*60
    while True:
        if time.time() - water_time > water_drinking_time:
            print("Its time to drink water. Enter 'drank' to stop the music: ")
            main_function_music("water.mp3", "drank")
            water_log("Drank")
            water_time = time.time()

        if time.time() - eyes_time > eyes_exercise_time:
            print("Its time to relax your eyes. Enter 'deyes' to stop the music: ")
            main_function_music("eyes.mp3", "deyes")
            eyes_log("Done")
            eyes_time = time.time()

        if time.time() - exercise_time > physical_exercise_time:
            print("Its time to move around. Enter 'dphy' to stop the music: ")
            main_function_music("physical.mp3", "dphy")
            exercise_log("Done")
            exercise_time = time.time()
