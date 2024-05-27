from lzma import CHECK_CRC32
import pygame as game
import random 
game.init()
c1,c2,c3=255,255,255
x1=1536
y1=864
size=(x1,y1)
dis=game.display.set_mode((size))
game.display.set_caption("Aim Lab From OLX")
score=0
x=50
y=108
state=0
while not state:
    dis.fill((c1,c2,c3))
    game.display.update()
    for event in game.event.get():
        if event.type==game.KEYDOWN:
            if game.KMOD_RSHIFT:
                state=1
    else:
        if event.type==game.MOUSEBUTTONDOWN:
            for i in range(0,100):
                x1=random.randint(100,620)
                y1=random.randint(100,620)
                c1=random.randint(0,255)
                c2=random.randint(0,225)
                c3=random.randint(0,255)
                dis.fill((c1,c2,c3))
game.quit()