from math import *
from kandinsky import *
from random import * 
from ion import *
from time import *
w = color(255,255,255)
isPlaying = False
c = [150, 50]
cloudsType = [0]
cloudsSize = [45, 10]

cloudSize = [38, 50, 7, 15]

cloudSpeed = 1.23
tsc = 39

playerXPos = 150.0
playerYPos = 50.0


playerSpeed = 4
playerJumpTime = 80
playerJumpForce = 3
gravity = 1.36
playerJumpRecover = 1
playerMaxHealth = 3
playerHealth = 3

isGrounded = False
isDead = False
canJumping = False

score = 0
probaCoins = 30
probaBadCoins = 10
probaDespawnCloud = 15

despawnSpeed = 1
minDespawnXSize = 12


coins = []
badCoins = []

BGc = color(0, 128, 255)

TARG_FPS=30
DELTA_TIME=1/TARG_FPS

def Init():
    playerHealth = playerMaxHealth
    isDead = False
    c = [150, 50]
    c = [45, 10]
    c = [0]
    fill_rect(0,0, 320, 240, BGc)
    isGrounded = False
    score = 0
    for i in range(5):
        Sc(randint(0, 320),randint(0, 240))

def Sc(x,y):
        c.append(x)
        c.append(y)
        xSize = randint(cloudSize[0],cloudSize[1])
        ySize = randint(cloudSize[2],cloudSize[3])
        cloudsSize.append(xSize)
        cloudsSize.append(ySize)

        m = randint(0, 100)
        if m <= probaDespawnCloud:
            cloudsType.append(1)
        else:
            cloudsType.append(0) 

        r = randint(0, 100)
        if(r <= probaCoins):
            coins.append(x + 22)
            coins.append(y - 30)
            return

        u = randint(0, 100)
        if(u <= probaBadCoins):
            badCoins.append(x + 22)
            badCoins.append(y - 30)


    


def updateCloud():
    i = 0
    while i < len(c):
        if c[i] > 369:
            c.pop(i+1)
            c.pop(i)

            cloudsSize.pop(i+1)
            cloudsSize.pop(i)

            cloudsType.pop(int(i/2))

        else:
            fill_rect(int(c[i]), int(c[i+1]), 2, cloudsSize[i+1], BGc)
            c[i] += cloudSpeed
            if cloudsType[int(i/2)] == 0:
                fill_rect(int(c[i]), int(c[i+1]), cloudsSize[i], cloudsSize[i+1], w)
            else:
                fill_rect(int(c[i]), int(c[i+1]), cloudsSize[i], cloudsSize[i+1], color(170, 170, 170))
        i += 2

def updateCoins():
    i = 0
    while i < len(coins):
        if coins[i] > 369:
            coins.pop(i+1)
            coins.pop(i)
        else:
            fill_rect(int(coins[i]), int(coins[i+1]), int(cloudSpeed+1), 10, BGc)
            coins[i] += cloudSpeed
            fill_rect(int(coins[i]), int(coins[i+1]), 10, 10, color(100, 100, 0))
        i += 2

        
def updateBadCoins():
    i = 0
    while i < len(badCoins):
        if badCoins[i] > 369:
            badCoins.pop(i+1)
            badCoins.pop(i)
        else:
            fill_rect(int(badCoins[i]), int(badCoins[i+1]), int(cloudSpeed+1), 10,BGc)
            badCoins[i] += cloudSpeed
            fill_rect(int(badCoins[i]), int(badCoins[i+1]), 10, 10, color(255, 0, 0))
        i += 2

def updatePlayer():
    fill_rect(int(playerXPos), int(playerYPos), 10, 20, color(255, 255, 0))

def DrawJumpTimer(_jumpTimer):
    fill_rect(10,210, 20, int((playerJumpTime - 20) / -2), color(0, 0, 0))
    fill_rect(10,210, 20, int((_jumpTimer - 20) / -2), color(255, 0, 0))


def DrawHealth():
    for i in range(0, playerMaxHealth):
        if i < playerHealth:
            fill_rect(300 - (15 * i),5, 10, 10, color(255, 0, 0))
        else:
            fill_rect(300 - (15 * i),5, 10, 10, color(0, 0, 0))


def dead():
    isDead = True
    playerHealth = playerMaxHealth
    score = 0
    fill_rect(0,0, 320, 240, BGc)

def restart():
    Init()

Init()

