__author__ = 'bo'
import pygame
from pygame.locals import *
pygame.init()
import sys
import time
import random
mine_length = 20
mine_width  = 20
mine_num    = random.randint(0,199)
if mine_num >= 400:
    mine_num = 400
current_stage= 0
start = time.time()
mines = [[9 for x in range(mine_width)] for x in range(mine_length)]
shows = [[0 for x in range(mine_width)] for x in range(mine_length)]
flags = [[0 for x in range(mine_width)] for x in range(mine_length)]
screen_width = mine_width * 20
screen_length= mine_length * 20
mine = pygame.image.load("textures//mine.png")
hide = pygame.image.load("textures//hide.png")
flag = pygame.image.load("textures//flag.png")
num1 = pygame.image.load("textures//num1.png")
num2 = pygame.image.load("textures//num2.png")
num3 = pygame.image.load("textures//num3.png")
num4 = pygame.image.load("textures//num4.png")
num5 = pygame.image.load("textures//num5.png")
num6 = pygame.image.load("textures//num6.png")
num7 = pygame.image.load("textures//num7.png")
num8 = pygame.image.load("textures//num8.png")
numbers = [num1,num2,num3,num4,num5,num6,num7,num8]
space= pygame.image.load("textures//space.png")

Font = pygame.font.SysFont("Calibri", 40)
Font20 = pygame.font.SysFont("Calibri", 20)
Font15 = pygame.font.SysFont("Calibri", 15)
text = Font.render("game over", 1, (0,0,0))
textw = Font.render("you win!!", 1, (0,0,0))

text2= Font15.render("press space to restart", 1, (0,0,0))

screen = pygame.display.set_mode((screen_width, screen_length))
pygame.display.set_caption("mine sweeper in Jeff's arcade")
pygame.display.set_icon(mine)

def summon_mines():
    for i in range(mine_num):
        xaxis = random.randint(0,mine_width-1)
        yaxis = random.randint(0,mine_length-1)
        while mines[xaxis][yaxis] == 0:
            xaxis = random.randint(0,mine_width-1)
            yaxis = random.randint(0,mine_length-1)
        mines[xaxis][yaxis] = 0

def summon_nums():
    mines_count = 0
    for i in range(mine_width):
        for ii in range(mine_length):
            if mines[i][ii] != 0:
                if ii-1 >= 0:
                    if mines[i][ii-1] == 0:
                        mines_count += 1
                    if i-1 >= 0:
                        if mines[i-1][ii-1] == 0:
                            mines_count += 1
                    if i+1 < mine_width:
                        if mines[i+1][ii-1] == 0:
                            mines_count += 1
                if ii+1 < mine_length:
                    if mines[i][ii+1] == 0:
                        mines_count += 1
                    if i-1 >= 0:
                        if mines[i-1][ii+1] == 0:
                            mines_count += 1
                    if i+1 < mine_width:
                        if mines[i+1][ii+1] == 0:
                            mines_count += 1
                if i+1 < mine_width:
                    if mines[i+1][ii] == 0:
                        mines_count += 1
                if i-1 >= 0:
                    if mines[i-1][ii] == 0:
                        mines_count += 1
                if mines_count != 0:
                    mines[i][ii] = mines_count
                mines_count = 0

def draw_stage():
    screen.fill((0,0,0))
    for i in range(mine_width):
        for ii in range(mine_length):
            if shows[i][ii] == 1:
                if mines[i][ii] == 0:
                    screen.blit(mine,(i*20,ii*20))
                elif mines[i][ii] == 9:
                    screen.blit(space,(i*20,ii*20))
                elif mines[i][ii] >= 1 and mines[i][ii] <= 8:
                    screen.blit(numbers[mines[i][ii] - 1], (i*20,ii*20))
            else:
                if flags[i][ii] == 1:
                    screen.blit(flag,(i*20,ii*20))
                else:
                    screen.blit(hide,(i*20,ii*20))

