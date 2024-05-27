import pygame as game
import random 
game.init()
c1,c2,c3=255,255,255
x1=1536
y1=864
size=(x1,y1)
dis=game.display.set_mode()
game.display.set_caption("Left Click For Surprise")
score=0
white=(255,255,255)
black=(0,0,0)
textcolour=(255,255,255)
dis.fill((c1,c2,c3))
font_style=game.font.SysFont("comicsansms",100)
text=font_style.render("FUCK YOU",True,textcolour)
state=0
text2colour=(0,0,0)
while not state:
    font2_style=game.font.SysFont("comicsansms",35)
    text2=font2_style.render("Hold Left click For Surprise",True,text2colour) 
    dis.blit(text2,(550,260))
    for event in game.event.get():
        if event.type==game.KEYDOWN:
            if game.KMOD_RSHIFT:
                state=1
    dis.blit(text,(566,360))
    game.display.update()
    if event.type==game.MOUSEBUTTONDOWN:
        dis.fill((0,0,0))
    elif event.type==game.MOUSEBUTTONUP:
        dis.fill((255,255,255))
game.quit()