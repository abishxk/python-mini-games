from lzma import CHECK_CRC32
import pygame as game
import random
import time
import pyautogui as gui
import keyboard
from pygame import image

game.init()
health = 90
kill = 0
c1, c2, c3 = 255, 255, 255
# x1=1536
# y1=864
x1 = 1600
y1 = 900
size = (x1, y1)
white = (c1, c2, c3)
dis = game.display.set_mode((size))
game.display.set_caption("Aim Lab Doge version")
score = 0
x = 750
y = 388
xx,yy=0,0
yellow = (0, 0, 125)
black = (0, 0, 0)
textcolour = ((0, 0, 0))
font_style = game.font.SysFont("comicsansms", 35)
text = font_style.render("Shoot Doge in the head once to kill Or Shoot thrice in his body to kill", True, white, black)
start = font_style.render("Press any key to start", True, white, black)
end = font_style.render("Press ESC to Quit", True, white, black)
state = 0
h = 1
health = 90
while h == 1:
    dis.fill(white)
    dis.blit(start, (590, 420))
    dis.blit(text, (220, 28))
    game.display.flip()
    for event in game.event.get():
        if event.type == game.KEYDOWN:
            h = 0
dis.fill(white)
while not state:
    for event in game.event.get():
        if event.type == game.KEYDOWN:
            if event.key == game.K_ESCAPE:
                state = 1
    a, b = game.mouse.get_pos()
    head = game.Rect(x-11, y-10, 30, 30)
    body = game.Rect(x-13, y+20, 35, 45)
    doge = image.load("dogeee.png")
    hole = image.load("hole.png")
    gun = image.load("gun.png")
    blood = image.load("blood.png")
    cur = game.Rect(a, b, 10, 10)
    dis.fill((c1, c2, c3))
    dis.blit(gun, (500, 622))
    dis.blit(doge, (x - 35, y - 13))
    #game.draw.rect(dis, yellow, head, 3)
    dis.blit(end, (0, 0))
    #game.draw.rect(dis, yellow, body, 3)
    # dis.blit(text, (600, 28))
    text2 = font_style.render("KILLS:" + str(score), True, textcolour)
    text3 = font_style.render("DOGE HEALTH:" + str(health), True, textcolour)
    dis.blit(text2, (750, 28))
    dis.blit(text3, (1000, 28))
    if health <= 60:
        dis.blit(blood, (x-25, y+25))
    if health <= 30:
        dis.blit(blood, (x-15, y+25))
    if health < 30:
        dis.blit(blood, (x-7, y+35))
    game.display.update()
    time.sleep(0.05)
    if cur.colliderect(head):
        if event.type == game.MOUSEBUTTONDOWN:
            health -= 90
            xx=x
            yy=y
            if health <= 0:
                dis.blit(blood,(x-23,y-13))
                game.display.update()
                time.sleep(0.1)
                score += 1
                x = random.randint(400, 800)
                y = random.randint(250, 500)
                health += 90
    elif cur.colliderect(body):
        if event.type == game.MOUSEBUTTONDOWN:
            health -= 30
            time.sleep(0.1)
            if health == 0:
                score += 1
                x = random.randint(400, 800)
                y = random.randint(250, 500)
                health+=90
    else:
        if event.type == game.MOUSEBUTTONDOWN:
            dis.blit(hole, (x, y))

game.quit()
