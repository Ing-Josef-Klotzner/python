#!/usr/bin/python
# -*- coding: utf-8 -*-
from __future__ import absolute_import, division, print_function
"""
Created on Mon Sep 25 23:16:54 2017

@author: josef
"""

import turtle, datetime, time

myPen = turtle.Turtle()
myPen.shape("arrow")
myPen.tracer(0)
myPen.speed(0)
myPen.shapesize(.5,1)
turtle.delay(0)

myPen.penup()
myPen.goto(0,-180)
myPen.pendown()
myPen.pensize(3)
myPen.color("blue")
myPen.circle(180)

for wi in range(6,361,6):   # 360/60 = 6 -- Sekundenstriche
    myPen.penup()
    myPen.goto(0,0)
    myPen.setheading(wi)
    myPen.fd(160)
    myPen.pendown()
    myPen.fd(10)

myPen.pensize(6)
for wi in range(30,361,30):   # 360/60 = 6 -- Minutenstriche
    myPen.penup()   #           bei 3,6,9,12 länger
    myPen.goto(0,0)
    myPen.setheading(wi)
    if wi % 90 == 0:
        myPen.fd(155)
        myPen.down()
        myPen.fd(15)
    else:
        myPen.fd(160)
        myPen.pendown()
        myPen.fd(10)

myPen.pensize(3)

while True:
    myPen.color("red")
    currentSecond = datetime.datetime.now().second
    currentMinute = datetime.datetime.now().minute
    currentHour = datetime.datetime.now().hour
    myPen.penup()
    myPen.goto(0,0)
    myPen.setheading(90) # Point to the top - 12 o'clock
    myPen.right(currentHour*360/12+currentMinute*360/12/60+currentSecond*360/12/60/60)
    myPen.pendown()
    myPen.pensize(7)
    myPen.forward(100)
    myPen.stamp()

    myPen.penup()
    myPen.goto(0,0)
    myPen.setheading(90) # Point to the top - 0 minute
    myPen.right(currentMinute*360/60+currentSecond*360/60/60)
    myPen.pendown()
    myPen.pensize(5)
    myPen.forward(130)
    myPen.stamp()
    
    myPen.color("green")    
    myPen.penup()
    myPen.goto(0,0)
    
    myPen.pensize(7)
    myPen.dot()
    myPen.pensize(3)
    
    myPen.setheading(90) # Point to the top - 0 minute
    myPen.right(currentSecond*360/60)
    myPen.pendown()
    myPen.forward(140)
        
    myPen.getscreen().update()

    time.sleep(.99)
    for _ in range(20):
        myPen.undo()

#    myPen.getscreen().update()

#turtle.done()
