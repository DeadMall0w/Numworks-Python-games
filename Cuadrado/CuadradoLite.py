from math import *
from random import *
from kandinsky import *
from ion import *
from time import *

fill_rect(0,0,320,320,color(160,200,200))
M=[]
w=18
s=12
z=0
g=[5,5]
t=0

for x in range(w):
  for y in range(w):
    r=randint(0,100)
    if r>=60:
      M.append(1)
    else:
      M.append(0)

def D():
  for x in range(w):
    for y in range(w):
      c=color(0,0,0)
      if M[y*w+x]==1:
        c=color(255,255,255)   
      elif M[y*w+x]==2:
        c=color(0,255,0)   
      fill_rect(x*s+57,y*s+5,s-2,s-2,c)

def P():
      c=color(0,255,0)   
      fill_rect(g[0]*s+57,g[1]*s+5,s-2,s-2,c)
      draw_string(str(t),20,105,color(0,0,0),color(160,200,200))
D()

while True:
  sleep(.04)
  if keydown(KEY_UP):  
    g[1]-=1
    if z==0:
      D()
      P()
    else:
      if M[g[1]*w+g[0]]==0:  
        P()
        t+=1
        M[g[1]*w+g[0]]=2
      else:
        g[1]+=1
    sleep(.25)
  elif keydown(KEY_DOWN):  
    g[1]+=1
    if z==0:
      D()
      P()
    else:
      if M[g[1]*w+g[0]]==0: 
        P()
        t+=1
        M[g[1]*w+g[0]]=2
      else:
        g[1]-=1
    sleep(.25)
  elif keydown(KEY_LEFT):  
    g[0]-=1
    if z==0:
      D()
      P()
    else:
      if M[g[1]*w+g[0]]==0:  
        P()
        t+=1
        M[g[1]*w+g[0]]=2
      else:
        g[0]+=1
    sleep(.25)
  elif keydown(KEY_RIGHT):  
    g[0]+=1
    if z==0:
      D()
      P()
    else:
      if M[g[1]*w+g[0]]==0:  
        M[g[1]*w+g[0]]=2
        t+=1
        P()
      else:
        g[0]-=1
    sleep(.25)
  if keydown(KEY_OK) and z==0:
    if M[g[1]*w+g[0]]==0:
      z=1
      t+=2