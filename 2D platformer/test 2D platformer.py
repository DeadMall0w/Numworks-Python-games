#NOT FINISHED !

from math import *
from kandinsky import *
from random import * 
from ion import *
from time import *

def F(x,y,w,h,c):
    fill_rect(x,y,w,h,c)

def Clamp(n,m,p): #clamp fonction
    n=max(min(n,p),m)
    return n
p=[50,100]
C=color(0,0,0)
m=[20,120,20,10,10,160,300,10,200,100,10,200,20,100,10,200]#[30,170,40,10]#,20,120,20,10,10,160,300,10,200,100,10,200,20,100,10,200] # map

for i in range(5):
    x = randint(10,200)
    y = randint(10,200)
    w = randint(10,40)
    h = randint(10,20)
    m+=x,y,w,h
v=[0,0] 

c=color(67,76,70)
b=color(49,59,70)
C=color(33,32,47)

d=0
F(0,0,320,240,b)
a=[]

t=0
f=1
def R(x,y,w,h): # collision 
    i=0
    while i<len(m):
        if x<m[i]-w or x>m[i]+m[i+2] or y<m[i+1]-h or y>m[i+1]+m[i+3]:
            pass
        else:
            return 1
        i+=4
    return 0

while True:
    if monotonic()-t < 1/45: #FPS
        continue
    t=monotonic()
    d+=1

    v[1]+=1.2*(1+abs(v[1])*.025) # gravity
    v[1] = min(v[1], 5)

    g=0
    if R(int(p[0])+3,int(p[1])+10,11,5)==1: # isGrounded
        v[1]=0
        g=1

    if keydown(KEY_RIGHT)and d>1: # move right
        if R(int(p[0])+15,int(p[1]),3,10)==0: # right wall check
            v[0]+=1 if g==0 else 4
            f=1 # facing right
        else:
            v[0]=min(0,v[0])
        
    elif keydown(KEY_LEFT)and d>1: # move left
        if R(int(p[0])-2,int(p[1]),3,10)==0:
            v[0]-=1 if g==0 else 4
            f=2 # facing left
        else:
            v[0]=max(0,v[0])

    else: # apply friction
        if v[0]>.5:
            v[0]-=.4 if g==0 else .9
        elif v[0]<-.5:
            v[0]+=.4 if g==0 else .9
        else:
            v[0]=0
            
    v[0]=Clamp(v[0],-4,4) #limit the speed

    if keydown(KEY_EXE) and g == 1: # Jump
        v[1]-=12
    i=0

    if keydown(KEY_ANS) and d>50: # trigger a dash
        d=-10
        
    if d<0:
        if d%2==0:
            a+=[int(p[0]),int(p[1]),0]

        if f ==1:
            s,u,z=15,-1,17
        else:
            s,u,z=-15,1,-2
        
        speed = 15
           #R(int(p[0])+15,int(p[1]),3,10)==0
        if R(int(p[0])+z,int(p[1]),4,10)==0:
            v[0]=s
        else:
            while R(int(p[0])+z,int(p[1]),5,10)==1:
                p[0]+=u
                F(int(p[0])-1,int(p[1]),2,15,b)
            v[0]=0
            d=0

        # if f ==1:
        #     s,u=15,1
        # else:
        #     s,u=-15,-1
        # if R(int(p[0])+17,int(p[1]),4,10)==0 and f==1:
        #     v[0]=s
        
        # elif R(int(p[0])-2,int(p[1]),4,10)==0 and f==2:
        #     v[0]=s
        # else:
        #     if f==1:
        #         while R(int(p[0])+15,int(p[1]),2,10)==1:
        #             F(int(p[0])+14,int(p[1]),u,15,b)
        #             p[0]-=1
        #     else:
        #         while R(int(p[0])-2,int(p[1]),2,10)==1:
        #             F(int(p[0])-1,int(p[1]),u,15,b)
        #             p[0]+=1
        #     d=0
    while i <len(a):# draw trail when the player is dashing 
        u=a[i+2]
        F(a[i],a[i+1],15,15,color(69-u,79-u,110-u*2))
        a[i+2]+=1
        if u>20:
            a.pop(i+2)
            a.pop(i+1)
            a.pop(i)

        i+=3

    i=0
    while i < len(m):
        F(m[i],m[i+1],m[i+2],m[i+3],C)
        i+=4

    F(int(p[0]),int(p[1]),15,15,b)
    p[0]+=v[0]
    
    if R(p[0]+2,p[1]-2,11,5)==0: # top collision
        p[1]+=int(v[1])
    else:
        if (v[1] < 0):
            v[1] = 0
            v[1] = 1
        p[1]+=v[1]
    if d < 0:
        F(int(p[0]),int(p[1]),15,15,color(69,79,90))  
    else:
        F(int(p[0]),int(p[1]),15,15,c)  
    
