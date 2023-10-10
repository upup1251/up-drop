import pygame, sys, random
import pygame.locals as GAME_GLOBALS
import pygame.event as GAME_EVENTS
import pygame.time as GAME_TIME
pygame.init()
pygame.mixer.init()
startimg = pygame.image.load(r"D:\py\up-drop\start.png")
pygame.mixer_music.load(r"D:\py\up-drop\necromancers_tower (1).ogg")

endimage = pygame.image.load(r"D:\py\up-drop\end.png")
zhujueimage = pygame.image.load(r"D:\py\up-drop\主角.png")
windowHeight = 700
windowWidth = 1200

num = 0
objectsize = 30
objectY = 0
objectVy = 0.1
objectX = 400
objectVx = 0
speed = 1
grivaty = 1
upspeed = 0.1

startscreen = True
endscreen = False
startgame = False
moveright = False
moveleft = False
movedown = False
leftupstair = True
rightupstair = True
newStair = False

surface = pygame.display.set_mode((windowWidth, windowHeight))

def move():
    global  objectVx,objectX,moveright,moveleft,objectY,grivaty,upspeed
    if moveright == True:
        if objectVx <= 0:
            objectVx = speed
        if objectX+ objectsize < windowWidth:
            objectX += objectVx
    elif moveleft == True:
        if objectVx >= 0:
            objectVx = -speed
        if objectX > 0:
            objectX += objectVx

def checkdown():
    global rightupstair,leftupstair,objectY,upspeed,objectVy
    global  movedown
    if surface.get_at((objectX,int(objectY+objectsize))) == (255, 255, 255, 255):
        leftupstair = False
        objectVy = -upspeed
    if surface.get_at((objectX+objectsize-1,int(objectY+objectsize))) == (255,255,255,255):
        rightupstair = False
        objectVy = -upspeed
    objectY += objectVy
    objectVy = speed

def quitgame():
    pygame.quit
    sys.exit()

class upstair():
    global upstairWidth,upstairX,newStair,upspeed
    upstairHeight = 20
    upstairWidth = 100
    upspeed = 0.1
    upstairY = windowHeight+20
    upstairX= random.randint(0,windowWidth-upstairWidth)
    def upping(self):
        global upstairX,newStair,upstairWidth,upspeed
        if newStair == True:
            upstairX = random.randint(0,windowWidth-100)
            newStair = False
            self.upstairX = upstairX
        if upspeed <0.2:
            upspeed += 0.01
        self.upstairY -= upspeed
        pygame.draw.rect(surface,(255,255,255),(0,self.upstairY,self.upstairX,self.upstairHeight))
        pygame.draw.rect(surface,(255,255,255),(self.upstairX+upstairWidth,self.upstairY,windowWidth-self.upstairX-upstairWidth,self.upstairHeight))

gaptime = 1000
timenow = 0
Lastnew = 0
new = []
def newstair():
    global newStair,Lastnew
    newStair = True
    newupstair = upstair()
    Lastnew = GAME_TIME.get_ticks()
    newupstair.upping()
    new.append(newupstair)
    del newupstair

pygame.mixer_music.play()
while True:
    surface.fill((0,0,0))
    pygame.display.set_caption("MY FIST PYGAME-UP")
    if pygame.mixer_music.get_busy() == False:
        pygame.mixer_music.play()
    if startscreen == True:
        surface.blit(startimg,(0,0))
        for event in GAME_EVENTS.get():
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    startgame = True
                    startscreen = False
            if event.type == GAME_GLOBALS.QUIT:
                quitgame()

    if endscreen == True:
        surface.blit(endimage,(0,0))
        font = pygame.font.SysFont("宋体",50)
        text = font.render(f"score:{num}",1,(255,255,255))
        surface.blit(text,(50,50))
        new.clear()
        objectY = 0
        objectX = 400
        for event in GAME_EVENTS.get():
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LSHIFT or event.key == pygame.K_RSHIFT:
                    startscreen = True
                    endscreen = False
                if event.key == pygame.K_RETURN:
                    startgame = True
                    endscreen = False

            if event.type == GAME_GLOBALS.QUIT:
                quitgame()

    if startgame == True:
        for index,stair in enumerate(new):
            if stair.upstairY> -10:
                stair.upping()
            else:
                new.pop(index)
                num += 1
        timenow = GAME_TIME.get_ticks()
        if timenow - Lastnew >= gaptime:
            newstair()
            if gaptime >500:
                gaptime -= 50
        pygame.draw.rect(surface,(255,255,255),(0,windowHeight-5,windowWidth,5))

        checkdown()
        move()
        pygame.draw.rect(surface,(255,0,0),(objectX,objectY,objectsize,objectsize))
        surface.blit(zhujueimage, (objectX, objectY))

        if objectY<0:
            endscreen = True
            startgame = False
            startscreen = False




    for event in GAME_EVENTS.get():
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_RIGHT:
                moveright = True
            if event.key == pygame.K_LEFT:
                moveleft = True

        if event.type == pygame.KEYUP:
            if event.key == pygame.K_RIGHT:
                moveright = False
            if event.key == pygame.K_LEFT:
                moveleft = False

        if event.type == GAME_GLOBALS.QUIT:
            quitgame()



    pygame.display.update()