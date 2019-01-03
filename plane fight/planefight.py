__author__ = 'Jeff\'s arcade'
import pygame
from pygame.locals import *
import sys
import random
import Buttons
pygame.init()

enemy_xaxis = [30,60,90,120,150]
enemy_yaxis = [0, -100, -200, -300, -400]
enemy_speed = [2,2,2,2,2]
bullets_xaxis = [0,0,0,0,0]
bullets_yaxis = [0,0,0,0,0]
bullets_delay = 3
bullets_count = 0
current_health = 10
current_add   = 1
current_difficulty = 1
alive         = True
point = 0;
hit = False
start_game = Buttons.Button()
Font = pygame.font.SysFont("Calibri", 40)
Font20 = pygame.font.SysFont("Calibri", 20)
Font15 = pygame.font.SysFont("Calibri", 15)
current = 0

for i in range(5):
    bullets_yaxis[i] = i * (100)
    bullets_xaxis[i] = 90
charactor_pos = [90,400]
screen_width = 200
screen_height = 500

charactor = pygame.image.load("textures//charactor.png")
enemy     = pygame.image.load("textures//enemy.png")
bullet    = pygame.image.load("textures//bullet.png")
boom      = pygame.image.load("textures//boom.png")
start     = pygame.image.load("textures//start.png")
base      = pygame.image.load("textures//base.png")
base_hit  = pygame.image.load("textures//base_hit.png")


screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("plane fight in Jeff's arcade")
pygame.display.set_icon(boom)

def draw_stage():
    global hit
    for xpos in range(len(enemy_xaxis)):
        screen.blit(enemy, (enemy_xaxis[xpos], enemy_yaxis[xpos]))
    for bxpos in range(len(bullets_xaxis)):
        if bullets_yaxis[bxpos] <= charactor_pos[1]:
            screen.blit(bullet, (bullets_xaxis[bxpos], bullets_yaxis[bxpos]))
    pygame.draw.rect(screen,(255,100,0),(5,5,current_health * 10, 5),0)
    if hit == True:
        screen.blit(base_hit,(0,425))
        hit = False
    elif hit == False:
        screen.blit(base,(0,400))
    screen.blit(charactor, (charactor_pos[0],charactor_pos[1]))

def hit_bullet(enemy_num):
    for i in range (5):
        if bullets_yaxis[i] < charactor_pos[1]:
            if enemy_xaxis[enemy_num] <= bullets_xaxis[i] and enemy_xaxis[enemy_num] + 21 >= bullets_xaxis[i]:
                if enemy_yaxis[enemy_num] <= bullets_yaxis[i] and enemy_yaxis[enemy_num] + 21 >= bullets_yaxis[i]:
                    return True
            elif enemy_xaxis[enemy_num] <= bullets_xaxis[i] + 3 and enemy_xaxis[enemy_num] + 21 >= bullets_xaxis[i] + 3:
                if enemy_yaxis[enemy_num] <= bullets_yaxis[i] and enemy_yaxis[enemy_num] + 21 >= bullets_yaxis[i]:
                    return True
    return False

def hit_enemy():
    global point
    for i in range(len(enemy_xaxis)):
        if hit_bullet(i) == True:
            screen.blit(boom,(enemy_xaxis[i], enemy_yaxis[i]))
            enemy_xaxis[i] = random.randint(0,175)
            enemy_yaxis[i] = -20
            if current_difficulty == 0:
                enemy_speed[i] = random.randint(1,2)
            elif current_difficulty == 1:
                enemy_speed[i] = random.randint(1,3)
            elif current_difficulty == 2:
                enemy_speed[i] = random.randint(2,6)
            elif current_difficulty == 3:
                enemy_speed[i] = random.randint(2,7)
            point += 20

def hit_charactor():
    for i in range(5):
        if charactor_pos[0] - 3 >= enemy_xaxis[i] and charactor_pos[0] + 3 <= enemy_xaxis[i] + 21:
            if charactor_pos[1] >= enemy_yaxis[i] + 5 and charactor_pos[1] <= enemy_yaxis[i] +16:
                return True;
        elif charactor_pos[0] + 18 >= enemy_xaxis[i] and charactor_pos[0] + 24 <= enemy_xaxis[i] + 21:
            if charactor_pos[1] >= enemy_yaxis[i] + 5 and charactor_pos[1] <= enemy_yaxis[i] +16:
                return True;

