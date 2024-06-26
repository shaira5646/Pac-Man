# -*- coding: utf-8 -*-
"""CSE423 Lab Project PacMan Group 8 .ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/10y1r7mlEScuJIYKljq_8GJ4cA926gZRM

GROUP 8 Project PAC MAN \
By \
Abeda Zahid Chandrica (22341061) \
Shaira Chowdhury (20101261) \
Sultana Marium Trina (20101059)
"""

!pip install -q lucid>=0.2.3

import numpy as np

import ctypes.util
from lucid.misc.gl.glcontext import create_opengl_context

# Now it's safe to import OpenGL and EGL functions
import OpenGL.GL as gl
from OpenGL.GLU import *

# create_opengl_context() creates GL context that is attached to an
# offscreen surface of specified size. Note that rendering to buffers
# of different size and format is still possible with OpenGL Framebuffers.
#
# Users are expected to directly use EGL calls in case more advanced
# context management is required.
WIDTH, HEIGHT = 800,600
create_opengl_context((WIDTH, HEIGHT))

# OpenGL context is available here.

print(gl.glGetString(gl.GL_VERSION))
print(gl.glGetString(gl.GL_VENDOR))
#print(gl.glGetString(gl.GL_EXTENSIONS))

####### SCORES #####
def pixels(x, y):
  gl.glColor3f(0, 0.5, 1.0)
  gl.glBegin(gl.GL_POINTS)
  gl.glVertex2f(x, y)
  gl.glEnd()

def convert(x1, y1, zone):
  if zone == 0:
    pass
  elif zone == 1:
    x1, y1 = y1, x1
  elif zone == 2:
    x1, y1 = y1, -x1
  elif zone == 3:
    x1, y1 = -x1, y1
  elif zone == 4:
    x1, y1 = -x1, -y1
  elif zone == 5:
    x1, y1 = -y1, -x1
  elif zone == 6:
    x1, y1 = -y1, x1
  elif zone == 7:
    x1, y1 = x1, -y1
  return x1, y1

def originalZone(x1, y1, zone):
  if zone == 0:
    pass
  elif zone == 1:
    x1, y1 = y1, x1
  elif zone == 2:
    x1, y1 = -y1, x1
  elif zone == 3:
    x1, y1 = -x1, y1
  elif zone == 4:
    x1, y1 = -x1, -y1
  elif zone == 5:
    x1, y1 = -y1, -x1
  elif zone == 6:
    x1, y1 = y1, -x1
  elif zone == 7:
    x1, y1 = x1, -y1
  return x1, y1

def drawLine(X1, Y1, X2, Y2):
  zone = findZone(X1, Y1, X2, Y2)
  pixels(X1, Y1)
  X1, Y1 = convert(X1, Y1, zone)
  X2, Y2 = convert(X2, Y2, zone)
  dx = X2 - X1
  dy = Y2 - Y1
  d = 2 * dy - dx
  e = 2 * dy
  ne = 2 * (dy - dx)
  x = X1
  y = Y1
  while (x < X2):
    #x = x + 1
    x = x + 0.001
    if (d > 0):
      d += ne # choosing NE
      #y += 1
      x = x + 0.001
    else:
      d += d + e # choosing E
    x_new, y_new = originalZone(x, y, zone)
    pixels(x_new, y_new)

def findZone(X1, Y1, X2, Y2):
  dx = X2 - X1
  dy = Y2 - Y1
  zone = None
  if dx<0:
    absDx=dx*(-1)
    absDy=dy
  elif dy<0:
    absDx=dx
    absDy=dy*(-1)
  else:
    absDx=dx
    absDy=dy
  if (absDx >= absDy):#(abs(dx) >= abs(dy)):
    if (dx >= 0 and dy >= 0):
      zone = 0
    if (dx >= 0 and dy < 0):
      zone = 7
    if (dx < 0 and dy >= 0):
      zone = 3
    if (dx < 0 and dy < 0):
      zone = 4
  elif (absDx < absDy):#(abs(dx) < abs(dy)):
    if (dx >= 0 and dy >= 0):
      zone = 1
    if (dx >= 0 and dy < 0):
      zone = 6
    if (dx < 0 and dy >= 0):
      zone = 2
    if (dx < 0 and dy < 0):
      zone = 5
  return zone


