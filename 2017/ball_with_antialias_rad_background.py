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

background = pygame.surface.Surface((X, Y))
for i in range(100):
    pygame.draw.rect(background, (0, int(i*2.5), 255-int(i*2.5)), (i*6, 0, 6, Y), 0)


def red1(d2):
    return [max(255-int(d2*0.5), 0), max(200-int(d2*2), 0), max(200-int(d2*2), 0)]


def red2(d2):
    return [max(255-int(d2*0.5), 0), max(200-int(d2*2), 0), 0]


def red3(d2):
    return [max(255-int(d2*0.5), 0), 0, max(200-int(d2*2), 0)]


def green1(d2):
    return [max(200-int(d2*2), 0), max(255-int(d2*0.5), 0), max(200-int(d2*2), 0)]


def green2(d2):
    return [0, max(255-int(d2*0.5), 0), max(200-int(d2*2), 0)]


def green3(d2):
    return [max(200-int(d2*2), 0), max(255-int(d2*0.5), 0), 0]


def blue1(d2):
    return [max(200-int(d2*2), 0), max(200-int(d2*2), 0), max(255-int(d2*0.3), 0)]


def blue2(d2):
    return [max(200-int(d2*2), 0), 0, max(255-int(d2*0.3), 0)]


def blue3(d2):
    return [0, max(200-int(d2*2), 0), max(255-int(d2*0.3), 0)]


def cyan1(d2):
    return [max(200-int(d2*2), 0), max(255-int(d2*0.3), 0), max(255-int(d2*0.3), 0)]


def magenta1(d2):
    return [max(255-int(d2*0.3), 0), max(100-int(d2*1.5), 0), max(255-int(d2*0.3), 0)]


def yellow1(d2):
    return [max(255-int(d2*0.6), 0), max(255-int(d2*0.6), 0), 0]


color_functions = [red1, red2, red3, green1, green2, green3, blue1, blue2, blue3, cyan1, magenta1, yellow1]


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

        self.perimeter = []  # list of pixels that needs anti-aliasing

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

                    if d > rad:  # prepare for anti-aliasing, get the perimeter pixels
                        alfa = d-rad
                        color_rim = [c * (1-alfa) for c in color]
                        self.perimeter.append(((i, j), color_rim, alfa))
                        color = transparent  # colorkey at rim

                    self.surf.set_at((i, j), color)

    def draw(self):
        """
    first: the self.surf (picture without perimeter) is blitted to screen
    second: the perimeter is updated, anti-aliasing to the background
    """
        screen.blit(background, (0, 0))
        screen.blit(self.surf, (40, 40))  # hard coded position

        # anti-aliasing
        for p in self.perimeter:
            x, y = p[0]
            x += 40  # hard coded position
            y += 40
            color = p[1]
            alfa = p[2]
            bg = screen.get_at((x, y))
            color_aa = [rim + back * alfa for rim, back in zip(color, bg)]
            screen.set_at((x, y), color_aa)

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

    ball.draw()

    pygame.display.flip()

