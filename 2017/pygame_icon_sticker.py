#!/usr/bin/python
# -*- coding: utf-8 -*-
from __future__ import absolute_import, division, unicode_literals, print_function
"""
Created on Fri Jul 28 01:15:32 2017

@author: josef
"""
'''
this idea/code I took from
http://www.geekgurldiaries.co.uk/home/blog
Monday, 10th of february 2014
"programming pictures with pygame"
(original code with small changes)
'''
import pygame

SAVEAS = '/home/josef/icon.png'

__author__ = 'Carrie Anne Philbin'

pygame.init()
clk = pygame.time.Clock()

#  squares 25x25pixel
#+ 9 columns (9x25 == 225 -> width)
#+ 6 rows (6x25 == 150 -> height)
#+ 8-bit-graphics
screen = pygame.display.set_mode((225,150),0,8)
r = pygame.Color(0, 255, 0, 255)   # green
#  funny sideeffect:
#+ icon.png shows a green invader if the chosen
#+ color was red
#+ if i choose green, then the icon.png appears in red ;-)
w = pygame.Color(255, 255, 255, 255)  # white
#add transparency
r.a = 128
pattern = [ 
 [ w, w, r, r, r, r, r, w, w ], 
 [ w, w, r, w, r, w, r, w, w ], 
 [ w, w, r, r, r, r, r, w, w ], 
 [ w, r, r, r, w, r, r, r, w ], 
 [ r, w, w, r, r, r, w, w, r ], 
 [ r, r, w, w, w, w, w, r, r ] 
]

for y, row in enumerate(pattern):
    for x, color in enumerate(row):
        rect = pygame.Rect(x*25, y*25, 25, 25)
        screen.fill(color, rect=rect)

pygame.display.flip()
pygame.image.save(screen, SAVEAS) 
while True:
    clk.tick(10)   # 10 fps genug, sonst cpu last zu hoch!
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            raise SystemExit()