def draw(num1):
  #gl.glTranslatef(-0.15,0,0)
  ##### DRAWING ZERO #####
  drawLine(-0.9, -0.7, -0.8, -0.7)
  drawLine(-0.9, -0.9, -0.9, -0.8)
  drawLine(-0.9, -0.8, -0.9, -0.7)
  drawLine(-0.8, -0.7, -0.8, -0.8)
  drawLine(-0.8, -0.8, -0.8, -0.9)
  drawLine(-0.9, -0.9, -0.8, -0.9)
  if num1==9:
    drawLine(0.2, 0.3, 0.2, 0.4)
    drawLine(0.2, 0.4, 0.3, 0.4)
    drawLine(0.3, 0.2, 0.3, 0.3)
    drawLine(0.2, 0.2, 0.3, 0.2)
    drawLine(0.3, 0.3, 0.3, 0.4)
    drawLine(0.2, 0.3, 0.3, 0.3)

  elif num1==8:
    drawLine(-0.75, -0.7, -0.65, -0.7)
    drawLine(-0.75, -0.7, -0.75, -0.8)
    drawLine(-0.75, -0.8, -0.75, -0.9)
    drawLine(-0.75, -0.8, -0.65, -0.8)
    drawLine(-0.65, -0.7, -0.65, -0.8)
    drawLine(-0.75, -0.8, -0.65, -0.9)
    drawLine(-0.65, -0.9, -0.75, -0.9)
    drawLine(-0.65, -0.8, -0.65, -0.9)

  elif num1==7:
    drawLine(0.2, 0.4, 0.3, 0.4)
    drawLine(0.3, 0.4, 0.3, 0.3)
    drawLine(0.3, 0.2, 0.3, 0.3)

  elif num1==6:
    drawLine(-0.75, -0.7, -0.65, -0.7)
    drawLine(-0.75, -0.7, -0.75, -0.8)
    drawLine(-0.75, -0.8, -0.75, -0.9)
    drawLine(-0.75, -0.9, -0.65, -0.9)
    drawLine(-0.65, -0.8, -0.65, -0.9)
    drawLine(-0.65, -0.8, -0.75, -0.8)

  elif num1==5:
    drawLine(-0.75, -0.7, -0.65, -0.7)
    drawLine(-0.75, -0.7, -0.75, -0.8)
    drawLine(-0.75, -0.8, -0.65, -0.8)
    drawLine(-0.75, -0.9, -0.65, -0.9)
    drawLine(-0.65, -0.8, -0.65, -0.9)

  elif num1==4:
    drawLine(-0.75, -0.7, -0.75, -0.8)
    drawLine(-0.75, -0.8, -0.65, -0.8)
    drawLine(-0.65, -0.7, -0.65, -0.8)
    drawLine(-0.65, -0.8, -0.65, -0.9)

  elif num1==3:
    drawLine(-0.75, -0.7, -0.65, -0.7)
    drawLine(-0.75, -0.8, -0.65, -0.8)
    drawLine(-0.65, -0.7, -0.65, -0.8)
    drawLine(-0.75, -0.8, -0.65, -0.9)
    drawLine(-0.65, -0.9, -0.75, -0.9)
    drawLine(-0.65, -0.8, -0.65, -0.9)

  elif num1==2:
    drawLine(-0.85, -0.7, -0.65, -0.7)
    drawLine(-0.65, -0.7, -0.65, -0.8)
    drawLine(-0.65, -0.8, -0.75, -0.8)
    drawLine(-0.75, -0.8, -0.75, -0.9)
    drawLine(-0.75, -0.9, -0.65, -0.9)

  elif num1==1:
    drawLine(-0.75, -0.7, -0.75, -0.8)
    drawLine(-0.75, -0.8, -0.75, -0.9)

  elif num1==0:
    drawLine(-0.75, -0.7, -0.65, -0.7)
    drawLine(-0.75, -0.7, -0.75, -0.8)
    drawLine(-0.75, -0.8, -0.75, -0.9)
    drawLine(-0.75, -0.9, -0.65, -0.9)
    drawLine(-0.65, -0.9, -0.65, -0.8)
    drawLine(-0.65, -0.8, -0.65, -0.7)

#### FRIUTS ####
import math
gl.glClear(gl.GL_COLOR_BUFFER_BIT)
gl.glPointSize(5)


def draw_points(x, y):
  gl.glColor3f(1, 0.2, 0.2)
  gl.glBegin(gl.GL_POINTS)
  gl.glVertex2f(x/1000,y/1000)
  gl.glEnd()

def convertZone(x,y,X,Y):
  draw_points(x + X, y + Y)
  draw_points(y + X, x + Y)
  draw_points(y + X, -x + Y)
  draw_points(-x + X, y + Y)
  draw_points(-x + X, -y + Y)
  draw_points(-y + X, -x + Y)
  draw_points(-y + X, x + Y)
  draw_points(x + X, -y + Y)

def midPointCircle(X, Y, r):
  d = 1 - r
  x = 0
  y = r
  convertZone(x,y, X, Y)
  while x <= y:
    x += 1
    if d < 0:
      d += 2 * x + 3
    else:
      y -= 1
      d += 2 * (x - y) + 5
    convertZone(x, y, X, Y)

def drawfruit(X, Y, R):
  midPointCircle(X, Y, R)

### FINAL PAC MAN WITH MOVEMENT ABOUT THE CENTRE ###

import math

gl.glClear(gl.GL_COLOR_BUFFER_BIT)

##### SHAPES ######

