import os
import time 
import keyboard

def enter():
    keyboard.press_and_release('enter')

def space():
    keyboard.press_and_release('space')

def writing(text):
    text = text.split()
    for i in text:
        keyboard.write(i)
        time.sleep(0.1)

keyboard.press_and_release('win + r')
time.sleep(0.3)
keyboard.write('chrome')
enter()
time.sleep(3)
keyboard.press_and_release('ctrl + shift + n')
time.sleep(1)
writing('p o r n h u b . c o m')
time.sleep(0.7)
# keyboard.press_and_release('ctrl + a')
# keyboard.press_and_release('delete')
keyboard.press_and_release('ctrl + w')
time.sleep(0.1)
keyboard.write('https://www.youtube.com/watch?v=dQw4w9WgXcQ')
enter()