#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Feb 24 20:04:41 2019

@author: sin
"""

import pygame

pygame.init()
img = pygame.image.load('images/ship.bmp')
rect = img.get_rect()
rect.x = rect.width
rect.y = rect.height

screen = pygame.display.set_mode((1200,800))

screen.fill((255,255,0))
screen.blit(img,rect)
pygame.display.update()

screen.fill((255,0,0))
screen.blit(img,rect)
pygame.display.flip()
