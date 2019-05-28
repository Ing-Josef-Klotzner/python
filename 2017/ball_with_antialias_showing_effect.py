#!/usr/bin/python
# -*- coding: utf-8 -*-
from __future__ import absolute_import, division, print_function
"""
Created on Mon Sep 25 23:16:54 2017

@author: josef
"""

import pygame, random, sys
pygame.init()

X = 600  # screen width
Y = 600  # screen heigth

WHITE = (255, 255, 255)

screen = pygame.display.set_mode((X, Y))
pygame.display.set_caption("Demo of anti-aliasing, by DK3250")
clock = pygame.time.Clock()


def red1(d2):
    return [max(255-int(d2*0.5), 0), max(200-int(d2*2), 0), max(200-int(d2*2), 0)]


def red2(d2):
    return [max(255-int(d2*0.5), 0), max(200-int(d2*2), 0), 0]


def red3(d2):
    return [max(255-int(d2*0.5), 0), 0, max(200-int(d2*2), 0)]


color_functions = [red1, red2, red3]


class Ball():
    """
    The Ball object has three parameters:
     - 'rad' is the radius in pixels
     - 'light_pos' is a (x, y) tuple, the two numbers each in the interval [-1; 1], the value
       indicates light position in radius units relative to center
     - 'color_func' is the gradient function used for colorization of the Ball object
"""
    def __init__(self, rad, light_pos, color_func):
        self.rad = rad

        x0 = rad + 1
        y0 = rad + 1
        x1 = x0 + int(light_pos[0] * rad)
        y1 = y0 + int(light_pos[1] * rad)

        transparent = WHITE
        self.surf = pygame.surface.Surface((x0*2, y0*2))
        self.surf.fill(transparent)
        self.surf.set_colorkey(transparent)

        for i in range(x0*2):
            for j in range(y0*2):
                d = ((i-x0)**2 + (j-y0)**2)**0.5
                if d > rad+1:
                    continue
                else:
                    # rate of color intensity change
                    d2 = ((i-x1)**2 + (j-y1)**2)**0.5 * 255 / rad

                    # apply color
                    color = color_func(d2)

                    if d > rad:  # anti-alising
                        alfa = d-rad
                        bg = WHITE
                        color = [c * (1-alfa) + b * alfa for c, b in zip(color, bg)]
#                        color = [color[0] * (1-alfa) + color[1] * alfa, color[0] * (1-alfa) + color[1] * alfa, color[0] * (1-alfa) + color[1] * alfa ]

                    self.surf.set_at((i, j), color)
#   ---    showing the effect   ---
        for i in range(x0-1,x0+79):
#            print("i loop", i)
            for j in range(y0*2-1, y0*2-9, -1):
                color = self.surf.get_at((i, j))
                for ix in range(2):  # zoomfaktor 2
                    for jy in range(2):
                        self.surf.set_at((i+int(x0*.4)+ix+(i-(x0-1))*1, j-jy-((y0*2-1)-j)*1), color)
#                        print(i,j,i+150+ix+(i-(x0-1))*3, j-jy-((y0*2-1)-j)*3,color, "  ", end="")

    def draw(self):
        screen.blit(self.surf, (40, 40))

    def move(self):
        pass

ball_color = random.choice(color_functions)
ball = Ball(255, (0.4, -0.4), ball_color)

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
    clock.tick(60)
    screen.fill(WHITE)

    ball.draw()

    pygame.display.flip()
