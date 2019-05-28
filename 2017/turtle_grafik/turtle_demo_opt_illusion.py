#!/usr/bin/python
# -*- coding: utf-8 -*-
from __future__ import absolute_import, division, print_function
"""
Created on Mon Sep 25 23:16:54 2017

@author: josef
"""
import itertools
from time import sleep
from turtle import up, down, bk, fd, rt, lt, done, bgcolor, pencolor, pensize, circle, speed, delay, fillcolor, begin_fill, end_fill, begin_poly, end_poly, get_poly, register_shape, shape, clear, reset, color, exitonclick

def draw_7_shape(out_rad, in_rad, step=-10):
    toggle = itertools.cycle(['white','black']).next
    down()
    for oc in range(out_rad, in_rad, step):
        cur_color = toggle()
        color(cur_color, cur_color)
#        fillcolor(cur_color)
#        pencolor(cur_color)
        circle(oc)
#        begin_fill()
#        circle(oc)
#        end_fill()
    up()

up()
#delay(10)
speed(0)
bgcolor("white")

fd(270)
lt(90)
down()
begin_poly()
draw_7_shape(270,190)
lt(90)
fd(380)
lt(90)
draw_7_shape(190,110)
lt(90)
fd(240)
lt(90)
draw_7_shape(110,20)
#sleep(5)
end_poly()

spir = get_poly()
register_shape("spiral", spir)
shape("spiral")
reset()
speed(0)
fillcolor("black")
while True:
    for _ in range(180):
        lt(2)
    for _ in range(180):
        rt(2)
#done()


