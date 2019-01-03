import sys
import pygame
import random
current_dir = ['C']
files = ['diskname',['C'],['D']]
start = pygame.image.load("ms-dos.png")
game  = pygame.image.load("game.jpg")
a = ""
print("welcome to M$-DO$ 1.0.00:00")
def search_dir_sub():
    for i in range(len(junk-1)):
        if junk[i+1][1] == current_dir[count]:
            count += 1
            junk = junk[i+1][1]
            
while True:
    try:
        a = raw_input(current_dir[0] + ":\>")
    except (EOFError):
        print("EOOOOOF")
    if a == "dir":
        for File in files:
            print(File+".COM")
    elif a == "ver":
        print("M$-DO$ 1.0.00:00 Copyright Micro$oft enterprise 70BC all rights reserved")
    elif a == "help":
        print ("Welcome to the Micro$oft M$-DO$ Help File. Unfourtunately, there is no help available at the moment.  Try again later")
    elif a == "tree":
        print ("This is the directory listing application for M$-DO$. Sorry, it appears that a virus has cleaned up your hard drive. Try again later.")
    elif a == "shut down":
        print("it will turn off in a second")
        pygame.time.wait(1000)
        sys.exit()
    elif a == "you are stupid":
        print ("I may be $tupid, but $o are you!")
    elif a[:2] == "md":
        files.append(a[3:])
    elif a == "win":
        print ("$tarting Micro$oft Window$ ver$ion 1.0. Please wait a few years while it boot$$$$$$$$$$$$$$$$$$$$.......")
        pygame.time.wait(5000)
        screen = pygame.display.set_mode((640,480))
        screen.blit(start,(0,0))
        pygame.display.flip()
        pygame.time.wait(5000)
        pygame.quit()
        print("this program is performing an ILLEGAL OPERATION and will be promptly TERMINATED.")
        print("Micro$oft Window$")
        print("please contact 911 for more information")
    elif a == "format":
        print("Formatting the content$ of your hard drive.  Plea$e wait a moment while all your hard work i$ utterly annihlated.")
        pygame.time.wait(3500)
        print("Micro$oft M$-DO$ has now de$troyed all your file$. >:D")
    elif a == "hello":
        print("sup bro")
    elif a == "how are you":
        print("I'm fine")
    else:
        ine = random.randint(0,2)
        if ine == 0:
            print("Bad command or file name")
        else:
            print("SyntaxError: invalid syntax")
    for letters in a:  
        if letters == "s" or letters == "S": 
            print("loving reminder : you ju$t entered an illegal charactor, please use $ in$tead.  It i$ important to know that we at Micro$oft care about your money.")
    if random.randint(0,10) <= 1:
        print("Your $y$tem ha$ performed an ILLEGAL OPERATION and ha$ CRA$HED. Please contact the Micro$oft Technician$ at 9-1-1 to $end $ome emeregeny vehicle$ to re$olve thi$ i$$ue")
        pygame.time.wait(5000)
        sys.exit()
    if random.randint(0,20) <= 1:
        print("do you want to play a game?")
        pygame.time.wait(5000)
        screen = pygame.display.set_mode((1272,858))
        screen.blit(game,(0,0))
        pygame.display.flip()
        pygame.time.wait(5000)
        pygame.quit()
