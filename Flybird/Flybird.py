from math import *
from kandinsky import *
from random import * 
from ion import *
from time import *

scale = 3
playerXPos = 45.0 
playerYPos = 50.0
playerYVel = 0.0

gravity = 4.5
maxPlayerYVel = 16

currentTick = 0
score = 0

jumpForce = 2
canJump = True

isDead = False

obstacles = []
obstacleSpeed = -1
obstacleSize = 75
obstacleWidth = 35
obstacleSpawnTime = 80
obstacleTimer = 0
# obstaclesLastOffset = 0

TARG_FPS=60
DELTA_TIME=1/TARG_FPS

fill_rect(0,0, 320, 240, color(0, 128, 255))

def draw_sprite(rects):
    for i in range(len(rects)):
        fill_rect(int(rects[i][0] * scale + playerXPos), int(rects[i][1] * scale + playerYPos), int(rects[i][2] * scale) , int(rects[i][3] * scale), rects[i][4])

def draw_bird():
    rects = [
            (1,2,9,4,(255,197,40)),
            (1,5,1,1,(255,168,28)),
            (1,6,1,1,(0,0,0)),
            (9,5,1,1,(255,168,28)),
            (10,5,1,2,(0,0,0)),
            (2,6,8,1,(255,168,28)),
            (2,7,8,1,(0,0,0)),
            (0,2,1,4,(0,0,0)),
            (1,2,1,1,(255,218,117)),
            (1,1,1,1,(0,0,0)),
            (2,1,8,1,(255,218,117)),
            (2,0,8,1,(0,0,0)),
            (10,1,1,1,(0,0,0)),
            (10,2,1,2,(255,170,155)),
            (9,2,1,2,(0,0,0)),
            (8,2,1,2,(255,255,255)),
            (10,4,1,1,(255,157,130)),
            (11,3,2,1,(255,157,130)),
            (11,4,2,1,(0,0,0)),
            (11,2,2,1,(0,0,0)),
            (13,3,1,1,(0,0,0)),
            (2,2,1,2,(0,0,0)),
            (3,2,3,1,(0,0,0)),
            (3,4,3,1,(0,0,0)),
            ]
    draw_sprite(rects)

draw_bird()

currentTime = 0
while True:
  if isDead == False:
    if (monotonic() - currentTime) > DELTA_TIME:            #FPS System  
        currentTime = monotonic()
        obstacleTimer += 1
        currentTick += 1
        if obstacleTimer > obstacleSpawnTime:
            obstacleTimer = 0
            obstacles.append(300)
            obstacles.append(randint(-30, 30))

        score = floor(currentTick / obstacleSpawnTime)
        # draw_string(str(score), 10, 10, color(255,255,255),color(0,128,255))

        fill_rect(int(playerXPos), int(playerYPos), int(15 * scale) , int(9 * scale),color(0, 128, 255))
        playerYVel += gravity * DELTA_TIME
        if playerYVel > maxPlayerYVel:
            playerYVel = maxPlayerYVel
        playerYPos += playerYVel

        if playerYPos >= 220 or playerYPos <= -20:
            isDead = True

        draw_bird()
        
        # Update the position of all obstacles
        i = 0
        while i < len(obstacles):
            if obstacles[i] < -35:
                obstacles.pop(i+1)
                obstacles.pop(i)
                continue
            fill_rect(obstacles[i], 165 + obstacles[i+1], obstacleWidth, obstacleSize + 50, color(0,128,255))
            fill_rect(obstacles[i], 0, obstacleWidth, obstacleSize + obstacles[i+1], color(0,128,255))
            obstacles[i] += obstacleSpeed
            fill_rect(obstacles[i], 165 + obstacles[i+1], obstacleWidth, obstacleSize + 50, color(0,255,0))
            fill_rect(obstacles[i], 0, obstacleWidth, obstacleSize + obstacles[i+1], color(0,255,0))
            i+=2

        #Collision
        z = 0
        while z < len(obstacles):
            if playerYPos - 6 < obstacleSize + obstacles[z+1]:
                if obstacles[z] - 16 < playerXPos and obstacles[z] + 10 > playerXPos:
                    isDead = True
            if obstacles[z] - 16 < playerXPos and obstacles[z] + 10 > playerXPos:
                if playerYPos + 22 > obstacleSize + obstacles[z+1] + 165 - obstacleSize:
                    isDead = True

                    
            z+=2
        
        if keydown(KEY_EXE):
            if canJump == True:
                playerYVel = -jumpForce
                canJump = False
        else:                                         
            canJump = True
  else:
    draw_string("You are Ded !  ",100,110, color(255, 255, 255), color(0,128,255))

