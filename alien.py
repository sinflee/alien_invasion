#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Feb 21 20:29:22 2019

@author: sin
"""

import pygame
from pygame.sprite import Sprite

class Alien(Sprite):
    """表示单个外星人的类"""
    
    def __init__(self, ai_settings, screen):
        """初始化外星人并设置其出事位置"""
        super().__init__()
        self.screen = screen
        self.ai_settings = ai_settings   
    
        self.image = pygame.image.load('images/alien.bmp')
        self.rect = self.image.get_rect()
        
        #每个外星人最初都在屏幕左上角附近
        self.rect.x = self.rect.width
        self.rect.y = self.rect.height
        
        self.x = float(self.rect.x)
        
    def blitme(self):
        
        self.screen.blit(self.image, self.rect)
        