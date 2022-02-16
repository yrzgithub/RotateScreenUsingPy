import time
import keyboard
import rotatescreen
screen=rotatescreen.get_primary_display()

i=90
j=0
while True:
    if keyboard.is_pressed("alt+shift+r"):
        time.sleep(0.4)
        screen.rotate_to(i*j)
        j+=1
    if j==4:
        j=0
    if keyboard.is_pressed("esc"):
        screen.rotate_to(0)