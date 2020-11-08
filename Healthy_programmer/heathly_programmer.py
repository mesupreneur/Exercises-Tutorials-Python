#------------------------------healthy_programmer_program-------------------------------------
''''
Assume that a programmer works at the office from 9-5 pm. We have to take care of his health and remind him three things,
To drink a total of 3.5-liter water after some time interval between 9-5 pm.35 min
To do eye exercise after every 30 minutes.
To perform physical activity after every 45 minutes.
'''
# Instructions:
'''
The task is to create a program that plays mp3 audio until the programmer enters the input which implies that he has done the task.

For Water, the user should enter “drank”
For Eye Exercise, the user should enter “eyedone”
For Physical Exercise, the user should enter “exdone”
After the user entered the input, a file should be created for every task (one file), which contains the details about the time when the user performed a certain task.
'''
# Challenge:
'''
You will have to manage the clashes between the reminders. Such that no two reminders play at the same time.
Use pygame module to play audio.
If you are following the lectures regularly, then I'm sure you can complete the task in no time.
'''
'''
In order to play music/audio files in pygame, pygame.mixer is used (pygame module for loading and playing sounds).
This module contains classes for loading Sound objects and controlling playback. 
There are basically four steps in order to do so:
Starting the mixer
mixer.init()
Loading the song.
mixer.music.load("song.mp3")
Setting the volume.
mixer.music.set_volume(0.7)
Start playing the song.
mixer.music.play()
'''
#---------------------------------how to use pygame audio module--------------
# import pygame
# file = 'some.mp3'
# pygame.init()
# pygame.mixer.init()
# pygame.mixer.music.load(file)
# pygame.mixer.music.play()
'''
mixer pygame module for loading and playing sounds is available and initialized before using it. The mixer module has a limited number of channels for playback of sounds.
Usually programs tell pygame to start playing audio and it selects an available channel automatically.
'''
import pygame#if we write (from pygame import mixer)then we have to write only mixer.
import datetime
import time#if we want to write from time import time then we only have to write time() to get the time
# but if we write import time then we have to write time.time()
def musicloop(file,stopper):#playing music in loop
    pygame.mixer.init()
    pygame.mixer.music.load(file)
    pygame.mixer.music.set_volume(0.7)
    pygame.mixer.music.play()
    while True:
        a=input()
        if a==stopper:
            pygame.mixer.music.stop()
            break
def log_now(message):
    with open("my_logs.txt","a") as f:
        f.write(f"{message} {datetime.datetime.now()}\n")
if __name__ == "__main__":#it is only use in main means this folder only
    # musicloop("water.mp3","stop")
    init_water= time.time()
    init_eyes= time.time()
    init_exercise= time.time()
    water_second=35*60#we have written 35*60 because 35 is second then to make it in minute we write *60
    eyes_second=30*60
    exercise_second=45*60
    while True:
        if time.time()-init_water>water_second:
            print("water drinking time.enter drank to stop the alarm")
            musicloop("water.mp3","drank")
            init_water=time.time()
            log_now("drank at ")
        if time.time()-init_eyes>eyes_second:
            print("eye exercise time.enter eyedone to stop the alarm")
            musicloop("eyes.mp3","eyedone")
            init_eyes=time.time()
            log_now("drank at ")
        if time.time()-init_exercise>exercise_second:
            print("exercise time.enter exdone to stop the alarm")
            musicloop("exercise.mp3","exdone")
            init_exercise=time.time()
            log_now("exercise at ")

