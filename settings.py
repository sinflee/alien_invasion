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
        self.ship_speed_factor = 3
        self.ship_limit = 3
        self.alien_speed_factor = 1.1
        self.fleet_drop_speed_factor = 1
        self.fleet_direction = 1
        #子弹设置
        self.bullet_speed_factor = 2
        self.bullet_width = 1200
        self.bullet_height = 5
        self.bullet_color = 60,60,60
        self.bullet_allowed = 5
        #提高游戏难度的参数
        self.speedup_scale = 1.1
        #记分
        self.alien_points = 50
        self.score_scale = 1.1

        self.initialize_dynamic_settings()
    
    def initialize_dynamic_settings(self):
        """初始化随游戏进行而变化的设置"""
        self.alien_speed_factor = 3
        self.bullet_speed_factor = 2
        self.ship_speed_factor = 3
        self.alien_points = 50
        self.fleet_direction = 1
    
    def increase_speed(self):
        """提高游戏速度设置"""
        self.ship_speed_factor *= self.speedup_scale
        self.alien_speed_factor *= self.speedup_scale
        self.bullet_speed_factor *= self.speedup_scale
        self.alien_points = int(self.alien_points * self.score_scale)