t = 0
y = 0
tc = tsc 
jumpTimer = playerJumpTime
ct = 0
while True:
    if isPlaying:
        if (monotonic() - ct) < DELTA_TIME:
            continue
        else:
            ct = monotonic()

        if isDead == False:
            if keydown(KEY_RIGHT):
                if playerXPos <= 305:
                    fill_rect(int(playerXPos), int(playerYPos), 10, 20, BGc)
                    playerXPos += playerSpeed
                    updatePlayer()

            if keydown(KEY_LEFT):
                if playerXPos >= 15:
                    fill_rect(int(playerXPos), int(playerYPos), 10, 20, BGc)
                    playerXPos -= playerSpeed
                    updatePlayer()

            canJump = False
            if keydown(KEY_EXE) or keydown(KEY_UP):
                k = 0
                while k < len(c):
                    dstX = int(playerXPos) - int(c[k])
                    dstY = int(playerYPos) - int(c[k+1])
                    if dstX <= cloudsSize[k] and dstX >= -2 and dstY <= 5 and dstY >= -5:
                        canJump = False
                        break
                    else:
                        canJump = True
                    k += 2

                if playerYPos >= 15 and canJump == True and isGrounded:
                    canJumping = True
                    fill_rect(int(playerXPos), int(playerYPos), 10, 20, BGc)
                    playerYPos -= playerJumpForce
                    updatePlayer()

                elif playerYPos >= 15 and canJump == True and canJumping and jumpTimer > 20:
                    jumpTimer -= 1
                    if jumpTimer >= 20:
                        fill_rect(int(playerXPos), int(playerYPos), 10, 20, BGc)
                        playerYPos -= playerJumpForce
                        updatePlayer()

            else:
                canJumping = False

            if isGrounded == False:
                if playerYPos >= 220 and isDead == False:
                    isDead = True
                    dead()
                else:
                    fill_rect(int(playerXPos), int(playerYPos), 10, 20, BGc)
                    playerYPos += gravity
                    updatePlayer()
            else: 
                if jumpTimer < playerJumpTime:
                    jumpTimer += playerJumpRecover
        
            i = 0
            while i < len(c):
                dstX = int(playerXPos) - int(c[i])
                dstY = int(playerYPos) - int(c[i+1])
                if dstX <= cloudsSize[i] and dstX >= -2 and dstY <= -10 and dstY >= -20:
                    isGrounded = True
                    if cloudsType[int(i/2)] == 1:
                        cloudsSize[i] -= despawnSpeed
                        c[i] += despawnSpeed
                        fill_rect(int(c[i])-2, int(c[i+1]), 4, cloudsSize[i+1], BGc)


                        if cloudsSize[i] <= minDespawnXSize:
                            fill_rect(int(c[i]), int(c[i+1]), cloudsSize[i] + 2, cloudsSize[i+1], BGc)

                            c.pop(i+1)
                            c.pop(i)

                            cloudsSize.pop(i+1)
                            cloudsSize.pop(i)

                            cloudsType.pop(int(i/2))
                    break
                else:
                    isGrounded = False
                i += 2

            v = 0
            while v < len(coins):
                dstX = int(playerXPos) - int(coins[v])
                dstY = int(playerYPos) - int(coins[v+1])
                if dstX <= 15 and dstX >= -5 and dstY <= 5 and dstY >= -15:
                    fill_rect(int(coins[v]), int(coins[v+1]), 12, 10, BGc)
                    coins.pop(v+1)
                    coins.pop(v)
                    score += 1
                    break
                v += 2

            z = 0
            while z < len(badCoins):
                dstX = int(playerXPos) - int(badCoins[z])
                dstY = int(playerYPos) - int(badCoins[z+1])
                if dstX <= 15 and dstX >= -5 and dstY <= 5 and dstY >= -15:
                    fill_rect(int(badCoins[z]), int(badCoins[z+1]), 12, 10, BGc)
                    badCoins.pop(z+1)
                    badCoins.pop(z)
                    score -= 1
                    playerHealth -= 1
                    if playerHealth == 0 and isDead == False:
                        isDead = True
                        dead()
                    break
                z += 2


            if isGrounded == True and playerXPos <= 305:
                fill_rect(int(playerXPos), int(playerYPos), 10, 20,BGc)
                playerXPos += cloudSpeed
                updatePlayer()
    

            updateCloud()
            updateCoins()
            updateBadCoins()
            DrawJumpTimer(jumpTimer)
            DrawHealth()

            tc -= 1
            if(tc < 0):
                rand = randint(-10, 10)
                tc = tsc  + rand
                Sc(randint(0, 10),randint(60, 220))

        else:
            jumpTimer = playerJumpTime
            fill_rect(0,0, 320, 240, BGc)
            draw_string("Vs etes mort, 'ok' pour relancer ",05,80, w, BGc)
            draw_string("Score: " + str(score),5,10, w, BGc)
            if keydown(KEY_OK):
                playerXPos = 150.0
                playerYPos = 50.0
                isDead = False
                playerHealth = playerMaxHealth
                score  = 0
                restart()
        draw_string("Score: " + str(score),5,10, w, BGc)

    else:
        draw_string("Press enter to play ! ",60,80, w, BGc)

        jumpTimer = playerJumpTime
        if keydown(KEY_OK) and isPlaying == False:
            isPlaying = True
            Init()

