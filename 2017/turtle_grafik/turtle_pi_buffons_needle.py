#!/usr/bin/python
# -*- coding: utf-8 -*-
from __future__ import absolute_import, division, print_function
#Estimating Pi using Buffon's Needle # www.101compiting.net/estimating-pi-using-buffons-needle

import turtle
import random
from math import sin

boardWidth = 40
needleLength = 30
numberOfNeedles = 1000
    
myPen = turtle.Turtle()
myPen.hideturtle()
myPen.speed(0)
turtle.delay(0)

omega = 2 * 3.141593
lines_y = range(-180, 181, 40)
Crossing_needles = 0

def check_line_crossing(y, angle, needleLength, lines_y):
    if angle == 0:
        y_end = y
    else:
        y_end = int(sin(omega * angle / 360) * needleLength + y)
    for line_y in lines_y:
#        print("y      " + str(y))
#        print("line_y " + str(line_y))
#        print("y_end  " + str(y_end))
#        print(angle)
        if y == y_end:
            if y == line_y:
#                print("True")
                return True
        if y > y_end:
            if y >= line_y and line_y >= y_end:
#                print("True")
                return True
        elif y_end >= line_y and line_y >= y:
#                print("True")
                return True
#    print("False")
#    print()
    return False
    

#Draw floor boards
for y in lines_y:
    myPen.penup()
    myPen.goto(-250,y)
    myPen.pendown()
    myPen.goto(250,y)

#Draw Needles
#myPen.color("#f442d1")
for needle in range(0,numberOfNeedles):
    x=random.randint(-190,190)
    y=random.randint(-190,190)
    angle=random.randint(0,360)
    if check_line_crossing(y,angle,needleLength, lines_y):
        myPen.color("#008f00")
        Crossing_needles += 1
    else:
        myPen.color("#f422d1")
        pass
    myPen.penup()
    myPen.goto(x,y)
    myPen.setheading(angle)
    myPen.pendown()
    myPen.forward(needleLength)
  
print("L = " + str(needleLength))
print("N = " + str(numberOfNeedles))
print("W = " + str(boardWidth))
print("C = " + str(Crossing_needles))
print("Pi = " + str(2.1*needleLength*numberOfNeedles/(Crossing_needles*boardWidth)))

turtle.done()
