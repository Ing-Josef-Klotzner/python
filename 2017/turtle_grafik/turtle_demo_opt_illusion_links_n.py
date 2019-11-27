#!/usr/bin/python
# -*- coding: utf-8 -*-
from __future__ import absolute_import, division, print_function
"""
Created on Mon Sep 25 23:16:54 2017

@author: josef
"""
import itertools
from time import sleep
from turtle import up, down, bk, fd, rt, lt, done, bgcolor, pencolor, pensize, circle, speed, delay, fillcolor, begin_fill, end_fill, begin_poly, end_poly, get_poly, register_shape, shape, clear, reset, color, exitonclick, stamp

def draw_7_shape(_shape, out_rad, in_rad, step=-10):
    toggle = itertools.cycle(['white','black']).next
    down()
    begin_poly()
    for oc in range(out_rad, in_rad, step):
        cur_color = toggle()
        color(cur_color, cur_color)
#        fillcolor(cur_color)
#        pencolor(cur_color)
        circle(oc)
#        begin_fill()
#        circle(oc)
#        end_fill()
    end_poly()
    spir = get_poly()
    register_shape(_shape, spir)
    clear()
    up()

up()
#delay(10)
speed(0)
bgcolor("white")

fd(270)
lt(90)
down()
#begin_poly()
#circle(290)
up()
rt(90)

#bk(20)
lt(90)
draw_7_shape("spiral1",270,190)
#lt(90)
#fd(360)
#lt(90)
draw_7_shape("spiral2",190,110)
#lt(90)
#fd(220)
#lt(90)
draw_7_shape("spiral3",110,20)

begin_poly()
shape("spiral1")
fillcolor("black")
stamp()
shape("spiral2")
lt(90)
fd(190)
lt(90)
stamp()
shape("spiral3")
lt(90)
fd(110)
stamp()
end_poly()
spir = get_poly()
register_shape("spiral", spir)
shape("spiral")
reset()
speed(0)
#fillcolor("black")
while True:
    lt(2)
#done()


