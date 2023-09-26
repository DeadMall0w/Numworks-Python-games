from kandinsky import *
from random import * 
from ion import *
from time import *
def F(x,y,w,h,c): # draw shape
    fill_rect(x,y,w,h,c)
F(0,0,320,240, color(32,33,36))
c=[color(32,33,36),color(172,172,172),color(116,116,116)]
F(0,160,320,2, color(172,172,172))
x=24.0
y=129
JumpForce=32
pY=0
cactusYPos=124
cactus=[]
clouds=[]

s=8

timer = 0
spawnTime = uniform(35,75)
def ds(r,X,Y): # draw sprite 
    for i in range(len(r)):
        F(int(r[i][0]*4+X),int(r[i][1]*4+Y),int(r[i][2]*4),int(r[i][3]*4),c[r[i][4]])
        
def D():
    r = [(2,6,1,2,1),(1,6,1,1,2),(1,7,1,1,0),(0,5,6,2,1),(0,3,1,2,1),(4,1,2,4,1),(6,1,3,3,1),(5,2,1,1,0)]
    ds(r,x,y)

def d():
    r=[(2,6,1,1,1),(1,6,1,2,2),(2,7,1,1,0),(0,5,6,2,1),(0,3,1,2,1),(4,1,2,4,1),(6,1,3,3,1),(5,2,1,1,0),]
    ds(r,x,y)

def r():
    r = [(2,6,1,2,0),(1,6,1,2,0),(0,5,6,2,0),(0,3,1,2,0),(4,1,2,4,0),(6,1,3,3,0),(5,2,1,1,0)]
    ds(r,x,y)

def draw_cac(i):
    r = [(4,0,2,10,1),(2,2,1,6,1),(7,3,1,5,1),(2,6,6,2,1)]
    ds(r, cactus[i], 124)

def drawCloud(i):
    r = [(0,5,8,2,1),(1,4,6,1,1),(2,3,2,1,1)]
    ds(r,clouds[i], clouds[i+1])
def remDrawCloud(i):
    r = [(0,5,8,2,0),(1,4,6,1,0),(2,3,2,1,0)]
    ds(r,clouds[i], clouds[i+1])

def rem_cac(i):
    x=3
    if s<=11:
        x=3
    else:
        x=4
    r=[(3,2,x,4,0),(6,0,x,6,0),(8,3,x,5,0),(6,8,x,2,0),]
    ds(r, cactus[i], 124)


d()
for i in range(len(cactus)):
    draw_cac(i)

timer=uniform(35,75)
t = 0
isDead = False
stMono=monotonic()
tim = 0
a = 0
while True:
    if isDead == True: # si on a perdue
        if keydown(KEY_EXE) or keydown(KEY_OK):
            E=[]
            y=133
            s=8
            stMono=monotonic()
            F(0,0,320,240,c[0])
            F(0,160,320,2,c[1])
            isDead=False
        continue
    if (monotonic()-t) > 1/30: # 30 fps
        # moon
        ds([(0,0,5,5,1)], 69, 20)
        
        t=monotonic()
        timer-=1
        tim+=1 
        if tim==5:
            tim=0
            if a==1:
                a=0
            else:
                a=1
        if timer <=5: 
            cactus.append(350)
            timer = uniform(25,40)
        
        #saut
        if keydown(KEY_EXE) and y == 129 or keydown(KEY_OK) and y == 129:
            pY-=JumpForce
            r()

        pY+=3
        if y< 129:
            r()

        y+=pY
        pY=min(10,pY)

        y = min(y, 129)
        if a==1:
            d()
        else:
            D()
        sc=int((monotonic()-stMono)*10)
       
        F(0,160,320,2,c[1])
        s+=sc/285000
        s=min(s,13)
        draw_string(str(sc),230,10,c[1],c[0])

        #generate clouds
        if randint(0,100) >= 99:
            clouds.append(400)
            clouds.append(randint(10, 40))
            clouds.append(randint(2,4))

        #draw and move all of the clouds 
        i = 0
        while i< len(clouds):
            if clouds[i] < -35:
                clouds.pop(i)
                clouds.pop(i)
                clouds.pop(i)
                continue
            remDrawCloud(i)
            clouds[i]-=clouds[i+2]
            drawCloud(i)      
            i+=3

        i = 0
        while i< len(cactus):
            if cactus[i] < -35:
                cactus.pop(i)
                continue
            cactus[i]-=s
            rem_cac(i)
            draw_cac(i)      
            if cactus[i] < 45 and cactus[i] > 20:
                if y > 81:
                    F(0,0,320,240, color(32,33,36))
                    draw_string("GAME OVER",80,120,c[1],c[0])
                    draw_string(str(sc),230,10,c[1],c[0])
                    cactus=[]
                    clouds=[]
                    isDead = True
                    sleep(.3)
            i+=1
