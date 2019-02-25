"""
Created on Tue Feb 19 23:10:07 2019

@author: sin
"""

class Settings():
    """存储游戏的所有设置的类"""
    
    def __init__(self):
        """初始化游戏的设置"""
        #屏幕设置
        self.screen_width = 1200
        self.screen_height = 800
        self.bg_color = (230, 230, 230)
        #ship and alien's的移动速度
        self.ship_speed_factor = 10
        self.ship_limit = 3
        self.alien_speed_factor = 10
        self.fleet_drop_speed_factor = 100
        self.fleet_direction = 1
        #子弹设置
        self.bullet_speed_factor = 15
        self.bullet_width = 500
        self.bullet_height = 15
        self.bullet_color = 60,60,60
        self.bullet_allowed = 5