def quad(x1,x2,y1,y2,type="H"):
  if type == "H":
    gl.glColor3f(1,0,0)
    gl.glBegin(gl.GL_QUADS)
    gl.glVertex2f(x1,y1)
    gl.glVertex2f(x1,y2)
    gl.glVertex2f(x2,y2)
    gl.glVertex2f(x2,y1)
    gl.glEnd()
  elif type == "G1":
    gl.glColor3f(0,0.5,0.7)
    gl.glBegin(gl.GL_QUADS)
    gl.glVertex2f(x1,y1)
    gl.glVertex2f(x1,y2)
    gl.glVertex2f(x2,y2)
    gl.glVertex2f(x2,y1)
    gl.glEnd()
  elif type == "G2":
    gl.glColor3f(0.8,0.5,0.7)
    gl.glBegin(gl.GL_QUADS)
    gl.glVertex2f(x1,y1)
    gl.glVertex2f(x1,y2)
    gl.glVertex2f(x2,y2)
    gl.glVertex2f(x2,y1)
    gl.glEnd()


def tri(x,y,x1,y1,x2,y2,type="PC"):
  if type == "PC":
    gl.glPointSize(5)
    gl.glColor3f(1,1,0)
    gl.glBegin(gl.GL_TRIANGLES)
    gl.glVertex2f(x,y)
    gl.glVertex2f(x1,y1)
    gl.glVertex2f(x2,y2)
    gl.glEnd()
  elif type == "H":
    gl.glPointSize(5)
    gl.glColor3f(1,0,0)
    gl.glBegin(gl.GL_TRIANGLES)
    gl.glVertex2f(x,y)
    gl.glVertex2f(x1,y1)
    gl.glVertex2f(x2,y2)
    gl.glEnd()
  elif type == "G1":
    gl.glPointSize(5)
    gl.glColor3f(0,0.5,0.7)
    gl.glBegin(gl.GL_TRIANGLES)
    gl.glVertex2f(x,y)
    gl.glVertex2f(x1,y1)
    gl.glVertex2f(x2,y2)
    gl.glEnd()
  elif type == "G2":
    gl.glPointSize(5)
    gl.glColor3f(0.8,0.5,0.7)
    gl.glBegin(gl.GL_TRIANGLES)
    gl.glVertex2f(x,y)
    gl.glVertex2f(x1,y1)
    gl.glVertex2f(x2,y2)
    gl.glEnd()

###### TRANSFORMATION #######

rf_Y = np.array([[-1, 0, 0],
             [0, 1, 0],
             [0, 0, 1]])
rf_X = np.array([[1, 0, 0],
             [0, -1, 0],
             [0, 0, 1]])
t_hearts = np.array([[1, 0, 0.1],
             [0, 1, 0],
             [0, 0, 1]])
t_g = np.array([[1, 0, 0],
             [0, 1, 0.75],
             [0, 0, 1]])
t_g2 = np.array([[1, 0, 0],
             [0, 1, 1.1],
             [0, 0, 1]])

rf_Y_t_g2 = np.matmul(rf_Y,t_g2)


