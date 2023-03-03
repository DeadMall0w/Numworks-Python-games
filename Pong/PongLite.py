from math import *
from kandinsky import *
from random import * 
from ion import *
from time import *
def F(z,e,i,o,x):
    fill_rect(z,e,i,o,x)
def H(c,d,t,q,j):
    draw_string(c,d,t,q,j)
a=69
F(0,0,320,240,color(0,0,0))
u=[150.0, 100.0,1,uniform(-0.69,0.69)]
bs=2.0
p1=100 
p2=100 
spd=3
sz=32
cw=1 
v=0
b=color(0,0,0)
w=color(255,255,255)
T=30
D=1/T
ct=0
def C(n,m,p):
    n=max(min(n,p),m)
    return n
while True:
    if (monotonic()-ct) < D:
        continue
    ct = monotonic()
    if(keydown(KEY_MINUS)):
        p1-=spd
        F(290,p1+30,6,20,b)
    if(keydown(KEY_EXE)):
        p1+=spd
        F(290,p1-spd,6,sz,b)
    F(290,p1,6,sz,w)
    if(keydown(KEY_ONE)):
        p2-=spd
        F(20,p2+30,6,20,b)
    if(keydown(KEY_ZERO)):
        p2+=spd
        F(20,p2-spd,6,sz,b)
    F(20,p2,6,sz,w)
    F(int(u[0]),int(u[1]),10,10,b)
    u[0]+=u[2]*bs
    u[1]+=u[3]*bs
    if u[1] <= 1 or u[1] >= 215:
        u[3]*=-1
    if cw == 1:
        if u[0] >= 280 and u[0] <= 290:
            if u[1] <= p1+sz+10 and u[1] >= p1-10:
                u[2]*=-1.06
                cw=2
                u[3]=C((p1-u[1]+sz/2)/20, -1.7,1.7)
                v+=1
    if cw == 2:
        if u[0] >= 10 and u[0] <= 24:
            if u[1] <= p2+sz+10 and u[1] >= p2-10:
                u[2]*=- 1.06
                cw=1
                u[3]= C((p2-u[1]+sz/2)/20, -1.7,1.7)
                v+=1
    s ="Appuye sur 'OK' pour relancer"
    if u[0] >= 320:
        H("Le joueur 2 a gagne !!", a,a,w,b)
        H(s,16,96,w,b)
        if keydown(KEY_OK):
            F(0,0,320,240,b)
            u=[150,100,1,uniform(-.7,.7)]
            p1=100
            p2=100
            cw=1
            v=0
    elif u[0] <= 0:
        H("Le joueur 1 a gagne !",a,a,w,b)
        H(s,16,96,w,b)
        if keydown(KEY_OK):
            F(0,0,320,240,b)
            u=[150, 100,1,uniform(-.7,.7)]
            p1=100
            p2=100
            cw=1
            v=0
    H(str(v),150,10,w,b)
    F(int(u[0]),int(u[1]),10,10,w)