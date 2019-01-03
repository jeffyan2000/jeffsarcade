__author__ = 'bo'
import pygame,sys
pygame.init()
screen_width = 700
screen_length= 500
screen = pygame.display.set_mode((screen_width, screen_length))
currentStage = 0
mission_window = pygame.image.load("textures//mission_frame.png")
Font = pygame.font.SysFont("Calibri", 40)
numbers = ["textures//num1.png",
        "textures//num2.png",
        "textures//num3.png",
        "textures//num4.png",
        "textures//num5.png",
        "textures//num6.png",
        "textures//num7.png",
        "textures//num8.png"]
space = "textures//space.png"
current_stage = 1

def split_by_n( seq, n ):
    while seq:
        yield seq[:n]
        seq = seq[n:]

class intereactObj():
    def __init__(self, intereactWay,intereactEvent,x,y,width,length,texture,texture2):
        self.intereactWay = intereactWay
        self.x        = x
        self.y        = y
        self.width    = width
        self.length   = length
        self.intereactEvt = intereactEvent
        self.current  = 0
        self.texture  = pygame.image.load(texture)
        self.texture2  = pygame.image.load(texture2)

    def pressed(self,pos):
        if pos[0] >= self.x and pos[0] < self.x + self.width:
            if pos[1] >= self.y and pos[1] < self.y + self.length:
                if self.current == 0:
                    self.current = 1
                elif self.current == 1:
                    self.current = 0
                return True
        return False

    def draw(self):
        if self.current == 1:
            screen.blit(self.texture2, (self.x,self.y))
        else:
            screen.blit(self.texture, (self.x,self.y))

class ListenerObj():
    def __init__(self, intereactObject, xaxis, yaxis, width, length,texture,texturechange):
        self.intereactObject = intereactObject
        self.x =xaxis
        self.y =yaxis
        self.width = width
        self.length = length
        self.texture  = pygame.image.load(texture)
        self.changeTexture  = pygame.image.load(texturechange)
        self.actived  = False

    def draw(self):
        if self.actived == True:
            screen.blit(self.texture,(self.x,self.y))
        else:
            screen.blit(self.changeTexture,(self.x,self.y))

    def pressed(self,pos):
        if pos[0] >= self.x and pos[0] < self.x + self.width:
            if pos[1] >= self.y and pos[1] < self.y + self.length:
                return True
        return False

    def button_related(self,button):
        mouse = pygame.mouse.get_pressed()
        pos = pygame.mouse.get_pos()
        if self.intereactObject.pressed(pos) == True:
            if button == 'left':
                if mouse == (1,0,0):
                    if self.actived == True:
                        self.actived = False
                    else:
                        self.actived = True
                    return True
            elif button == 'right':
                if mouse == (0,0,1):
                    if self.actived == True:
                        self.actived = False
                    else:
                        self.actived = True
                    return True
            elif button == 'double':
                if mouse == (1,0,1):
                    if self.actived == True:
                        self.actived = False
                    else:
                        self.actived = True
                    return True

class Aim():
    def __init__(self,texture,x,y,length,width):
        self.texture = pygame.image.load("textures//" + texture + ".png")
        self.x       = x
        self.y       = y
        self.length  = length
        self.width   = width

none = Aim("space",-200,-200,0,0)

class KeyboardListener():
    def __init__(self,texture,x,y,length,width,aim):
        self.texture = pygame.image.load("textures//" + texture + ".png")
        self.x       = x
        self.y       = y
        self.length  = length
        self.width   = width
        self.aim     = aim

    def keyboard_handler(self):
        keys_pressed = pygame.key.get_pressed()
        if keys_pressed[pygame.K_LEFT]:
            self.x -= 8
        if keys_pressed[pygame.K_RIGHT]:
            self.x += 8

    def finish(self):
        if self.x >= self.aim.x and self.x <= self.aim.x + self.aim.width:
            if self.y >= self.aim.y and self.y <= self.aim.y + self.aim.length:
                return True
            elif self.y + self.length >= self.aim.y and self.y + self.length <= self.aim.y + self.aim.length:
                return True

        elif self.x + self.width >= self.aim.x and self.x + self.width <= self.aim.x + self.aim.width:
            if self.y >= self.aim.y and self.y <= self.aim.y + self.aim.length:
                return True
            elif self.y + self.length >= self.aim.y and self.y + self.length <= self.aim.y + self.aim.length:
                return True

    def draw(self):
        screen.blit(self.texture,(self.x,self.y))

