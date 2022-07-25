from PIL import ImageGrab
import keyboard
import os
import time
#счетчик
counter = 0
#обозначения клавиш
start = 's'
pause = 'p'
quit_key = 'q'

while True:
    if keyboard.is_pressed(start):
        while True:
            os.chdir('path to image folder')
            img = ImageGrab.grab()
            img.save(f'{counter}.jpg')
            counter += 1
            time.sleep(0.5)
            if keyboard.is_pressed(pause):
                break
    if keyboard.is_pressed(quit_key):
        break



