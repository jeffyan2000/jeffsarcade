__author__ = 'bo'
import pygame
import sys
import random
from pygame.locals import *
import Buttons
body = pygame.image.load("textures//body.png")
tail = pygame.image.load("textures//tail.png")
head = pygame.image.load("textures//head.png")
food = pygame.image.load("textures//food.png")
turn = pygame.image.load("textures//body_turn.png")
start= pygame.image.load("textures//start.png")
body_list = []
tail_list = []
head_list = []
turn_list = []
#up
body_list.append(pygame.transform.rotate(body,-90))
tail_list.append(pygame.transform.rotate(tail,-90))
head_list.append(pygame.transform.rotate(head,-90))
turn_list.append(pygame.transform.rotate(turn,-90))
#down
body_list.append(pygame.transform.rotate(body,-270))
tail_list.append(pygame.transform.rotate(tail,-270))
head_list.append(pygame.transform.rotate(head,-270))
turn_list.append(pygame.transform.rotate(turn,-270))
#right
body_list.append(pygame.transform.rotate(body,-180))
tail_list.append(pygame.transform.rotate(tail,-180))
head_list.append(pygame.transform.rotate(head,-180))
turn_list.append(pygame.transform.rotate(turn,-180))
#left
body_list.append(pygame.transform.rotate(body,0))
tail_list.append(pygame.transform.rotate(tail,0))
head_list.append(pygame.transform.rotate(head,0))
turn_list.append(pygame.transform.rotate(turn,0))