def keyboard_handler():
    keys_pressed = pygame.key.get_pressed()
    if keys_pressed[K_LEFT] and charactor_pos[0] >= 0:
        charactor_pos[0] -= 5
    if keys_pressed[K_RIGHT] and charactor_pos[0] <= 180:
        charactor_pos[0] += 5
    if keys_pressed[K_UP] and charactor_pos[1] >= 0:
        charactor_pos[1] -= 5
    if keys_pressed[K_DOWN] and charactor_pos[1] <= 480:
        charactor_pos[1] += 5

def summon_enemy():
    global current_health,hit
    for ii in range(5):
        enemy_yaxis[ii] += enemy_speed[ii]
        if enemy_yaxis[ii] >= 500:
            current_health -= 1
            hit = True
            enemy_yaxis[ii] = 0
            enemy_xaxis[ii] = random.randint(0,175)
            if current_difficulty == 0:
                enemy_speed[ii] = random.randint(1,2)
            elif current_difficulty == 1:
                enemy_speed[ii] = random.randint(1,3)
            elif current_difficulty == 2:
                enemy_speed[ii] = random.randint(2,6)
            elif current_difficulty == 3:
                enemy_speed[ii] = random.randint(2,7)

def summon_bullet():
    for i in range(len(bullets_xaxis)):
        if current_difficulty == 0:
            bullets_yaxis[i] -= 6
        elif current_difficulty == 1:
            bullets_yaxis[i] -= 6
        elif current_difficulty == 2:
            bullets_yaxis[i] -= 8
        elif current_difficulty == 3:
            bullets_yaxis[i] -= 9
        if bullets_yaxis[i] <= 0:
            bullets_xaxis[i] = charactor_pos[0] + 9
            bullets_yaxis[i] = screen_height
        elif bullets_yaxis[i] >= charactor_pos[1]:
            bullets_xaxis[i] = charactor_pos[0] + 9

start_game.create_button(screen,(255,255,255),70,100,56,30,2,"start",(0,0,0))
easy = Buttons.Button()
beginner = Buttons.Button()
hard = Buttons.Button()
insane = Buttons.Button()
diffcult = Buttons.Button()
easy.create_button(screen,(255,255,255),70,100,56,30,2,"easy",(0,0,0))
beginner.create_button(screen,(255,255,255),70,100,56,30,2,"beginner",(0,0,0))
hard.create_button(screen,(255,255,255),70,100,56,30,2,"hard",(0,0,0))
insane.create_button(screen,(255,255,255),70,100,56,30,2,"insane",(0,0,0))
diffcult.create_button(screen,(255,255,255),70,100,56,30,2,"diffculty",(0,0,0))
text = Font.render("game over", 1, (100,150,0))
text2= Font15.render("press space to main menu", 1, (150,150,50))
def starts():
    global current
    while True:
        pos = pygame.mouse.get_pos()
        screen.blit(start,(0,0))
        if start_game.pressed(pos) == True:
            start_game.create_button(screen,(0,0,0),70,100,56,30,2,"start",(255,255,255))
        else:
            start_game.create_button(screen,(255,255,255),70,100,56,30,2,"start",(0,0,0))
        if diffcult.pressed(pos) == True:
            diffcult.create_button(screen,(0,0,0),64,150,70,30,2,"diffculty",(255,255,255))
        else:
            diffcult.create_button(screen,(255,255,255),64,150,70,30,2,"diffculty",(0,0,0))
        pygame.display.flip()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == pygame.MOUSEBUTTONDOWN:
                if start_game.pressed(pos) == True:
                    current = 1
                    return
                elif diffcult.pressed(pos) == True:
                    current = 3
                    return
