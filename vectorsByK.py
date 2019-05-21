# vectors2 and mapping functions
# possible todo: Add a menu system
#to create vectors and present 
# possible todo: add numbering to graph line

import turtle as t
import math as m
import random


# this is to show the cursor
t.st()

# this is to stop the speed of the turtles movement from being
#painfully slow
t.speed(0)

#so you can use 8 bit rgb 
t.colormode(255)


# initialise some colours
RED = (255,0,0)
GREEN = (0,255,0)
BLUE = (0,0,255)
CYAN = (0,255,255)
YELLOW = (255,255,0)


# this is to stop the vectors from being only 1 pixel per unit vector
tscale = 30


# really a record of vectors for now
class vectors:
  #random colour
  def __init__(self,x,y,name,color = (random.randint(0,255),random.randint(0,255),random.randint(0,255))):
    
    self.x = x # The vectors x and below the y coordinate
    self.y = y
    self.color = color# The colour used in turtle
    self.name = name# The name of the vector, not used currently
    self.vectorcomp = [x,y]# The vector as an array 

# getters
  def getColor(self):
    return self.color

  def getComp(self):
    return self.vectorcomp
    
  def getName(self):
    return self.name



# multipy the vector by a scalar
def scalar_mult(self,scale,vector):
    
  vector_mult=[]
  for a in range(len(vector.getComp())):
    vector_mult.append(vector[a]*scale)
  return vector_mult

# add two vectors together.
def add_vectors(self,vector1,vector2):
  if len(vector1.getComp()) == len(vector2.getComp()):
    vectorsum = []
  else:
    print("unable to sum two incoherent vectors")
    
  for a in range(len(vector1.getComp())):
    vectorsum.append(vector1.getComp()[a]+vector2.getComp()[a])
  return vectorsum
  

# subtract two vectors together
def sub_vectors(self,vector1,vector2):
  if len(vector1.getComp()) == len(vector2.getComp()):
    vectorsum = []
    for a in range(len(vector1.getComp())):
      vectorsum.append(vector1.getComp()[a]-vector2.getComp()[a])
    return vectorsum
  else:
    print("unable to sum two incoherent vectors")


# show vectors in turtle graphics
def present(vector):
  t.pensize(2)
  t.st()
  center()
  colorv = vector.getColor()
  t.color(colorv)

  if dimcheck(vector.getComp()):
    x = vector.getComp()[0]
    y = vector.getComp()[1]
    finalx = x*tscale
    finaly = y*tscale
    t.pendown()
    t.goto(finalx,finaly)
    addtriangle(vector,finalx,finaly)
  t.color(0,0,0)
  t.pensize(1)

# simply check if the vectors are two dimensional
def dimcheck(vectordim):
  if len(vectordim) != 2:
    print("vector is not 2 dimensional...")
    return False
  else:
    return True

# adds a triangle head to the vector to show direction and not make it look
#like a boring line
def addtriangle(vector,x,y):
  if dimcheck(vector.getComp()):
    t.st()
    t.up()

    arrowSize = (modul(vector.getComp()))/5
    arrowSize *= tscale

    t.seth(m.degrees(dotangle(vector.getComp(),[10,0])))
    t.goto(x,y)

    t.pendown()

    t.right(150)
    t.forward(arrowSize)
    t.backward(arrowSize)
    t.right(60)
    t.forward(arrowSize)
    t.backward(arrowSize)
    center()


def dotprod(vector1,vector2):
  Sum = (vector1[0]*vector2[0])+(vector1[1]*vector2[1])
  return Sum


def dotangle(vector1,vector2):
  Sum = dotprod(vector1,vector2)

  angle = m.acos(Sum/(modul(vector1)*modul(vector2)))
  return angle


def modul(vector):
  mod = m.sqrt(vector[0]**2 + vector[1]**2)
  return mod


def center():
  t.up()
  t.goto(0,0)
  t.pendown()
  t.seth(0)

#show a graph to allow a more accurate understanding
def graph():
  width = t.window_width()
  height = t.window_height()

  center()
  for a in range((width//2)//tscale):
    t.forward(tscale)
    t.right(90)
    t.forward(tscale/3)
    t.left(180)
    t.forward(tscale/3)
    t.seth(0)

  center()
  for a in range((width//2)//tscale):
    t.forward(-tscale)
    t.right(-90)
    t.forward(-tscale/3)
    t.left(-180)
    t.forward(-tscale/3)
    t.seth(0)

  t.up()
  t.goto(0,0)
  t.pendown()
  t.seth(90)
  for b in range((height//2)//tscale):
    t.forward(tscale)
    t.right(90)
    t.forward(tscale/3)
    t.left(180)
    t.forward(tscale/3)
    t.seth(90)

  t.up()
  t.goto(0,0)
  t.pendown()
  t.seth(90)
  for b in range((height//2)//tscale):
    t.forward(-tscale)
    t.right(-90)
    t.forward(-tscale/3)
    t.left(-180)
    t.forward(-tscale/3)
    t.seth(90)

'''
graph()
v1 = vectors(5,5,"vector1",RED)
present(v1)
'''
input()

