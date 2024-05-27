import pygame as game
#import win32api
import random
import time
import pyautogui as py
import keyboard

game.init()
x = 9
y = 90
white = (255, 255, 255)
blue = (0, 0, 255)
black = (0, 0, 0)
posx = 100
posy = 100
font = game.font.SysFont("comicsansms", 35)
bfont = game.font.SysFont("comicsansms", 61)
yestext = bfont.render("Yeah That's what i thought You Dumb Piece of SHIT", True, white, black)
canceltext = bfont.render("You're not so Dumb after all", True, white, black)
start = bfont.render("Press ENTER to start", True, white, black)
d = game.display.set_mode()
error = game.image.load("error2.png")
ye = game.image.load("yes.png")
n = game.image.load("no.png")
g = 0
h = 1
game.mouse.set_visible(0)
displayyes = False
displaycancel = False
gamecomplete = 0
posyes = (320, 355)
posno = (600, 355)
x1, y1 = 320, 355
x2, y2 = 600, 355
x3, y3 = 793, 114
while not g:
    for event in game.event.get():
        if event.type == game.KEYDOWN:
            if event.key == game.K_ESCAPE:
                g = 1
    while h == 1:
        d.fill(white)
        d.blit(start, (560, 420))
        game.display.flip()
        if keyboard.is_pressed("enter"):
            h = 0
    text = font.render(" " + str(x) + "," + str(y), True, (0, 0, 0))
    err = game.transform.scale(error, (303 * 2.5, 150 * 2.5))
    yes = game.transform.scale(ye, (60 * 2, 23 * 2))
    no = game.transform.scale(n, (60 * 2, 23 * 2))
    d.fill(black)
    game.mouse.set_visible(1)
    d.blit(text, (0, 0))
    cur = game.Rect(x, y, 10, 10)
    d.blit(err, (posx, posy))
    d.blit(yes, (posyes))
    d.blit(no, (x2, y2))
    w1, w2, w3, w4 = yes.get_rect()
    yess = game.Rect(x1, y1, w3, w4)
    noo = game.Rect(x2, y2, w3, w4)
    cancel = game.Rect(x3, y3, 51, w4 + 3)
    # game.draw.rect(d,black,yess)
    # game.draw.rect(d,black,noo)
    # game.draw.rect(d,blue,cur)
    # game.draw.rect(d,black,cancel)
    x, y = game.mouse.get_pos()
    if cur.colliderect(yess):
        if event.type == game.MOUSEBUTTONDOWN:
            displayyes = True
    elif cur.colliderect(cancel):
        if event.type == game.MOUSEBUTTONDOWN:
            displaycancel = True
    if displayyes == True:
        d.fill((0, 0, 0))
        posx = 10000
        posy = 10000
        posyes = (1000, 1000)
        posno = (1000, 1000)
        x1, y1 = 1000, 1000
        x2, y2 = 1000, 1000
        x3, y3 = 1000, 1000
        d.blit(yestext, (20, 350))
        gamecomplete = 1
    if displaycancel == True:
        posx = 10000
        posy = 10000
        posyes = (1000, 1000)
        posno = (1000, 1000)
        x1, y1 = 1000, 1000
        x2, y2 = 1000, 1000
        x3, y3 = 1000, 1000
        d.fill((0, 0, 0))
        d.blit(canceltext, (382, 350))
        gamecomplete = 1
    if cur.colliderect(noo):
        x2 = random.randint(227, 739)
        y2 = random.randint(240, 403)
    game.display.flip()
    if gamecomplete == 1:
        time.sleep(4)
        g = 1

game.quit()

if display++true:
    pos=10000
    posy=1000
    posyes=1000
    posu=1000
    x1,y1,=10.
    
