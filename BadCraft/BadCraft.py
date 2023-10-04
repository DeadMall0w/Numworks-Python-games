# NOT FINISHED !


from math import *
from kandinsky import *
from random import * 
from ion import *
from time import *


# variables ***********************************************************************

# world gen. ********************************************************************
backGroundColor = color(0, 128, 255)
map = {1:[1,1,0,0,0,1]}
blockSize = 10


mapXSize = 22
height = 10
maxHeight = 22
minHeight = 3
mapYCollision = []
redraw = False

#Bloc color ************************************************************************
rockMainColor = color(128, 128, 128)

grassMainColor = color(0, 170, 0)
grassSecondColor = color(139,69,19)

dirtColor = color(139,69,19)


# player stats *****************************************************************

playerAcceleration = 8
playerFriction = 6
playerMaxXVel = 10
playerJumpForce = 3.69
playerSpeed = 3

playerXPos = 250
playerYPos = 50.0

playerXSize = 7
playerYSize = 12

playerXVel = 0
playerYVel = 0

playerMainColor = color(255, 255, 255)

minXPos = 15
maxXPos = 305
  
isGrounded = True
canJump = True
jumpTickInterval = 10

hasGravity = True
playerXFlySpeed = 2
playerYFlySpeed = 2

cursorXPos = 4
cursorYPos = 10

cursorColor = color(255, 0, 0)

cursorMovingTick = 1 



# Main world stats ***********************************************************************
gravity = 9.81

# Games stats **********************************************************************
TARG_FPS=30
DELTA_TIME=1/TARG_FPS
UPDATE_MAP_DRAWN = 2 #every "x" s. the map will be redraw


fill_rect(0,0, 320, 240, color(0,128,255))
#Populate the map ! ********************************************************************
_mapXSize = 320/blockSize
blocks = []
for x1 in range(0, _mapXSize):
    for y1 in range(0, maxHeight):
        if y1 <= height:
            diffHeight = height - y1
            if diffHeight < 1:
                mapYCollision.append(y1)
                blocks.append(2)
            elif diffHeight <  randint(2,4):
                blocks.append(3)
            else:
                blocks.append(1)
        else:
            blocks.append(0)
        

    # seed(int(_seed - _seed2 + x1 * x1 * x1 - _seed * 2*_seed2))
    height += randint(-1,1) #Set a random height for the next iteration 
    if height > maxHeight:
        height = maxHeight
    elif height < minHeight:
        height = minHeight
    
    map[x1] = blocks
    

    blocks = []

#DRAW THE MAP ! ***************************************************************************
for _x in range(0, len(map)):
    for _y in range(0,len(map[_x])):
        _blockType = map[_x][_y]
        if _blockType == 1: #rock 
            fill_rect(int(_x*blockSize), int((240 - blockSize) - _y*blockSize), blockSize,blockSize, rockMainColor)
        elif _blockType == 2: # grass
            fill_rect(int(_x*blockSize), int((240 - blockSize) - _y*blockSize), blockSize,blockSize, grassSecondColor)
            fill_rect(int(_x*blockSize), int((240 - blockSize) - _y*blockSize), blockSize,int(blockSize/4), grassMainColor)
        elif _blockType == 3: # dirt
            fill_rect(int(_x*blockSize), int((240 - blockSize) - _y*blockSize), blockSize,blockSize, dirtColor)
        

def BakeCollision(_mapXSize, _maxHeight, _map): #prebake the collision, so the game can do the collision more easier and with low performance cost ! 
    # for x1 in range(0, _mapXSize):
    #     for y1 in range(0, _maxHeight):
    #         if _map[x1[y2]] == 0:
    #             #Do nothing because it's an air block 
    print("")

def DrawCursor(cursorXPos, cursorYPos, blockSize):
    fill_rect(int(cursorXPos*blockSize), cursorYPos*blockSize, 4,2, cursorColor)
    fill_rect(int(cursorXPos*blockSize), cursorYPos*blockSize, 2,4, cursorColor)

    fill_rect(int(cursorXPos*blockSize), cursorYPos*blockSize + 8, 4,2, cursorColor)
    fill_rect(int(cursorXPos*blockSize), cursorYPos*blockSize + 6, 2,4, cursorColor)

    fill_rect(int(cursorXPos*blockSize) +6, cursorYPos*blockSize + 8, 4,2, cursorColor)
    fill_rect(int(cursorXPos*blockSize) + 8, cursorYPos*blockSize + 6, 2,4, cursorColor)

    fill_rect(int(cursorXPos*blockSize) + 6, cursorYPos*blockSize, 4,2, cursorColor)
    fill_rect(int(cursorXPos*blockSize)+ 8, cursorYPos*blockSize, 2,4, cursorColor)
            