### PAC MAN ###
def pacman(x,y,r,direction="right"):
  if direction == "right":
    #zone0
    tri(x,y,x+r/2,y+r*(3/4),x+r*(3/4),y+r/2)
    #zone1
    tri(x,y,x,y+r,x+r/4,y+r)
    tri(x,y,x+r/2,y+r*3/4,x+r/4,y+r)
    #zone2
    tri(x,y,x,y+r,x-r/4,y+r)
    tri(x,y,x-r/2,y+r*3/4,x-r/4,y+r)
    #zone3
    tri(x,y,x-r/2,y+r*3/4,x-r*3/4,y+r/2)
    tri(x,y,x-r*3/4,y+r/2,x-r*3/4,y)
    #zone4
    tri(x,y,x-r*3/4,y-r/2,x-r*3/4,y)
    tri(x,y,x-r*3/4,y-r/2,x-r/2,y-r*3/4)
    #zone5
    tri(x,y,x-r/4,y-r,x-r/2,y-r*3/4)
    tri(x,y,x-r/4,y-r,x,y-r)
    #zone6
    tri(x,y,x+r/4,y-r,x,y-r)
    tri(x,y,x+r/4,y-r,x+r/2,y-r*3/4)
    #zone7
    tri(x,y,x+r/2,y-r*3/4,x+r*3/4,y-r/2)

  elif direction == "up":
    #zone0
    tri(x,y,x+r/2,y+r*(3/4),x+r*(3/4),y+r/2)
    tri(x,y,x+r*3/4,y,x+r*3/4,y+r/2)
    #zone1
    tri(x,y,x+r/2,y+r*3/4,x+r/4,y+r)
    #zone2
    tri(x,y,x-r/2,y+r*3/4,x-r/4,y+r)
    #zone3
    tri(x,y,x-r/2,y+r*3/4,x-r*3/4,y+r/2)
    tri(x,y,x-r*3/4,y+r/2,x-r*3/4,y)
    #zone4
    tri(x,y,x-r*3/4,y-r/2,x-r*3/4,y)
    tri(x,y,x-r*3/4,y-r/2,x-r/2,y-r*3/4)
    #zone5
    tri(x,y,x-r/4,y-r,x-r/2,y-r*3/4)
    tri(x,y,x-r/4,y-r,x,y-r)
    #zone6
    tri(x,y,x+r/4,y-r,x,y-r)
    tri(x,y,x+r/4,y-r,x+r/2,y-r*3/4)
    #zone7
    tri(x,y,x+r/2,y-r*3/4,x+r*3/4,y-r/2)
    tri(x,y,x+r*3/4,y,x+r*3/4,y-r/2)

  elif direction == "down":
    #zone0
    tri(x,y,x+r/2,y+r*(3/4),x+r*(3/4),y+r/2)
    tri(x,y,x+r*3/4,y,x+r*3/4,y+r/2)
    #zone1
    tri(x,y,x,y+r,x+r/4,y+r)
    tri(x,y,x+r/2,y+r*3/4,x+r/4,y+r)
    #zone2
    tri(x,y,x,y+r,x-r/4,y+r)
    tri(x,y,x-r/2,y+r*3/4,x-r/4,y+r)
    #zone3
    tri(x,y,x-r/2,y+r*3/4,x-r*3/4,y+r/2)
    tri(x,y,x-r*3/4,y+r/2,x-r*3/4,y)
    #zone4
    tri(x,y,x-r*3/4,y-r/2,x-r*3/4,y)
    tri(x,y,x-r*3/4,y-r/2,x-r/2,y-r*3/4)
    #zone5
    tri(x,y,x-r/4,y-r,x-r/2,y-r*3/4)
    #zone6
    tri(x,y,x+r/4,y-r,x+r/2,y-r*3/4)
    #zone7
    tri(x,y,x+r/2,y-r*3/4,x+r*3/4,y-r/2)
    tri(x,y,x+r*3/4,y,x+r*3/4,y-r/2)

  elif direction == "left":
    #zone0
    tri(x,y,x+r/2,y+r*(3/4),x+r*(3/4),y+r/2)
    tri(x,y,x+r*3/4,y,x+r*3/4,y+r/2)
    #zone1
    tri(x,y,x,y+r,x+r/4,y+r)
    tri(x,y,x+r/2,y+r*3/4,x+r/4,y+r)
    #zone2
    tri(x,y,x,y+r,x-r/4,y+r)
    tri(x,y,x-r/2,y+r*3/4,x-r/4,y+r)
    #zone3
    tri(x,y,x-r/2,y+r*3/4,x-r*3/4,y+r/2)
    #zone4
    tri(x,y,x-r*3/4,y-r/2,x-r/2,y-r*3/4)
    #zone5
    tri(x,y,x-r/4,y-r,x-r/2,y-r*3/4)
    tri(x,y,x-r/4,y-r,x,y-r)
    #zone6
    tri(x,y,x+r/4,y-r,x,y-r)
    tri(x,y,x+r/4,y-r,x+r/2,y-r*3/4)
    #zone7
    tri(x,y,x+r/2,y-r*3/4,x+r*3/4,y-r/2)
    tri(x,y,x+r*3/4,y,x+r*3/4,y-r/2)

#### BLUE BARS ####

#Inner outline
gl.glColor3f(0,0,1)
gl.glBegin(gl.GL_LINES)
gl.glVertex2f(-0.94,0.94)
gl.glVertex2f(0.94,0.94)
gl.glVertex2f(0.94,-0.94)
gl.glVertex2f(-0.94,-0.94)
gl.glVertex2f(-0.94,0.94)
gl.glVertex2f(-0.94,-0.94)
gl.glVertex2f(0.94,0.94)
gl.glVertex2f(0.94,-0.94)
gl.glEnd()

#Outer outline
gl.glColor3f(0,0,1)
gl.glBegin(gl.GL_LINES)
gl.glVertex2f(-0.98,0.98)
gl.glVertex2f(0.98,0.98)
gl.glVertex2f(0.98,-0.98)
gl.glVertex2f(-0.98,-0.98)
gl.glVertex2f(-0.98,0.98)
gl.glVertex2f(-0.98,-0.98)
gl.glVertex2f(0.98,0.98)
gl.glVertex2f(0.98,-0.98)
gl.glEnd()

#Center Top slab
gl.glColor3f(0,0,1)
gl.glBegin(gl.GL_LINES)
gl.glVertex2f(-0.02,0.94)
gl.glVertex2f(-0.02,0.5)
gl.glVertex2f(0.02,0.94)
gl.glVertex2f(0.02,0.5)
gl.glVertex2f(0.02,0.5)
gl.glVertex2f(-0.02,0.5)
gl.glEnd()

#rect obstacles left1
gl.glColor3f(0,0,1)
gl.glBegin(gl.GL_LINES)
gl.glVertex2f(-0.75,0.5)
gl.glVertex2f(-0.65,0.5)
gl.glVertex2f(-0.65,0.7)
gl.glVertex2f(-0.75,0.7)
gl.glVertex2f(-0.75,0.5)
gl.glVertex2f(-0.75,0.7)
gl.glVertex2f(-0.65,0.5)
gl.glVertex2f(-0.65,0.7)
gl.glEnd()

#rect obstacles left2
gl.glColor3f(0,0,1)
gl.glBegin(gl.GL_LINES)
gl.glVertex2f(-0.45,0.5)
gl.glVertex2f(-0.2,0.5)
gl.glVertex2f(-0.2,0.7)
gl.glVertex2f(-0.45,0.7)
gl.glVertex2f(-0.45,0.5)
gl.glVertex2f(-0.45,0.7)
gl.glVertex2f(-0.2,0.5)
gl.glVertex2f(-0.2,0.7)
gl.glEnd()

