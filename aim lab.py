from lzma import CHECK_CRC32
import pygame as game
import random 
import keyboard
game.init()
kill=0
c1,c2,c3=255,255,255
#x1=1536
#y1=864
x1=1600
y1=900
size=(x1,y1)
dis=game.display.set_mode((size))
game.display.set_caption("Aim Lab From OLX")
score=0
x=750
y=388
yellow=(0,0,125)
textcolour=((0,0,0))
font_style=game.font.SysFont("comicsansms",35)
text=font_style.render("TRAINING RANGE", True,textcolour)
state=0
while not state:
    for event in game.event.get():
        if event.type==game.KEYDOWN:
            if game.KMOD_LSHIFT:
                state=1
    a,b=game.mouse.get_pos()
    coins=game.Rect(x,y,10,10)
    cur=game.Rect(a,b,10,10)
    dis.fill((c1,c2,c3))
    game.draw.rect(dis, yellow, coins,5)
    dis.blit(text,(600,28))
    text2=font_style.render("score:"+str(score),True,textcolour)
    dis.blit(text2,(0,0))
    game.display.update()
    if cur.colliderect(coins):
        if event.type==game.MOUSEBUTTONDOWN:
            score+=1
            x=random.randint(400,800)
            y=random.randint(250,500)
            c1=random.randint(100,255)
            c2=random.randint(100,225)
            c3=random.randint(100,255)
            dis.fill((c1,c2,c3))
            
        
game.quit()