currentTime = 0
mapDrawTick = 0
jumpTick = 0
_cursorMovingTick = 0
while True:
   
    if (monotonic() - currentTime) > DELTA_TIME:            #FPS System  
        currentTime = monotonic()
        mapDrawTick += 1
        _cursorMovingTick += 1
        
        if canJump == False:
            jumpTick += 1
            if jumpTick >= jumpTickInterval:
                jumpTick = 0
                canJump = True

        if mapDrawTick >= TARG_FPS * UPDATE_MAP_DRAWN or redraw == True:
            redraw = False
            mapDrawTick = 0

            _x = 0
            _y = 0

            for _x in range(0, len(map)):
                for _y in range(0,len(map[_x])):
                    _blockType = map[_x][_y]
                    if _blockType == 1: #rock 
                        fill_rect(int(_x*blockSize), int((240 - blockSize) - _y*blockSize), blockSize,blockSize, rockMainColor)
                    elif _blockType == 2: # grass
                        fill_rect(int(_x*blockSize), int((240 - blockSize) - _y*blockSize), blockSize,blockSize, grassSecondColor)
                        fill_rect(int(_x*blockSize), int((240 - blockSize) - _y*blockSize), blockSize,int(blockSize/4), grassMainColor)
                    elif _blockType == 3: # dirt
                        fill_rect(int(_x*blockSize), int((240 - blockSize) - _y*blockSize), blockSize,blockSize, dirtColor)
        #Movement ********************************************************************
        #floor colision *****
        i = 0
        isGrounded = False
        playerMainColor = color(0,0,0)
        while i < len(mapYCollision):
            dstX = int(playerXPos) - int(i*blockSize)
            dstY = int(playerYPos) - int((240 - blockSize) - mapYCollision[i]*blockSize)
            if dstX <= blockSize and dstX >= -playerXSize+2 and dstY <= blockSize and dstY >= -playerYSize-2:
                isGrounded = True
                playerMainColor = color(255,255,255)
            i += 1
        
        #Inputs detection *************************************************************
        if keydown(KEY_ZERO):#enabled GOD MOD
            if hasGravity == True:
                hasGravity = False
            else:
                hasGravity = True

        # s = ""
        if hasGravity == False:
            playerMainColor = color(255,0,0)
            # s = "GOD MOD ENABLED !"
        
        # draw_string(s,170,0, color(255, 0, 0), backGroundColor)

        if keydown(KEY_RIGHT):
            if hasGravity == True:
                if playerXPos <= maxXPos:

                    playerXVel += playerAcceleration
            else:
                fill_rect(int(playerXPos),int(playerYPos), playerXSize, playerYSize, backGroundColor)
                playerXPos += playerXFlySpeed
        
    
        if keydown(KEY_LEFT): #Move left 
            if hasGravity == True:
                if playerXPos >= minXPos:
                    playerXVel -= playerAcceleration
            else:
                fill_rect(int(playerXPos),int(playerYPos), playerXSize, playerYSize, backGroundColor)
                playerXPos -= playerXFlySpeed

        if keydown(KEY_DOWN):
            if hasGravity == False:
                fill_rect(int(playerXPos),int(playerYPos), playerXSize, playerYSize, backGroundColor)
                playerYPos += playerYFlySpeed

        if keydown(KEY_NINE): #Debug !* ******* *** ****** **** ** *  *** * ***** **** **** *** ***** **** 
            BakeCollision(_mapXSize, maxHeight, map)

        #Movement of the cursor ! ***********************************************************(le fun !! )
        if keydown(KEY_SIX): #Move the cursor to the right  
            #redraw the block at the last position of the cursor 
            if _cursorMovingTick >= cursorMovingTick:
                _cursorMovingTick = 0
                _blockID = map[cursorXPos][maxHeight - cursorYPos+1]
                if _blockID == 0:
                    fill_rect(int(cursorXPos*blockSize), cursorYPos*blockSize, blockSize,blockSize, backGroundColor)
                elif _blockID == 1: #rock 
                    fill_rect(int(cursorXPos*blockSize), cursorYPos*blockSize, blockSize,blockSize, rockMainColor)
                elif _blockID == 2: # grass
                    fill_rect(int(cursorXPos*blockSize), cursorYPos*blockSize, blockSize,blockSize, grassSecondColor)
                    fill_rect(int(cursorXPos*blockSize), cursorYPos*blockSize, blockSize,int(blockSize/4), grassMainColor)
                elif _blockID == 3: # dirt
                    fill_rect(int(cursorXPos*blockSize), cursorYPos*blockSize, blockSize,blockSize, dirtColor)
            
                cursorXPos += 1
                DrawCursor(cursorXPos, cursorYPos, blockSize)


        if keydown(KEY_FOUR): #Move the cursor to the left
            #redraw the block at the last position of the cursor 
            if _cursorMovingTick >= cursorMovingTick:
                _cursorMovingTick = 0
                _blockID = map[cursorXPos][maxHeight - cursorYPos+1]
                if _blockID == 0:
                    fill_rect(int(cursorXPos*blockSize), cursorYPos*blockSize, blockSize,blockSize, backGroundColor)
                elif _blockID == 1: #rock 
                    fill_rect(int(cursorXPos*blockSize), cursorYPos*blockSize, blockSize,blockSize, rockMainColor)
                elif _blockID == 2: # grass
                    fill_rect(int(cursorXPos*blockSize), cursorYPos*blockSize, blockSize,blockSize, grassSecondColor)
                    fill_rect(int(cursorXPos*blockSize), cursorYPos*blockSize, blockSize,int(blockSize/4), grassMainColor)
                elif _blockID == 3: # dirt
                    fill_rect(int(cursorXPos*blockSize), cursorYPos*blockSize, blockSize,blockSize, dirtColor)
            
                cursorXPos -= 1
                DrawCursor(cursorXPos, cursorYPos, blockSize)

        if keydown(KEY_EIGHT): #Move the cursor "upward"  
            #redraw the block at the last position of the cursor 
            if _cursorMovingTick >= cursorMovingTick:
                _cursorMovingTick = 0
                _blockID = map[cursorXPos][maxHeight - cursorYPos+1]
                if _blockID == 0:
                    fill_rect(int(cursorXPos*blockSize), cursorYPos*blockSize, blockSize,blockSize, backGroundColor)
                elif _blockID == 1: #rock 
                    fill_rect(int(cursorXPos*blockSize), cursorYPos*blockSize, blockSize,blockSize, rockMainColor)
                elif _blockID == 2: # grass
                    fill_rect(int(cursorXPos*blockSize), cursorYPos*blockSize, blockSize,blockSize, grassSecondColor)
                    fill_rect(int(cursorXPos*blockSize), cursorYPos*blockSize, blockSize,int(blockSize/4), grassMainColor)
                elif _blockID == 3: # dirt
                    fill_rect(int(cursorXPos*blockSize), cursorYPos*blockSize, blockSize,blockSize, dirtColor)
            
                cursorYPos -= 1
                DrawCursor(cursorXPos, cursorYPos, blockSize)

        if keydown(KEY_TWO): #Move the cursor "downward"  
            #redraw the block at the last position of the cursor 
            if _cursorMovingTick >= cursorMovingTick:
                _cursorMovingTick = 0
                _blockID = map[cursorXPos][maxHeight - cursorYPos+1]
                if _blockID == 0:
                    fill_rect(int(cursorXPos*blockSize), cursorYPos*blockSize, blockSize,blockSize, backGroundColor)
                elif _blockID == 1: #rock 
                    fill_rect(int(cursorXPos*blockSize), cursorYPos*blockSize, blockSize,blockSize, rockMainColor)
                elif _blockID == 2: # grass
                    fill_rect(int(cursorXPos*blockSize), cursorYPos*blockSize, blockSize,blockSize, grassSecondColor)
                    fill_rect(int(cursorXPos*blockSize), cursorYPos*blockSize, blockSize,int(blockSize/4), grassMainColor)
                elif _blockID == 3: # dirt
                    fill_rect(int(cursorXPos*blockSize), cursorYPos*blockSize, blockSize,blockSize, dirtColor)
            
                cursorYPos += 1
                DrawCursor(cursorXPos, cursorYPos, blockSize)

        if keydown(KEY_MINUS): #BREAK THE BLOCK !! 
            map[cursorXPos][maxHeight - cursorYPos+1] = 0
            redraw = True
            DrawCursor(cursorXPos, cursorYPos, blockSize)

        
        if keydown(KEY_EXE) or keydown(KEY_UP):
            if hasGravity == True:
                if isGrounded == True and canJump == True:
                    canJump = False
                    playerYVel -= playerJumpForce
            else:
                fill_rect(int(playerXPos),int(playerYPos), playerXSize, playerYSize, backGroundColor)
                playerYPos -= playerYFlySpeed
                
        
        #Apply friction 
        if playerXVel > playerFriction:
            playerXVel -= playerFriction
        elif playerXVel < -playerFriction:
            playerXVel += playerFriction
        else:
            playerXVel = 0

        #Apply gravity
        if isGrounded == False:
            playerYVel += gravity * DELTA_TIME
        elif playerYVel > 0:
            playerYVel = 0
            

        _playerXVelocity = playerXVel * DELTA_TIME
        _playerYVelocity = playerYVel * DELTA_TIME
    
        # #Clear player sprite at last frame 
        fill_rect(int(playerXPos),int(playerYPos), playerXSize, playerYSize, backGroundColor)

        #Apply velocity to player 
        playerXPos += _playerXVelocity
        playerYPos += playerYVel

        #Draw player at new his new position 
        fill_rect(int(playerXPos),int(playerYPos), playerXSize, playerYSize, playerMainColor)


    


