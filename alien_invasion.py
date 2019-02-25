#! /anaconda3/bin/python
"""
Created on Tue Feb 19 23:06:12 2019

@author: sin
"""
import pygame
import game_functions as gf
from pygame.sprite import Group
from game_stats import GameStats

from settings import Settings
from ship import Ship
def run_game():
    #初始化pygame、设置和屏幕对象
    pygame.init()
    ai_settings = Settings()
    stats = GameStats(ai_settings)
    screen = pygame.display.set_mode(
            (ai_settings.screen_width,ai_settings.screen_height))
    pygame.display.set_caption("Alien Invasion")
    
    #创建一艘飞船,bullets fleet
    ship = Ship(ai_settings,screen)
    bullets = Group()
    aliens = Group()
    gf.create_fleet(ai_settings, screen, ship, aliens)
    
    #开始游戏主循环
    while True:
        
        gf.check_events(ai_settings, screen, ship, bullets)
        if stats.game_active:
                ship.update()
                gf.update_bullets(ai_settings , screen, ship, aliens, bullets)
                gf.update_aliens(ai_settings, stats, screen, ship, aliens, bullets)
        gf.update_screen(ai_settings, screen, ship, aliens, bullets)


run_game()
