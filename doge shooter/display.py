from lzma import CHECK_CRC32
import pygame as game
import random
import time
import pyautogui as gui
import keyboard
from pygame import image

game.init()
clock = game.time.Clock()
starttime = 1000
curr = False
active = False
done = False
health = 90
kill = 0
c1, c2, c3 = 255, 255, 255
x1=1920
y1=1080
#x1 = 1600
#y1 = 900
size = (x1, y1)
white = (c1, c2, c3)
dis = game.display.set_mode((size))
game.display.set_caption("Aim Lab Doge version")
score = 0
x = 750
y = 388
xx, yy = 0, 0
yellow = (0, 0, 125)
black = (0, 0, 0)
textcolour = ((0, 0, 0))
font_style = game.font.SysFont("comicsansms", 35)
font_stylesmall = game.font.SysFont("comicsansms", 12)
win = font_style.render("Damn that was Fast!", True, white, black)
lose = font_style.render("Bruh you're too slow!", True, white, black)
text = font_style.render("Shoot Doge in the head once to kill Or Shoot thrice in his body to kill", True, white, black)
start = font_style.render("Press any key to start", True, white, black)
playname = font_style.render("Enter your name and hit 'ENTER'", True, black)
tip = font_stylesmall.render("*left click on the input box to type your name*", True, black)
end = font_style.render("Press ESC to Quit", True, white, black)
state = 0
h = 1
k = 0
health = 1000
while h == 1:
    font = game.font.Font(None, 32)
    clock = game.time.Clock()
    input_box = game.Rect(830, 450, 140, 40)
    color_inactive = black
    color_active = yellow
    color = color_inactive
    active = False
    name = ''
    done = False

    while not done:
        for event in game.event.get():
            if event.type == game.QUIT:
                done = True
            if event.type == game.MOUSEBUTTONDOWN:
                # If the user clicked on the input_box rect.
                if input_box.collidepoint(event.pos):
                    # Toggle the active variable.
                    active = not active
                else:
                    active = False
                # Change the current color of the input box.
                color = color_active if active else color_inactive
            if event.type == game.KEYDOWN:
                if active:
                    if event.key == game.K_RETURN:
                        print(name)
                        h=0
                        done = True
                    elif event.key == game.K_BACKSPACE:
                        name = name[:-1]
                    else:
                        name += event.unicode

        dis.fill(white)
        # Render the current text.
        txt_surface = font.render(name, True, color)
        # Resize the box if the text is too long.
        width = max(250, txt_surface.get_width() + 10)
        input_box.w = width
        # Blit the text.
        dis.blit(playname,(input_box.x-115,input_box.y-60))
        dis.blit(tip, (input_box.x-5, input_box.y + 40))
        dis.blit(txt_surface, (input_box.x + 5, input_box.y + 7))
        # Blit the input_box rect.
        game.draw.rect(dis, color, input_box, 5)

        game.display.flip()
        clock.tick(30)

while not state:
    for event in game.event.get():
        if event.type == game.KEYDOWN:
            if event.key == game.K_ESCAPE:
                state = 1
    a, b = game.mouse.get_pos()
    start_time = time.time()
    starttime -= 1
    head = game.Rect(x - 11, y - 8, 30, 28)
    body = game.Rect(x - 13, y + 20, 35, 45)
    doge = image.load("dogeee.png")
    hole = image.load("hole.png")
    gun = image.load("gunnnnn.png")
    blood = image.load("blood.png")
    cur = game.Rect(a, b, 10, 10)
    dis.fill((c1, c2, c3))
    dis.blit(gun, (530, 720))
    dis.blit(doge, (x - 35, y - 13))
    # game.draw.rect(dis, yellow, head, 3)
    dis.blit(end, (0, 0))
    # game.draw.rect(dis, yellow, body, 3)
    # dis.blit(text, (600, 28))
    pname = font_style.render("PLAYER NAME :" + name, True, black)
    text2 = font_style.render("Score:" + str(score), True, textcolour)
    text3 = font_style.render("DOGE HEALTH:" + str(health), True, textcolour)
    text4 = font_style.render("time :" + str(starttime), True, white,black)
    dis.blit(text4, (1765, 0))
    dis.blit(pname, (350, 0))
    dis.blit(text2, (920, 0))
    dis.blit(text3, (1250, 0))
    if cur.colliderect(head) or cur.colliderect(body):
        curr = True
    else:
        curr = False
        if event.type == game.MOUSEBUTTONDOWN:
            dis.blit(hole, (a - 23, b - 17))
            game.display.update()
            time.sleep(0.1)
    game.display.update()
    time.sleep(0.05)
    if cur.colliderect(head):
        if event.type == game.MOUSEBUTTONDOWN:
            health -= 25
            dis.blit(blood, (x - 23, y - 13))
            game.display.update()
            time.sleep(0.1)
            x = random.randint(400, 800)
            y = random.randint(250, 500)
    elif cur.colliderect(body):
        if event.type == game.MOUSEBUTTONDOWN:
            health -= 50
            dis.blit(blood, (x - 25, y + 25))
            game.display.update()
            time.sleep(0.1)
            x = random.randint(400, 800)
            y = random.randint(250, 500)
    if starttime<=0:
        game.quit()
    clock.tick(60)
game.quit()
