import rotatescreen
import time
sec=1
screen=rotatescreen.get_primary_display()
for i in range(10):
    screen.rotate_to(0)
    time.sleep(sec)
    screen.rotate_to(90)
    time.sleep(sec)
    screen.rotate_to(180)
    time.sleep(sec)
    screen.rotate_to(270)
    time.sleep(sec)