def click_handler():
    pos = pygame.mouse.get_pos()
    button = pygame.mouse.get_pressed()
    for xaxis in range(mine_width):
        for yaxis in range(mine_length):
            if button == (1,0,0):
                if xaxis*20 <= pos[0] and xaxis*20+20 > pos[0]:
                    if yaxis*20 <= pos[1] and yaxis*20+20 > pos[1]:
                        shows[xaxis][yaxis] = 1
            elif button == (0,0,1):
                if xaxis*20 <= pos[0] and xaxis*20+20 > pos[0]:
                    if yaxis*20 <= pos[1] and yaxis*20+20 > pos[1]:
                        if flags[xaxis][yaxis] == 0:
                            flags[xaxis][yaxis] = 1
                        else:
                            flags[xaxis][yaxis] = 0
            elif button == (1,0,1):
                if xaxis*20 <= pos[0] and xaxis*20+20 > pos[0]:
                    if yaxis*20 <= pos[1] and yaxis*20+20 > pos[1]:
                        if shows[xaxis][yaxis] == 1:
                            show_double(xaxis,yaxis)

def show_around(x,y):
    if x + 1 < mine_width:
        if mines[x+1][y] == 9:
            shows[x+1][y] = 1
        if y+1 < mine_length:
            if mines[x+1][y+1] == 9:
                shows[x+1][y+1] = 1
        if y-1 >= 0:
            if mines[x+1][y-1] == 9:
                shows[x+1][y-1] = 1
    if x - 1 >= 0:
        if mines[x-1][y] == 9:
            shows[x-1][y] = 1
        if y+1 < mine_length:
            if mines[x-1][y+1] == 9:
                shows[x-1][y+1] = 1
        if y-1 >= 0:
            if mines[x-1][y-1] == 9:
                shows[x-1][y-1] = 1
    if y + 1 < mine_length:
        if mines[x][y+1] == 9:
            shows[x][y+1] = 1
    if y - 1 >= 0:
        if mines[x][y-1] == 9:
            shows[x][y-1] = 1

def show_num(x,y):
    if x + 1 < mine_width:
        if mines[x+1][y] != 9 and mines[x+1][y] != 0:
            shows[x+1][y] = 1
        if y+1 < mine_length:
            if mines[x+1][y+1] != 9 and mines[x+1][y+1] != 0:
                shows[x+1][y+1] = 1
        if y-1 >= 0:
            if mines[x+1][y-1] != 9 and mines[x+1][y-1] != 0:
                shows[x+1][y-1] = 1
    if x - 1 >= 0:
        if mines[x-1][y] != 9 and mines[x-1][y] != 0:
            shows[x-1][y] = 1
        if y+1 < mine_length:
            if mines[x-1][y+1] != 9 and mines[x-1][y+1] != 0:
                shows[x-1][y+1] = 1
        if y-1 >= 0:
            if mines[x-1][y-1] != 9 and mines[x-1][y-1] != 0:
                shows[x-1][y-1] = 1
    if y + 1 < mine_length:
        if mines[x][y+1] != 9 and mines[x][y+1] != 0:
            shows[x][y+1] = 1
    if y - 1 >= 0:
        if mines[x][y-1] != 9 and mines[x][y-1] != 0:
            shows[x][y-1] = 1

