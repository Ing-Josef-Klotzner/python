#!/usr/bin/python
# -*- coding: utf-8 -*-
from __future__ import absolute_import, division, print_function
"""
Created on Mon Sep 25 23:16:54 2017

@author: josef
"""

import turtle
myPen = turtle.Turtle()
myPen.shape("arrow")

myPen.color("red")
turtle.delay(5) #Set the speed of the turtle

for i in range(0,11):
    yFrom=10-i
    #xTo=i
    myPen.penup()
    myPen.goto(0,20*yFrom)
    myPen.pendown()
    myPen.goto(20*i,0)
    
for i in range(0,11):
    yFrom=-i
    xTo=10-i
    myPen.penup()
    myPen.goto(0,20*yFrom)
    myPen.pendown()
    myPen.goto(20*xTo,0)
    
for i in range(0,11):
    yFrom=-i
    xTo=-10+i
    myPen.penup()
    myPen.goto(0,20*yFrom)
    myPen.pendown()
    myPen.goto(20*xTo,0)
    
for i in range(0,11):
    yFrom=i
    xTo=-10+i
    myPen.penup()
    myPen.goto(0,20*yFrom)
    myPen.pendown()
    myPen.goto(20*xTo,0)
    
turtle.done()