def game():
    global current,current_add,current_health,charactor_pos,enemy_xaxis,enemy_yaxis,enemy_speed,bullets_xaxis,bullets_yaxis,bullets_delay,bullets_count,alive,hit,point
    while True:
        screen.fill((255,255,255))
        points = Font15.render("you got:" + str(point) + " points", 1, (0,25,50))
        draw_stage()
        screen.blit(points, (0,20))
        keyboard_handler()
        summon_enemy()
        summon_bullet()
        hit_enemy()
        keys_pressed2 = pygame.key.get_pressed()
        if keys_pressed2[K_ESCAPE]:
            enemy_xaxis = [30,60,90,120,150]
            point = 0
            enemy_yaxis = [0, -100, -200, -300, -400]
            enemy_speed = [2,2,2,2,2]
            bullets_xaxis = [0,0,0,0,0]
            for i in range(5):
                bullets_yaxis[i] = i * (100)
                bullets_xaxis[i] = 90
            bullets_delay = 3
            bullets_count = 0
            current_health = 10
            current_add   = 1
            alive         = True
            charactor_pos = [90,400]
            hit = False
            current = 0
            return
        if point >= current_add * 1000 and current_health <= 20:
            if current_difficulty == 2:
                current_health += 2
                current_add    += 1
            elif current_difficulty == 0:
                current_health += 0.5
                current_add    += 1
            elif current_difficulty == 1:
                current_health += 1
                current_add    += 1
            elif current_difficulty == 3:
                current_health += 4
                current_add    += 1
        if hit_charactor() == True:
            current = 2
            return
        elif current_health == 0:
            current = 2
            return
        pygame.display.flip()
        pygame.time.wait(30)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
def difficulty():
    global current_difficulty,current
    screen.fill((255,255,255))
    while True:
        pos = pygame.mouse.get_pos()
        easy.create_button(screen,(255,255,255),70,100, 70,30,2,"easy",(0,0,0))
        beginner.create_button(screen,(255,255,255),70,150,70,30,2,"beginner",(0,0,0))
        hard.create_button(screen,(255,255,255),70,200,70,30,2,"hard",(0,0,0))
        insane.create_button(screen,(255,255,255),70,250,70,30,2,"insane",(0,0,0))
        pygame.display.flip()
        if current_difficulty == 0:
            easy.create_button(screen,(0,0,0),70,100,70,30,2,"easy",(255,255,255))
        elif current_difficulty == 1:
            beginner.create_button(screen,(0,0,0),70,150,70,30,2,"beginner",(255,255,255))
        elif current_difficulty == 2:
            hard.create_button(screen,(0,0,0),70,200,70,30,2,"hard",(255,255,255))
        elif current_difficulty == 3:
            insane.create_button(screen,(0,0,0),70,250,70,30,2,"insane",(255,255,255))
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == pygame.MOUSEBUTTONDOWN:
                if easy.pressed(pos) == True:
                    current_difficulty = 0
                    current = 0
                    return
                elif beginner.pressed(pos) == True:
                    current_difficulty = 1
                    current = 0
                    return
                elif hard.pressed(pos) == True:
                    current_difficulty = 2
                    current = 0
                    return
                elif insane.pressed(pos) == True:
                    current_difficulty = 3
                    current = 0
                    return
def gameover():
    global current,current_add,current_health,charactor_pos,enemy_xaxis,enemy_yaxis,enemy_speed,bullets_xaxis,bullets_yaxis,bullets_delay,bullets_count,alive,hit,point
    while True:
        screen.blit(text,(10,200))
        screen.blit(text2,(5,250))
        pygame.display.flip()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
        keys_pressed2 = pygame.key.get_pressed()
        if keys_pressed2[K_SPACE]:
            enemy_xaxis = [30,60,90,120,150]
            point = 0
            enemy_yaxis = [0, -100, -200, -300, -400]
            enemy_speed = [2,2,2,2,2]
            bullets_xaxis = [0,0,0,0,0]
            for i in range(5):
                bullets_yaxis[i] = i * (100)
                bullets_xaxis[i] = 90
            bullets_delay = 3
            bullets_count = 0
            current_health = 10
            current_add   = 1
            charactor_pos = [90,400]
            alive         = True
            hit = False
            current = 0
            return

while True:
   if current == 0:
       starts()
   elif current == 1:
       game()
   elif current == 2:
       gameover()
   elif current == 3:
       difficulty()