#rect obstacles right1
gl.glColor3f(0,0,1)
gl.glBegin(gl.GL_LINES)
gl.glVertex2f(0.75,0.5)
gl.glVertex2f(0.65,0.5)
gl.glVertex2f(0.65,0.7)
gl.glVertex2f(0.75,0.7)
gl.glVertex2f(0.75,0.5)
gl.glVertex2f(0.75,0.7)
gl.glVertex2f(0.65,0.5)
gl.glVertex2f(0.65,0.7)
gl.glEnd()

#rect obstacles right2
gl.glColor3f(0,0,1)
gl.glBegin(gl.GL_LINES)
gl.glVertex2f(0.45,0.5)
gl.glVertex2f(0.2,0.5)
gl.glVertex2f(0.2,0.7)
gl.glVertex2f(0.45,0.7)
gl.glVertex2f(0.45,0.5)
gl.glVertex2f(0.45,0.7)
gl.glVertex2f(0.2,0.5)
gl.glVertex2f(0.2,0.7)
gl.glEnd()

#slab left
gl.glColor3f(0,0,1)
gl.glBegin(gl.GL_LINES)
gl.glVertex2f(-0.94,0.15)
gl.glVertex2f(-0.65,0.15)
gl.glVertex2f(-0.65,0.2)
gl.glVertex2f(-0.94,0.2)
gl.glVertex2f(-0.94,0.15)
gl.glVertex2f(-0.94,0.2)
gl.glVertex2f(-0.65,0.15)
gl.glVertex2f(-0.65,0.2)
gl.glEnd()

#slab right
gl.glColor3f(0,0,1)
gl.glBegin(gl.GL_LINES)
gl.glVertex2f(0.94,0.15)
gl.glVertex2f(0.65,0.15)
gl.glVertex2f(0.65,0.2)
gl.glVertex2f(0.94,0.2)
gl.glVertex2f(0.94,0.15)
gl.glVertex2f(0.94,0.2)
gl.glVertex2f(0.65,0.15)
gl.glVertex2f(0.65,0.2)
gl.glEnd()

#monster cage
gl.glColor3f(0.8706,0.6471,0.6431)
gl.glBegin(gl.GL_LINES)
gl.glVertex2f(-0.3,-0.6)
gl.glVertex2f(0.3,-0.6)
gl.glColor3f(0,0,1)
gl.glVertex2f(0.3,-0.9)
gl.glVertex2f(-0.3,-0.9)
gl.glVertex2f(-0.3,-0.6)
gl.glVertex2f(-0.3,-0.9)
gl.glVertex2f(0.3,-0.6)
gl.glVertex2f(0.3,-0.9)
gl.glEnd()

#'T' center
gl.glColor3f(0,0,1)
gl.glBegin(gl.GL_LINES)
gl.glVertex2f(-0.18,0.15)
gl.glVertex2f(0.18,0.15)
gl.glVertex2f(0.18,0.2)
gl.glVertex2f(-0.18,0.2)
gl.glVertex2f(-0.18,0.15)
gl.glVertex2f(-0.18,0.2)
gl.glVertex2f(0.18,0.15)
gl.glVertex2f(0.18,0.2)

gl.glVertex2f(-0.02,0.15)
gl.glVertex2f(-0.02,-0.1)
gl.glVertex2f(0.02,0.15)
gl.glVertex2f(0.02,-0.1)
gl.glVertex2f(0.02,-0.1)
gl.glVertex2f(-0.02,-0.1)
gl.glEnd()

#Degree of rotation
a = math.cos(math.radians(90))
b = math.sin(math.radians(90))

c = math.cos(math.radians(-90))
d = math.sin(math.radians(-90))

#rotation matrix
r = np.array([[a, -b, 0],
             [b, a, 0],
             [0, 0, 1]])

r1 = np.array([[c, -d, 0],
             [d, c, 0],
             [0, 0, 1]])



#original matrix
v1 = np.array([[-0.18],
              [0.2],
              [1]])
v2 = np.array([[0.18],
              [0.2],
              [1]])
v3 = np.array([[0.18],
              [0.15],
              [1]])
v4 = np.array([[-0.18],
              [0.15],
              [1]])
v5 = np.array([[-0.02],
              [0.15],
              [1]])
v6 = np.array([[0.02],
              [0.15],
              [1]])
v7 = np.array([[0.02],
              [-0.1],
              [1]])
v8 = np.array([[-0.02],
              [-0.1],
              [1]])

#rotation
v11 = np.matmul(r,v1)
v22 = np.matmul(r,v2)
v33 = np.matmul(r,v3)
v44 = np.matmul(r,v4)
v55 = np.matmul(r,v5)
v66 = np.matmul(r,v6)
v77 = np.matmul(r,v7)
v88 = np.matmul(r,v8)

v11a = np.matmul(r1,v1)
v22b = np.matmul(r1,v2)
v33c = np.matmul(r1,v3)
v44d = np.matmul(r1,v4)
v55e = np.matmul(r1,v5)
v66f = np.matmul(r1,v6)
v77g = np.matmul(r1,v7)
v88h = np.matmul(r1,v8)

