from math import *
from kandinsky import *
from random import * 
from ion import *
from time import *
def F(x,y,w,h,c):
    fill_rect(x,y,w,h,c)
B=color(0,0,0)
a=255
W=color(a,a,a)
R=color(a,0,0)
def C(n,m,p):
    n=max(min(n,p),m)
    return n
b=[150.0, 100.0,2,uniform(-3,3)]
p=[]
w=1
t=0
g=0
S=0
j=0
F(0,0,320,a,B)
while True:
    if (monotonic()-t) < 1/45:
        continue
    t = monotonic()
    if g==0:
        s=("-Solo","-Versus Bot","-1v1","PONG !","Press 'OK' to play.","score: ")
        if keydown(KEY_DOWN):
            if j==2: j=0
            else : j+=1
            sleep(.15)
        if keydown(KEY_UP):
            if j==0:j=2
            else:j-=1
            sleep(.15)
        for i in range(3):
            draw_string(s[i], 95,80+i*20,R if j==i else W,B)
        draw_string(s[3],10,5,W,B)
        draw_string(s[4],120,195,W,B)
        if S!=0:
            draw_string(s[5]+str(S),120,40,W,B)
        if keydown(KEY_OK):
            g=j+1
            F(0,0,320,a,B)
            p=[a/2,180]
            S=0
            b=[150.0, 100.0,2,uniform(-3,3)]
        continue
    F(int(b[0]),int(b[1]),10,10,B)
    b[0]+=b[2]
    b[1]+=b[3]
    if b[1] <= 1 or b[1] >= 215:
        b[3]*=-1
        w=1
    if b[0] <= 1 or b[0] >= 315:
        b[2]*=-1
        w=1

    if g == 1:
        if p[0]<b[0]-45 or p[0]>b[0]+10 or p[1]<b[1]-10 or p[1]>b[1]+10:
            ak=0
        else:
            if w == 1:
                b[3]*=-1.04
                b[3]=C(b[3],-4.5,4.5)
                b[2]+=(b[0]-p[0]-22)/10
                b[2]*=1.04
                w=0
                S+=1
        
        if b[1] > 200:
            g=0
            F(0,0,320,a,B)
            continue
    draw_string(str(S),10,10,W,B)        
    F(int(b[0]),int(b[1]),10,10,W)
    if keydown(KEY_RIGHT):
        F(int(p[0]),int(p[1]),5,5,B)
        p[0]+=5
    if keydown(KEY_LEFT):
        F(int(p[0])+45,int(p[1]),5,5,B)
        p[0]-=5
    if keydown(17):
        g=0
        F(0,0,320,a,B)
        continue
    F(int(p[0]),int(p[1]),45,5,W)