class backgrounds():
    def __init__(self, texture):
        self.texture = pygame.image.load(texture)

    def draw(self):
        screen.blit(self.texture,(0,0))

class missions():
    def __init__(self, mission):
        self.message = list(split_by_n(mission,16))
        self.show = True
        self.word = [0,0,0,0,0,0,0,0,0,0,0,0,0,0]

    def accept(self,pos):
        if pos[0] >= 317 and pos[0] <= 390:
            if pos[1] >= 348 and pos[1] <= 374:
                return True

    def write(self):
        for i in range(len(self.message)):
            self.word[i] = Font.render(self.message[i], 1, (0,0,0))
            screen.blit(self.word[i],(220,i*30+20))

    def draw(self):
        if self.show == True:
            screen.blit(mission_window, (200,0))
            self.write()

class stage_animate():
    def __init__(self,stage,num):
        self.x     = screen_width
        self.stage = Font.render("stage "+ str(num) +" : " + stage, 1, (0,0,0))
        self.stop  = 0
        self.act   = 1

    def draw(self):
        if self.x >= -700:
            if self.stop <= 25 and self.x <= 200:
                self.stop += 1
                screen.blit(self.stage, (self.x,200))

            else :
                screen.blit(self.stage, (self.x,200))
                self.x -= 16
        else:
            self.act = 0

def title(stage_name,stage):
    while True:
        screen.fill((255,255,255))
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
        stage_name.draw()
        if stage_name.act == 0:
            return
        pygame.time.wait(30)
        pygame.display.flip()

def mission_stage(mission,stage):
    while True:
        screen.fill((255,255,255))
        mission.draw()
        pos = pygame.mouse.get_pos()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if mission.accept(pos) == True:
                    mission.show = False
                    break
        pygame.display.flip()
        if mission.show == False:
            break
        pygame.time.wait(30)

def stage1():
    stage_name = stage_animate("open the door",1)
    mission    = missions("Unlock the door by pressing the right buttons")
    background = backgrounds("textures//stage1_background.png")
    enter      = intereactObj(pygame.MOUSEBUTTONDOWN,1,325,300,110,56,"textures//stage1_enter.png","textures//stage1_enter_act.png")
    open       = ListenerObj(enter,0,100,160,160,"textures//stage1_open.png","textures//stage1_open_hide.png")
    num = [0,0,0,0,0,0,0,0]
    for i in range (2):
        for ii in range(4):
            num[i*4+ii] = intereactObj(pygame.MOUSEBUTTONDOWN,1,i*50+300,ii*50+100,21,21,numbers[i*2+ii],space)
    title(stage_name,1)
    mission_stage(mission,1)


    boom = 0
    oooo = 0
    while True:
        background.draw()
        enter.draw()
        open.draw()
        pos = pygame.mouse.get_pos()
        for i in range(8):
            num[i].draw()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                for i in range(8):
                    num[i].pressed(pos)
                if enter.pressed(pos) == True and boom != 20:
                    boom += 1
                elif open.pressed(pos) and oooo == 1:
                    oooo = 2
                elif boom == 20 and oooo == 0:
                    if open.button_related("left") == True:
                        oooo = 1
        if oooo == 2:
            global current_stage
            current_stage += 1
            break
        pygame.display.flip()
        pygame.time.wait(30)