whole_xaxis = [30,30,30,30,30,30,30,30,30,30,30,30,30,30,30,30,30,30]
whole_yaxis = [30,31,32,33,34,35,36,37,38,39,40,41,42,43,44,45,46,47]
current_dir = [0 , 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
current_stage = 0
current_direction = 0
current_difficulty= 1
delay = 8
delay_count = 0
point = 0
food_pos = [40,30]
food_pos2= [50,30]
screen_width = 420 #60 SU
screen_length = 420#60 SU
screen = pygame.display.set_mode((screen_width, screen_length))
pygame.display.set_caption("the snake in Jeff's arcade")
pygame.display.set_icon(head)

def move_snake():
    del whole_xaxis[len(whole_xaxis) - 1]
    del whole_yaxis[len(whole_yaxis) - 1]
    del current_dir[len(current_dir) - 1]
    if current_direction == 0:                      #up
        whole_xaxis.insert(0,whole_xaxis[0])
        whole_yaxis.insert(0,whole_yaxis[0] - 1)
    elif current_direction == 1:                    #down
        whole_xaxis.insert(0,whole_xaxis[0])
        whole_yaxis.insert(0,whole_yaxis[0] + 1)
    elif current_direction == 2:                    #right
        whole_xaxis.insert(0,whole_xaxis[0] + 1)
        whole_yaxis.insert(0,whole_yaxis[0])
    elif current_direction == 3:                    #left
        whole_xaxis.insert(0,whole_xaxis[0] - 1)
        whole_yaxis.insert(0,whole_yaxis[0])
    current_dir.insert(0,current_direction)
    current_dir[len(whole_xaxis) - 1] = current_dir[len(whole_xaxis) - 2]

def draw_snake():
    screen.blit(head_list[current_dir[0]],(whole_xaxis[0] * 7,whole_yaxis[0] * 7))
    for i in range(len(whole_xaxis) - 2):
        if current_dir[i + 1] == current_dir[i]:
            screen.blit(body_list[current_dir[i+1]],(whole_xaxis[i+1]*7,(whole_yaxis[i+1]*7)))
        else:
            if current_dir[i] == 0:
                if current_dir[i + 1] == 3:
                    screen.blit(turn_list[3],(whole_xaxis[i+1]*7,(whole_yaxis[i+1]*7)))
                elif current_dir[i + 1] == 2:
                    screen.blit(turn_list[1],(whole_xaxis[i+1]*7,(whole_yaxis[i+1]*7)))
            elif current_dir[i] == 1:
                if current_dir[i + 1] == 3:
                    screen.blit(turn_list[0],(whole_xaxis[i+1]*7,(whole_yaxis[i+1]*7)))
                elif current_dir[i + 1] == 2:
                    screen.blit(turn_list[2],(whole_xaxis[i+1]*7,(whole_yaxis[i+1]*7)))
            elif current_dir[i] == 2:
                if current_dir[i + 1] == 1:
                    screen.blit(turn_list[3],(whole_xaxis[i+1]*7,(whole_yaxis[i+1]*7)))
                elif current_dir[i + 1] == 0:
                    screen.blit(turn_list[0],(whole_xaxis[i+1]*7,(whole_yaxis[i+1]*7)))
            elif current_dir[i] == 3:
                if current_dir[i + 1] == 1:
                    screen.blit(turn_list[1],(whole_xaxis[i+1]*7,(whole_yaxis[i+1]*7)))
                elif current_dir[i + 1] == 0:
                    screen.blit(turn_list[2],(whole_xaxis[i+1]*7,(whole_yaxis[i+1]*7)))
    screen.blit(tail_list[current_dir[len(current_dir)-1]],(whole_xaxis[len(whole_xaxis)-1]*7,whole_yaxis[len(whole_yaxis)-1]*7))

def food_cal():
    global point
    if whole_xaxis[0] == food_pos[0]:
        if whole_yaxis[0] == food_pos[1]:
            point += 1
            food_pos[0] = random.randint(1,58)
            food_pos[1] = random.randint(1,58)
            if current_dir[len(current_dir) - 1] == 0:
                whole_xaxis.append(whole_xaxis[len(whole_xaxis) - 1])
                whole_yaxis.append(whole_yaxis[len(whole_yaxis) - 1] + 1)
                current_dir.append(0)
            elif current_dir[len(current_dir) - 1] == 1:
                whole_xaxis.append(whole_xaxis[len(whole_xaxis) - 1])
                whole_yaxis.append(whole_yaxis[len(whole_yaxis) - 1] - 1)
                current_dir.append(1)
            elif current_dir[len(current_dir) - 1] == 2:
                whole_xaxis.append(whole_xaxis[len(whole_xaxis) - 1] - 1)
                whole_yaxis.append(whole_yaxis[len(whole_yaxis) - 1])
                current_dir.append(2)
            elif current_dir[len(current_dir) - 1] == 3:
                whole_xaxis.append(whole_xaxis[len(whole_xaxis) - 1] + 1)
                whole_yaxis.append(whole_yaxis[len(whole_yaxis) - 1])
                current_dir.append(3)
    elif whole_xaxis[0] == food_pos2[0]:
        if whole_yaxis[0] == food_pos2[1]:
            point += 1
            food_pos2[0] = random.randint(1,58)
            food_pos2[1] = random.randint(1,58)
            if current_dir[len(current_dir) - 1] == 0:
                whole_xaxis.append(whole_xaxis[len(whole_xaxis) - 1])
                whole_yaxis.append(whole_yaxis[len(whole_yaxis) - 1] + 1)
                current_dir.append(0)
            elif current_dir[len(current_dir) - 1] == 1:
                whole_xaxis.append(whole_xaxis[len(whole_xaxis) - 1])
                whole_yaxis.append(whole_yaxis[len(whole_yaxis) - 1] - 1)
                current_dir.append(1)
            elif current_dir[len(current_dir) - 1] == 2:
                whole_xaxis.append(whole_xaxis[len(whole_xaxis) - 1] - 1)
                whole_yaxis.append(whole_yaxis[len(whole_yaxis) - 1])
                current_dir.append(2)
            elif current_dir[len(current_dir) - 1] == 3:
                whole_xaxis.append(whole_xaxis[len(whole_xaxis) - 1] + 1)
                whole_yaxis.append(whole_yaxis[len(whole_yaxis) - 1])
                current_dir.append(3)
    screen.blit(food,(food_pos[0] * 7, food_pos[1] * 7))
    screen.blit(food,(food_pos2[0] * 7, food_pos2[1] * 7))

def die():
    if whole_xaxis[0] >= 60 or whole_xaxis[0] < 0:
        return True
    if whole_yaxis[0] >= 60 or whole_yaxis[0] < 0:
        return True
    for i in range (len(whole_xaxis) - 1):
        if whole_xaxis[i+1] == whole_xaxis[0]:
            if whole_yaxis[i+1] == whole_yaxis[0]:
                return True

def keyboard_handler():
    global current_direction
    keys_pressed = pygame.key.get_pressed()
    if keys_pressed[K_LEFT] and current_dir[0] != 2:
        current_direction = 3
    elif keys_pressed[K_RIGHT] and current_dir[0] != 3:
        current_direction = 2
    elif keys_pressed[K_UP] and current_dir[0] != 1:
        current_direction = 0
    elif keys_pressed[K_DOWN] and current_dir[0] != 0:
        current_direction = 1

start_game = Buttons.Button()
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

def game():
    global whole_xaxis,whole_yaxis,current_dir,current_stage,current_direction,point,food_pos,delay_count
    while True:
        delay_count += 1
        if delay_count == delay:
            screen.fill((255,255,255))
            points = Font15.render("you got:" + str(point) + " points", 1, (0,25,50))
            screen.blit(points, (0,20))
            food_cal()
            move_snake()
            draw_snake()
            if die() == True:
                current_stage = 2
                return
            pygame.display.flip()
            delay_count = 0
        keyboard_handler()
        pygame.time.wait(20)
        keys_pressed2 = pygame.key.get_pressed()
        if keys_pressed2[K_ESCAPE]:
            whole_xaxis = [30,30,30,30,30,30,30,30,30,30,30,30,30,30,30,30,30,30]
            whole_yaxis = [30,31,32,33,34,35,36,37,38,39,40,41,42,43,44,45,46,47]
            current_dir = [0 , 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
            current_stage = 0
            current_direction = 0
            point = 0
            delay_count = 0
            food_pos = [40,30]
            return
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

def starts():
    global current_stage
    while True:
        pos = pygame.mouse.get_pos()
        screen.blit(start,(0,0))
        if start_game.pressed(pos) == True:
            start_game.create_button(screen,(0,0,0),120,320,56,30,2,"start",(255,255,255))
        else:
            start_game.create_button(screen,(255,255,255),120,320,56,30,2,"start",(0,0,0))
        if diffcult.pressed(pos) == True:
            diffcult.create_button(screen,(0,0,0),250,320,70,30,2,"diffculty",(255,255,255))
        else:
            diffcult.create_button(screen,(255,255,255),250,320,70,30,2,"diffculty",(0,0,0))
        pygame.display.flip()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == pygame.MOUSEBUTTONDOWN:
                if start_game.pressed(pos) == True:
                    current_stage = 1
                    return
                elif diffcult.pressed(pos) == True:
                    current_stage = 3
                    return

def difficulty():
    global current_difficulty,current_stage,delay
    screen.blit(start,(0,0))
    while True:
        pos = pygame.mouse.get_pos()
        easy.create_button(screen,(255,255,255),180,100, 70,30,2,"easy",(0,0,0))
        beginner.create_button(screen,(255,255,255),180,150,70,30,2,"beginner",(0,0,0))
        hard.create_button(screen,(255,255,255),180,200,70,30,2,"hard",(0,0,0))
        insane.create_button(screen,(255,255,255),180,250,70,30,2,"insane",(0,0,0))
        pygame.display.flip()
        if current_difficulty == 0:
            easy.create_button(screen,(0,0,0),180,100,70,30,2,"easy",(255,255,255))
        elif current_difficulty == 1:
            beginner.create_button(screen,(0,0,0),180,150,70,30,2,"beginner",(255,255,255))
        elif current_difficulty == 2:
            hard.create_button(screen,(0,0,0),180,200,70,30,2,"hard",(255,255,255))
        elif current_difficulty == 3:
            insane.create_button(screen,(0,0,0),180,250,70,30,2,"insane",(255,255,255))
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == pygame.MOUSEBUTTONDOWN:
                if easy.pressed(pos) == True:
                    current_difficulty = 0
                    current_stage = 0
                    delay = 10
                    return
                elif beginner.pressed(pos) == True:
                    current_difficulty = 1
                    current_stage = 0
                    delay = 8
                    return
                elif hard.pressed(pos) == True:
                    current_difficulty = 2
                    current_stage = 0
                    delay = 6
                    return
                elif insane.pressed(pos) == True:
                    current_difficulty = 3
                    current_stage = 0
                    delay = 4
                    return

Font = pygame.font.SysFont("Calibri", 40)
Font20 = pygame.font.SysFont("Calibri", 20)
Font15 = pygame.font.SysFont("Calibri", 15)
text = Font.render("game over", 1, (100,150,0))
text2= Font15.render("press space to main menu", 1, (150,150,50))

def gameover():
    global whole_xaxis,whole_yaxis,current_dir,current_stage,current_direction,point,food_pos,food_pos2,delay_count
    screen.blit(text,(130,200))
    screen.blit(text2,(130,250))
    pygame.display.flip()
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
        keys_pressed = pygame.key.get_pressed()
        if keys_pressed[K_SPACE]:
            whole_xaxis = [30,30,30,30,30,30,30,30,30,30,30,30,30,30,30,30,30,30]
            whole_yaxis = [30,31,32,33,34,35,36,37,38,39,40,41,42,43,44,45,46,47]
            current_dir = [0 , 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
            current_stage = 0
            current_direction = 0
            point = 0
            delay_count = 0
            food_pos = [40,30]
            food_pos2 = [40,40]
            return

while True:
    if current_stage == 1:
        game()
    elif current_stage == 0:
        starts()
    elif current_stage == 3:
        difficulty()
    elif current_stage == 2:
        gameover()