#matrix T left
gl.glColor3f(0,0,1)
gl.glBegin(gl.GL_LINES)
gl.glVertex2f(v11[0][0]-0.25,v11[1][0]-0.1)
gl.glVertex2f(v22[0][0]-0.25,v22[1][0]-0.1)
gl.glVertex2f(v22[0][0]-0.25,v22[1][0]-0.1)
gl.glVertex2f(v33[0][0]-0.25,v33[1][0]-0.1)
gl.glVertex2f(v33[0][0]-0.25,v33[1][0]-0.1)
gl.glVertex2f(v44[0][0]-0.25,v44[1][0]-0.1)
gl.glVertex2f(v44[0][0]-0.25,v44[1][0]-0.1)
gl.glVertex2f(v11[0][0]-0.25,v11[1][0]-0.1)
gl.glEnd()

gl.glColor3f(0,0,1)
gl.glBegin(gl.GL_LINES)
gl.glVertex2f(v55[0][0]-0.25,v55[1][0]-0.1)
gl.glVertex2f(v66[0][0]-0.25,v66[1][0]-0.1)
gl.glVertex2f(v66[0][0]-0.25,v66[1][0]-0.1)
gl.glVertex2f(v77[0][0]-0.3,v77[1][0]-0.1)
gl.glVertex2f(v77[0][0]-0.3,v77[1][0]-0.1)
gl.glVertex2f(v88[0][0]-0.3,v88[1][0]-0.1)
gl.glVertex2f(v88[0][0]-0.3,v88[1][0]-0.1)
gl.glVertex2f(v55[0][0]-0.25,v55[1][0]-0.1)

gl.glEnd()

#matrix T right
gl.glColor3f(0,0,1)
gl.glBegin(gl.GL_LINES)
gl.glVertex2f(v11a[0][0]+0.25,v11a[1][0]-0.1)
gl.glVertex2f(v22b[0][0]+0.25,v22b[1][0]-0.1)
gl.glVertex2f(v22b[0][0]+0.25,v22b[1][0]-0.1)
gl.glVertex2f(v33c[0][0]+0.25,v33c[1][0]-0.1)
gl.glVertex2f(v33c[0][0]+0.25,v33c[1][0]-0.1)
gl.glVertex2f(v44d[0][0]+0.25,v44d[1][0]-0.1)
gl.glVertex2f(v44d[0][0]+0.25,v44d[1][0]-0.1)
gl.glVertex2f(v11a[0][0]+0.25,v11a[1][0]-0.1)
gl.glEnd()

gl.glColor3f(0,0,1)
gl.glBegin(gl.GL_LINES)
gl.glVertex2f(v55e[0][0]+0.25,v55e[1][0]-0.1)
gl.glVertex2f(v66f[0][0]+0.25,v66f[1][0]-0.1)
gl.glVertex2f(v66f[0][0]+0.25,v66f[1][0]-0.1)
gl.glVertex2f(v77g[0][0]+0.3,v77g[1][0]-0.1)
gl.glVertex2f(v77g[0][0]+0.3,v77g[1][0]-0.1)
gl.glVertex2f(v88h[0][0]+0.3,v88h[1][0]-0.1)
gl.glVertex2f(v88h[0][0]+0.3,v88h[1][0]-0.1)
gl.glVertex2f(v55e[0][0]+0.25,v55e[1][0]-0.1)

gl.glEnd()

##### Black Line trail #####
def lines(x1,y1,x2,y2):
  gl.glLineWidth(4)
  gl.glBegin(gl.GL_LINES)
  gl.glColor3f(0,0,0)
  gl.glVertex2f(x1,y1)
  gl.glVertex2f(x2,y2)
  gl.glEnd()

### POINTS ###
def points():
  y1 = -0.45
  y2 = 0.35
  i = -0.85
  while i<=0.85:
    gl.glPointSize(3)
    gl.glBegin(gl.GL_POINTS)
    gl.glColor3f(0,1,1)
    gl.glVertex2f(i,y1)
    gl.glVertex2f(i,y2)
    gl.glEnd()
    i+=0.05
  y = 0.8
  i = -0.85
  j = 0.1
  while i<-0.05:
    gl.glPointSize(3)
    gl.glBegin(gl.GL_POINTS)
    gl.glColor3f(0,1,1)
    gl.glVertex2f(i,y)
    gl.glVertex2f(j,y)
    gl.glEnd()
    i+=0.05
    j+=0.05

  x1 = 0.1
  x2 = -x1
  x3 = 0.85
  x4 = -x3
  i = 0.35
  while i<=0.85:
    gl.glPointSize(3)
    gl.glBegin(gl.GL_POINTS)
    gl.glColor3f(0,1,1)
    gl.glVertex2f(x1,i)
    gl.glVertex2f(x2,i)
    gl.glVertex2f(x3,i)
    gl.glVertex2f(x4,i)
    gl.glEnd()
    i+=0.05

  x1 = 0.55
  x2 = -x1
  i = -0.45
  while i<=0.85:
    gl.glPointSize(3)
    gl.glBegin(gl.GL_POINTS)
    gl.glColor3f(0,1,1)
    gl.glVertex2f(x1,i)
    gl.glVertex2f(x2,i)
    gl.glEnd()
    i+=0.05

  gl.glPointSize(3)
  gl.glBegin(gl.GL_POINTS)
  gl.glColor3f(0,0,0)
  gl.glVertex2f(0.85,0.35)
  gl.glVertex2f(-0.85,0.35)
  gl.glEnd()

