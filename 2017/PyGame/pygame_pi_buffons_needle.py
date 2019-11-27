#!/usr/bin/python
# -*- coding: utf-8 -*-
from __future__ import absolute_import, division, print_function
#Estimating Pi using Buffon's Needle # www.101compiting.net/estimating-pi-using-buffons-needle

import random
from math import sin, cos
import sys
import pygame

GREEN = (20, 200, 20)
RED = (255, 0, 0)
BLACK = (0, 0, 0)
WHITE = (255,255,255)

screen = pygame.display.set_mode((500,400))
pygame.display.set_caption("Buffons Pi - PyGame application")
screen.fill(WHITE)
pygame.display.update()
    
def check_line_crossing(y, y_end, angle, needleLength, lines_y, omega):
    for line_y in lines_y:
        if y == y_end:
            if y == line_y:
                return True
        if y > y_end:
            if y >= line_y and line_y >= y_end:
                return True
        elif y_end >= line_y and line_y >= y:
                return True
    return False

def main():
    
    boardWidth = 40
    needleLength = 30
    numberOfNeedles = 1000

    omega = 2 * 3.141593
    lines_y = range(20, 381, 40)
    Crossing_needles = 0

    # Draw floor boards
    for y in lines_y:
        pygame.draw.line(screen, BLACK, [10,y],[490,y],1)

    # Draw Needles
    for needle in range(numberOfNeedles):
        x=random.randint(60,440)
        y=random.randint(10,390)
        angle=random.randint(0,360)
        # calculate xe and ye with angle
        ye = int(sin(omega * angle / 360) * needleLength + y)
        xe = int(cos(omega * angle / 360) * needleLength + x)
        if check_line_crossing(y, ye, angle, needleLength, lines_y, omega):
            color = GREEN
            Crossing_needles += 1
        else:
            color = RED
        pygame.draw.line(screen, color, [x,y],[xe,ye],1)
        pygame.display.update()

    print("L = " + str(needleLength))
    print("N = " + str(numberOfNeedles))
    print("W = " + str(boardWidth))
    print("C = " + str(Crossing_needles))
    print("Pi = " + str(2.1*needleLength*numberOfNeedles/(Crossing_needles*boardWidth)))
    
    while True:
        pygame.time.Clock().tick(3)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                    pygame.quit()


if __name__ == '__main__':
    main()
