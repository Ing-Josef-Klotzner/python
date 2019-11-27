#!/usr/bin/python
# -*- coding: utf-8 -*-
from __future__ import absolute_import, division, print_function
"""
Created on Mon Sep 25 23:16:54 2017

@author: josef
"""

import pygame, sys
pygame.init()

X = 600  # screen width
Y = 600  # screen heigth

WHITE = (255, 255, 255)

screen = pygame.display.set_mode((X, Y))
pygame.display.set_caption("Demo of anti-aliasing without anti-alias")
clock = pygame.time.Clock()


def red1(d2):  # gradient function
    return [max(255-int(d2*0.5), 0), max(200-int(d2*2), 0), max(200-int(d2*2), 0)]


class Ball():
    """
    The Ball object has three parameters:
     - 'rad' is the radius in pixels
     - 'light_pos' is a (x, y) tuple, the two numbers each in the interval [-1; 1], the value
       indicates light position in radius units relative to center
     - 'color_func' is the gradient function used for colorization of the Ball object
"""
    def __init__(self, rad, light_pos, color_func):
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
                if d > rad:
                    continue
                else:
                    # rate of color intensity change
                    d2 = ((i-x1)**2 + (j-y1)**2)**0.5 * 255 / rad

                    # apply color
                    color = color_func(d2)
                    self.surf.set_at((i, j), color)

    def draw(self):
        screen.blit(self.surf, (40, 40))

    def move(self):
        pass

ball = Ball(255, (0.4, -0.4), red1)

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    clock.tick(60)
    screen.fill(WHITE)

    ball.draw()

    pygame.display.flip()