### CALLING POINTS ###

points()

##### Input ####
inp = input("Please Enter starting coordinates (for example= 0,0.35) :  ").split(",")
x1, y1 = float(inp[0]),float(inp[1]) #0,0.35
inp2 =  input("Please Enter ending coordinates (for example = 0.5, 0.35) : ").split(",")
userX, userY = float(inp2[0]), float(inp2[1]) #0, 0.35

direction = input("Please Enter Direction (right, left, up or down) :")

##### GHOST #####
tri(0.185,-0.65,0.215,-0.65,0.20,-0.73,"G1")
tri(0.185,-0.65,0.20,-0.73,0.16,-0.69,"G1")
tri(0.16,-0.69,0.20,-0.73,0.15,-0.73,"G1")
tri(0.215,-0.65,0.20,-0.73,0.24,-0.69,"G1")
tri(0.24,-0.69,0.20,-0.73,0.25,-0.73,"G1")
quad(0.15,0.25,0.-0.73,-0.8,"G1")

g1 = np.array([[0.185],
            [-0.65],
            [1]])
g2 = np.array([[0.215],
            [-0.65],
            [1]])
g3 = np.array([[0.2],
            [-0.73],
            [1]])
g4 = np.array([[0.16],
            [-0.69],
            [1]])
g5 = np.array([[0.15],
            [-0.73],
            [1]])
g6 = np.array([[0.24],
            [-0.69],
            [1]])
g7 = np.array([[0.25],
            [-0.73],
            [1]])
g8 = np.array([[0.25],
            [-0.8],
            [1]])

g11 =  np.matmul(rf_Y,g1)
g22 =  np.matmul(rf_Y,g2)
g33 =  np.matmul(rf_Y,g3)
g44 =  np.matmul(rf_Y,g4)
g55 =  np.matmul(rf_Y,g5)
g66 =  np.matmul(rf_Y,g6)
g77 =  np.matmul(rf_Y,g7)
g88 =  np.matmul(rf_Y,g8)

tri(g11[0][0],g11[1][0],g22[0][0],g22[1][0],g33[0][0],g33[1][0],"G2")
tri(g11[0][0],g11[1][0],g33[0][0],g33[1][0],g44[0][0],g44[1][0],"G2")
tri(g44[0][0],g44[1][0],g33[0][0],g33[1][0],g55[0][0],g55[1][0],"G2")
tri(g22[0][0],g22[1][0],g33[0][0],g33[1][0],g66[0][0],g66[1][0],"G2")
tri(g66[0][0],g66[1][0],g33[0][0],g33[1][0],g77[0][0],g77[1][0],"G2")
quad(g55[0][0],g88[0][0],g55[1][0],g88[1][0],"G2")

g11 =  np.matmul(t_g,g1)
g22 =  np.matmul(t_g,g2)
g33 =  np.matmul(t_g,g3)
g44 =  np.matmul(t_g,g4)
g55 =  np.matmul(t_g,g5)
g66 =  np.matmul(t_g,g6)
g77 =  np.matmul(t_g,g7)
g88 =  np.matmul(t_g,g8)

tri(g11[0][0],g11[1][0],g22[0][0],g22[1][0],g33[0][0],g33[1][0],"G2")
tri(g11[0][0],g11[1][0],g33[0][0],g33[1][0],g44[0][0],g44[1][0],"G2")
tri(g44[0][0],g44[1][0],g33[0][0],g33[1][0],g55[0][0],g55[1][0],"G2")
tri(g22[0][0],g22[1][0],g33[0][0],g33[1][0],g66[0][0],g66[1][0],"G2")
tri(g66[0][0],g66[1][0],g33[0][0],g33[1][0],g77[0][0],g77[1][0],"G2")
quad(g55[0][0],g88[0][0],g55[1][0],g88[1][0],"G2")


g11 =  np.matmul(rf_Y_t_g2,g1)
g22 =  np.matmul(rf_Y_t_g2,g2)
g33 =  np.matmul(rf_Y_t_g2,g3)
g44 =  np.matmul(rf_Y_t_g2,g4)
g55 =  np.matmul(rf_Y_t_g2,g5)
g66 =  np.matmul(rf_Y_t_g2,g6)
g77 =  np.matmul(rf_Y_t_g2,g7)
g88 =  np.matmul(rf_Y_t_g2,g8)

tri(g11[0][0],g11[1][0],g22[0][0],g22[1][0],g33[0][0],g33[1][0],"G1")
tri(g11[0][0],g11[1][0],g33[0][0],g33[1][0],g44[0][0],g44[1][0],"G1")
tri(g44[0][0],g44[1][0],g33[0][0],g33[1][0],g55[0][0],g55[1][0],"G1")
tri(g22[0][0],g22[1][0],g33[0][0],g33[1][0],g66[0][0],g66[1][0],"G1")
tri(g66[0][0],g66[1][0],g33[0][0],g33[1][0],g77[0][0],g77[1][0],"G1")
quad(g55[0][0],g88[0][0],g55[1][0],g88[1][0],"G1")

