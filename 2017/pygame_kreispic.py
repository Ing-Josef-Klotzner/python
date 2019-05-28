#!/usr/bin/python
# -*- coding: utf-8 -*-
from __future__ import absolute_import, division, unicode_literals, print_function
"""
Created on Fri Jul 28 01:19:49 2017

@author: josef
"""


#! /opt/bin/python3

'''
create ball-image by yourself
save it as png
and move the newly created image through
a rectangle to prove its transparency
'''
import os
import pygame

pygame.init()

FNAME = '/dev/shm/kreis.png'
WHITE = pygame.Color(255, 255, 255, 255)  # white
WHITE.a = 0
YELLOW = pygame.Color(255, 255, 0, 255)  # yellow
# strange thing - I have to choose green to receive red in png-file!
RED = pygame.Color(255, 0, 0, 255)
RED_trans = pygame.Color(255, 0, 0, 200)
BLUE = pygame.Color(0, 0, 255, 255)
FPS = 30

# create surface for circle 
# right now i don't know it better
screen = pygame.display.set_mode((200,200),pygame.NOFRAME,8)
forkreis = screen.convert_alpha()
forkreis.fill(WHITE)

pygame.draw.circle(forkreis, RED_trans,(100,100),100)
pygame.image.save(forkreis, FNAME)

#change display back to normal
pygame.display.set_mode((800,600),0,32)
pygame.display.set_caption("transparent")

myrect = pygame.Rect(375,250,50,100)
myrect2 = pygame.Rect(175,270,50,100)
myrect3 = pygame.Rect(575,290,50,100)
mycircle = pygame.image.load(FNAME).convert_alpha()

clock = pygame.time.Clock()
speed = 100

x = 0

shallcontinue = True
while shallcontinue:
    ms = clock.tick(FPS)
    s = ms/1000
    x += speed*s
    if x > 600:
        speed = -speed
    elif x < 0:
        speed = -speed
        x = 0
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            shallcontinue = False
        if event.type == pygame.KEYDOWN:
            if event.key in (pygame.K_q,pygame.K_ESCAPE):
                shallcontinue = False
    screen.lock()
    screen.fill((0,0,0))
    pygame.draw.rect(screen, YELLOW, myrect)
    pygame.draw.rect(screen, BLUE, myrect2)
    pygame.draw.rect(screen, RED, myrect3)
    screen.unlock()
    screen.blit(mycircle, (x,300))
    pygame.display.flip()

pygame.quit()
os.remove(FNAME)