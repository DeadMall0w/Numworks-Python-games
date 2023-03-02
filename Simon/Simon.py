from math import *
from ion import *
from kandinsky import *
from random import *
from time import *

x=[20,120,220,120]
y=[72,20,72,144]
c=[[0,0,1],[1,0,0],[0,1,0],[1,0,1]]
p=[]

fill_rect(0,0,320,240,color(0,0,0))

fill_rect(20,72,65,65,color(0,0,120))
fill_rect(120,20,65,65,color(120,0,0))
fill_rect(220,72,65,65,color(0,120,0))
fill_rect(120,144,65,65,color(120,0,120))

def B(i):
  fill_rect(x[i],y[i],65,65,color(c[i][0]*255,c[i][1]*255,c[i][2]*255))
  sleep(.4)
  fill_rect(x[i],y[i],65,65,color(c[i][0]*120,c[i][1]*120,c[i][2]*120)) 
  sleep(.3)

def V(i):
  fill_rect(x[i],y[i],65,65,color(c[i][0]*255,c[i][1]*255,c[i][2]*255))
  sleep(.2)
  fill_rect(x[i],y[i],65,65,color(c[i][0]*120,c[i][1]*120,c[i][2]*120)) 
  sleep(.1)

def C():
  for i in p:
    B(i)
    
def P():
  p.append(randint(0,3))
  C()  

s=0
def Pq():    
  P()
  j=True
  k=0
  while k<len(p):
    if keydown(KEY_FOUR):
      V(0)
      if p[k]==0:
        k+=1
        sleep(.1)
      else:
        k+=1
        print("0")
        draw_string("o",100,100)     
    if keydown(KEY_EIGHT):
      V(1)
      if p[k]==1:
        print("69")
        k+=1
        sleep(.1)
      else:
        k+=1
        print("0")
        draw_string("o",100,100)     
    if keydown(KEY_TWO):
      V(3)
      if p[k]==3:
        print("69")
        k+=1
        sleep(.1)
      else:
        k+=1
        print("0")
        draw_string("o",100,100)     
    if keydown(KEY_SIX):
      V(2)
      if p[k]==2:
        print("69")
        k+=1
        sleep(.1)
      else:
        k+=1
        print("0")
        draw_string("o",100,100)     

  draw_string(str(len(p)),250,10,color(255,255,255),color(0,0,0))     
  Pq()  
Pq()