#Eyes
gl.glColor3f(1,1,1)
gl.glPointSize(8)
gl.glBegin(gl.GL_POINTS)
gl.glVertex2f(0.225,-0.73)
gl.glVertex2f(0.175,-0.73)
gl.glVertex2f(-0.225,-0.73)
gl.glVertex2f(-0.175,-0.73)
gl.glVertex2f(0.225,0.02)
gl.glVertex2f(0.175,0.02)
gl.glVertex2f(-0.225,0.37)
gl.glVertex2f(-0.175,0.37)
gl.glEnd()

gl.glColor3f(0,0,0)
gl.glPointSize(4)
gl.glBegin(gl.GL_POINTS)
gl.glVertex2f(0.225,-0.73)
gl.glVertex2f(0.175,-0.73)
gl.glVertex2f(-0.225,-0.73)
gl.glVertex2f(-0.175,-0.73)
gl.glVertex2f(0.225,0.02)
gl.glVertex2f(0.175,0.02)
gl.glVertex2f(-0.225,0.37)
gl.glVertex2f(-0.175,0.37)
gl.glEnd()


######## HEARTS/LIVES #####
tri(0.7,-0.7,0.72,-0.75,0.68,-0.75,"H")
tri(0.74,-0.7,0.72,-0.75,0.76,-0.75,"H")
quad(0.68,0.76,-0.75,-0.8,"H")
tri(0.68,-0.8,0.76,-0.8,0.72,-0.9,"H")

h1 = np.array([[0.7],
            [-0.7],
            [1]])
h2 = np.array([[0.72],
            [-0.75],
            [1]])
h3 = np.array([[0.68],
            [-0.75],
            [1]])
h4 = np.array([[0.74],
            [-0.7],
            [1]])
h5 = np.array([[0.76],
            [-0.75],
            [1]])
h6 = np.array([[0.68],
            [-0.8],
            [1]])
h7 = np.array([[0.76],
            [-0.8],
            [1]])
h8 = np.array([[0.72],
            [-0.9],
            [1]])
h11 =  np.matmul(t_hearts,h1)
h22 =  np.matmul(t_hearts,h2)
h33 =  np.matmul(t_hearts,h3)
h44 =  np.matmul(t_hearts,h4)
h55 =  np.matmul(t_hearts,h5)
h66 =  np.matmul(t_hearts,h6)
h77 =  np.matmul(t_hearts,h7)
h88 =  np.matmul(t_hearts,h8)

if -0.225 <= userX <= -0.15 and userY == 0.35:
  pass
else:
  tri(h11[0][0],h11[1][0],h22[0][0],h22[1][0],h33[0][0],h33[1][0],"H")
  tri(h44[0][0],h44[1][0],h22[0][0],h22[1][0],h55[0][0],h55[1][0],"H")
  quad(h33[0][0],h77[0][0],h33[1][0],h77[1][0],"H")
  tri(h66[0][0],h66[1][0],h77[0][0],h77[1][0],h88[0][0],h88[1][0],"H")



if -0.225 <= userX <= -0.15 and userY == 0.35:
  direction = "wrong"

#### Calling Functions #####

### Mouth Placement ###
if direction == "right":
  lines(x1-0.01,y1,userX-0.09,userY)
elif direction == "up":
  lines(x1,y1-0.01,userX,userY-0.09)
elif direction == "left":
  lines(x1+0.01,y1,userX+0.09,userY)
elif direction == "down":
  lines(x1,y1+0.01,userX,userY+0.09)

if -0.225 <= userX <= -0.15 and userY == 0.35:
  pass
else:
  pacman(userX,userY,0.09, direction)

##### FRUITS ######
drawfruit(-850,350,50)
r = 50
x = -850
y = 350
if userX != 0.85 or userY != 0.35:
  v1 = np.array([[x],
              [y],
              [1]])
  v11 = np.matmul(rf_Y,v1)
  drawfruit(v11[0][0],v11[1][0],r)

#### SCORE ###
if userX==0 and userY==0.35:
  draw(0)
elif -0.225 <= userX <= -0.15 and userY == 0.35:
  draw(0)
elif -0.9<=userX<0 and userY == 0.35:
  draw(5)
elif 0<userX<0.85 and userY == 0.35:
  draw(3)
elif userX == 0.85 or userY == 0.35:
  draw(8)
elif 0.35<userY<=0.9:
  draw(6)
elif -0.9<=userY<0.35:
  draw(4)


from IPython.display import display
from PIL import Image

img_buf = gl.glReadPixelsub(0, 0, WIDTH, HEIGHT, gl.GL_RGB, gl.GL_UNSIGNED_BYTE)
img = np.frombuffer(img_buf,np.uint8).reshape(HEIGHT, WIDTH, 3)[::-1]
display(Image.fromarray(img,'RGB'))