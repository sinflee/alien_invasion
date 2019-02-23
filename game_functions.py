#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Feb 20 19:14:00 2019

@author: sin
"""

import sys
import pygame
from bullet import Bullet
from alien import Alien


def check_keydown_events(event, ai_settings, screen, ship, bullets):
    #响应按键
    if event.key == pygame.K_RIGHT:
        ship.moving_right = True
    elif event.key == pygame.K_LEFT:
        ship.moving_left = True
    elif event.key == pygame.K_UP:
        ship.moving_up = True
    elif event.key == pygame.K_DOWN:
        ship.moving_down = True
    #创建一颗子弹，并将其加入到编组bullets中
    elif event.key == pygame.K_SPACE:
        fire_bullet(ai_settings, screen, ship, bullets)
    #响应退出按钮
    elif event.key == pygame.K_q:
        sys.exit()

def check_keyup_events(event,ship):
    #响应松开
    if event.key == pygame.K_RIGHT:
        ship.moving_right = False
    elif event.key == pygame.K_LEFT:
        ship.moving_left = False
    elif event.key == pygame.K_UP:
        ship.moving_up = False
    elif event.key == pygame.K_DOWN:
        ship.moving_down = False     
def check_events(ai_settings, screen, ship, bullets):
    """相应按键和鼠标事件"""
    #监视键盘和鼠标事件
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
        #相应按键按下事件
        elif event.type == pygame.KEYDOWN:
            check_keydown_events(event, ai_settings, screen, ship, bullets)
        #相应按键弹起事件    
        elif event.type == pygame.KEYUP:
            check_keyup_events(event,ship)

def update_screen(ai_settings, screen, ship, aliens, bullets):
    """更新屏幕上的图像，并切换到新屏幕"""
    #每次循环时都重绘屏幕
    screen.fill(ai_settings.bg_color)
    #在飞船和外星人后面绘制所有子弹
    for bullet in bullets.sprites():
        bullet.draw_bullet()
    #绘制飞船
    ship.blitme()
    aliens.draw(screen)
    #让最近绘制的屏幕可见
    pygame.display.flip()

def fire_bullet(ai_settings, screen, ship, bullets):
    #如果还没有达到限制，就发射一颗子弹,并加入编组bullets中
    if len(bullets) < ai_settings.bullet_allowed:
        new_bullet = Bullet(ai_settings, screen, ship)
        bullets.add(new_bullet)
        
def update_bullets(bullets):
    """更新子弹的位置，并删除已经消失的子弹"""
    bullets.update()
    #删除已经消失的子弹
    for bullet in bullets.copy():
        if bullet.rect.bottom <= 0:
            bullets.remove(bullet)

def get_number_aliens_x(ai_settings, alien_width):
    """计算每行可以容纳多少个外星飞船"""
    available_space_x = ai_settings.screen_width - 2 * alien_width
    number_aliens_x = int(available_space_x / (2 * alien_width))
    return number_aliens_x

def get_number_aliens_y(ai_settings, ship_height, alien_height):
    """计算屏幕上班部分可以容纳多少行的飞船"""
    available_space_y = ((ai_settings.screen_height - ship_height) / 2 - 
                         alien_height )
    number_aliens_y = int(available_space_y / (1.5 * alien_height))
    print(number_aliens_y)
    return number_aliens_y

def create_alien(ai_settings, screen, aliens, alien_number, row_number):
    """创建单个外星人并放在当前行"""
    alien = Alien(ai_settings, screen)
    alien_width = alien.rect.width
    alien_height = alien.rect.height
    alien.x = alien_width + 2 * alien_width * alien_number
    alien.y = alien_height + 2 * alien_height * row_number
    alien.rect.x = alien.x
    alien.rect.y = alien.y
    aliens.add(alien)
    
def create_fleet(ai_settings, screen, ship, aliens):
    """创建外星人舰队"""
    #创建一个外星人，并计算一行可以容纳多少个外星人
    alien = Alien(ai_settings, screen)
    ship_height = ship.rect.height
    alien_number_x = get_number_aliens_x(ai_settings, alien.rect.width)
    alien_number_y = get_number_aliens_y(ai_settings, ship_height, 
                                         alien.rect.height)
    
    #创建第一行外星人
    for num_y in range(alien_number_y):
        for num_x in range(alien_number_x):
            create_alien(ai_settings, screen, aliens, num_x, num_y)

def chect_fleet_edges(ai_settings, aliens):
    """有外星人达到屏幕边缘时采取相应措施"""
    for alien in aliens.sprites():
        if alien.check_edges():
            change_fleet_direction(ai_settings, aliens)
            break
    
def change_fleet_direction(ai_settings,aliens):
    """将整群外星人向下移，并改变移动方向"""
    for alien in aliens.sprites():
        alien.rect.y += ai_settings.fleet_drop_speed_factor
    ai_settings.fleet_direction *= -1
            
def update_aliens(ai_settings, aliens):
    """更新外星人的位置"""
    chect_fleet_edges(ai_settings, aliens)
    aliens.update()