def stage2():
    stage_name = stage_animate("avoid the guard",2)
    mission    = missions("Passing through them without    being noticed")
    aim        = Aim("space",500,0,500,50)
    background = backgrounds("textures//stage2_background.png")
    title(stage_name,2)
    mission_stage(mission,2)
    charactor  = KeyboardListener("stage2_charactor",100,300,100,150,aim)
    while True:
        background.draw()
        charactor.draw()
        charactor.keyboard_handler()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
        if charactor.x >= 300 and charactor.x < 400:
            charactor.x = 10
        elif charactor.x < -50:
            charactor.x = screen_width - 50
        elif charactor.x > screen_width - 50:
            charactor.x = -50
        elif charactor.finish() == True:
            global current_stage
            current_stage += 1
            break
        pygame.display.flip()
        pygame.time.wait(30)

def stage3():
    stage_name = stage_animate("find the chest",3)
    mission    = missions("Find where the  chest is         hint: there is a white cross on the chest")
    background = backgrounds("textures//stage3_background.png")
    chest      = pygame.image.load("textures//stage3_chest.png")
    title(stage_name,3)
    mission_stage(mission,3)
    oooo = 0
    while True:
        background.draw()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                screen.blit(chest,(250,200))
                pygame.display.flip()
                pygame.time.wait(3000)
                oooo = 1
        if oooo == 1:
            global current_stage
            current_stage += 1
            break
        pygame.display.flip()
        pygame.time.wait(30)

def stage4():
    stage_name = stage_animate("click the button",4)
    mission    = missions("Follow the real instruction")
    background = backgrounds("textures//stage4_background.png")
    title(stage_name,4)
    mission_stage(mission,4)
    button = intereactObj(pygame.MOUSEBUTTONDOWN, 1, 250,300,215,81,"textures//stage4_button.png","textures//stage4_button_act.png")
    num1   = intereactObj(pygame.MOUSEBUTTONDOWN, 1, 250,100,78,96,"textures//stage4_num1.png","textures//stage4_num1_act.png")
    oooo = 0
    while True:
        background.draw()
        button.draw()
        num1.draw()
        pos = pygame.mouse.get_pos()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if button.pressed(pos) == True:
                    oooo += 1
                    if oooo == 10:
                        oooo = 0
                num1.pressed(pos)
        text = Font.render("you pressed " + str(oooo) + " times",1,(0,0,0))
        if num1.current == 1:
            if oooo == 3:
                global current_stage
                current_stage += 1
                screen.blit(text,(200,400))
                pygame.display.flip()
                pygame.time.wait(2000)
                break
        screen.blit(text,(200,400))
        pygame.display.flip()
        pygame.time.wait(30)

def stage5():
    stage_name = stage_animate("click the button again",5)
    mission    = missions("Do what it said")
    background = backgrounds("textures//stage5_background.png")
    title(stage_name,5)
    mission_stage(mission,5)
    buttonr = intereactObj(pygame.MOUSEBUTTONDOWN, 1, 200,300,141,61,"textures//stage5_red.png","textures//stage5_red.png")
    buttong = intereactObj(pygame.MOUSEBUTTONDOWN, 1, 300,300,141,61,"textures//stage5_green.png","textures//stage5_green_act.png")
    oooo = 100
    while True:
        background.draw()
        if oooo == 1:
            buttonr.x = 350
            buttong.x = 150
        else:
            buttong.x = 350
            buttonr.x = 150
        buttonr.draw()
        buttong.draw()
        pos = pygame.mouse.get_pos()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                mou = pygame.mouse.get_pressed()
                if mou == (1,0,0):
                    if buttonr.pressed(pos) == True:
                        oooo = 100
                    elif buttong.pressed(pos) == True:
                        oooo -= 1

        text = Font.render("press the green button for " + str(oooo) + " times",1,(0,0,0))
        screen.blit(text,(50,250))
        pygame.display.flip()
        pygame.time.wait(30)
        if oooo == 0:
            global current_stage
            current_stage = 1
            break

while True:
    if current_stage == 1:
        stage1()
    elif current_stage == 2:
        stage2()
    elif current_stage == 3:
        stage3()
    elif current_stage == 4:
        stage4()
    elif current_stage == 5:
        stage5()