def show_double(i,ii):
    mines_count = 0
    if mines[i][ii] != 0 and mines[i][ii] != 9 and shows[i][ii] == 1:
          if ii-1 >= 0:
              if mines[i][ii-1] == 0 and flags[i][ii-1] == 1:
                  mines_count += 1
              if i-1 >= 0:
                  if mines[i-1][ii-1] == 0 and flags[i-1][ii-1] == 1:
                      mines_count += 1
              if i+1 < mine_width:
                  if mines[i+1][ii-1] == 0 and flags[i+1][ii-1] == 1:
                      mines_count += 1
          if ii+1 < mine_length:
              if mines[i][ii+1] == 0 and flags[i][ii+1] == 1:
                  mines_count += 1
              if i-1 >= 0:
                  if mines[i-1][ii+1] == 0 and flags[i-1][ii+1] == 1:
                      mines_count += 1
              if i+1 < mine_width:
                  if mines[i+1][ii+1] == 0 and flags[i+1][ii+1] == 1:
                      mines_count += 1
          if i+1 < mine_width:
              if mines[i+1][ii] == 0 and flags[i+1][ii] == 1:
                  mines_count += 1
          if i-1 >= 0:
              if mines[i-1][ii] == 0 and flags[i-1][ii] == 1:
                  mines_count += 1
    if mines_count == mines[i][ii]:
        if ii-1 >= 0:
            if mines[i][ii-1] != 0:
                shows[i][ii-1] = 1
            if i-1 >= 0:
                if mines[i-1][ii-1] != 0:
                    shows[i-1][ii-1] = 1
            if i+1 < mine_width:
                if mines[i+1][ii-1] != 0:
                    shows[i+1][ii-1] = 1
        if ii+1 < mine_length:
            if mines[i][ii+1] != 0:
                shows[i][ii+1] = 1
            if i-1 >= 0:
                if mines[i-1][ii+1] != 0:
                    shows[i-1][ii+1] = 1
            if i+1 < mine_width:
                if mines[i+1][ii+1] != 0:
                    shows[i+1][ii+1] = 1
        if i-1 >= 0:
            if mines[i-1][ii] != 0:
                shows[i-1][ii] = 1
        if i+1 < mine_width:
            if mines[i+1][ii] != 0:
                shows[i+1][ii] = 1

def show_all():
    for i in range(mine_width):
        for ii in range(mine_length):
            if mines[i][ii] == 9 and shows[i][ii] == 1:
                show_around(i,ii)
                show_num(i,ii)

def win():
    count = 0
    for i in range(mine_width):
        for ii in range(mine_length):
            if shows[i][ii] == 1:
                count += 1
    if count == mine_width * mine_length - mine_num:
        return True
    else:
        return False

def lose():
    for i in range(mine_width):
        for ii in range(mine_length):
            if shows[i][ii] == 1:
                if mines[i][ii] == 0:
                    return True

summon_mines()
summon_nums()

def game():
    global current_stage,mines,shows,flags,start
    while True:
        keys_pressed = pygame.key.get_pressed()
        show_all()
        if keys_pressed[K_SPACE]:
            start = time.time()
            mines = [[9 for x in range(mine_width)] for x in range(mine_length)]
            shows = [[0 for x in range(mine_width)] for x in range(mine_length)]
            flags = [[0 for x in range(mine_width)] for x in range(mine_length)]
            summon_mines()
            summon_nums()
        if win() == True:
            current_stage = 1
            return
        elif lose() == True:
            current_stage = 2
            return
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == pygame.MOUSEBUTTONDOWN:
                click_handler()
        draw_stage()
        pygame.display.flip()

def wingame():
    global current_stage,mines,shows,flags,start
    time_used = time.time()-start
    times = Font15.render("you used " + str(int(time_used)) + " seconds",1,(0,0,0))
    while True:
        screen.blit(textw,(130,170))
        screen.blit(text2,(135,210))
        screen.blit(times,(135,250))
        pygame.display.flip()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
        keys_pressed = pygame.key.get_pressed()
        if keys_pressed[K_SPACE]:
            start = time.time()
            mines = [[9 for x in range(mine_width)] for x in range(mine_length)]
            shows = [[0 for x in range(mine_width)] for x in range(mine_length)]
            flags = [[0 for x in range(mine_width)] for x in range(mine_length)]
            summon_mines()
            summon_nums()
            current_stage = 0
            return

def losegame():
    global current_stage,mines,shows,flags,start
    while True:
        screen.blit(text,(130,170))
        screen.blit(text2,(135,210))
        pygame.display.flip()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
        keys_pressed = pygame.key.get_pressed()
        if keys_pressed[K_SPACE]:
            start = time.time()
            mines = [[9 for x in range(mine_width)] for x in range(mine_length)]
            shows = [[0 for x in range(mine_width)] for x in range(mine_length)]
            flags = [[0 for x in range(mine_width)] for x in range(mine_length)]
            summon_mines()
            summon_nums()
            current_stage = 0
            return
while True:
    if current_stage == 0:
        game()
    elif current_stage == 1:
        wingame()
    elif current_stage == 2:
        losegame()
