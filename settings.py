# coding:utf-8

# 创建设置类
class Settings():
    """存储 ShipGame 的所有设置类"""
    def __init__(self):
        "初始化游戏设置"
        # 屏幕设置
        self.screen_width = 1200
        self.screen_height = 800
        self.bg_color = (230, 230, 230)
        # ship settings
        self.ship_speed_factor = 0.5
        self.ship_limit = 3
        # bullet settings
        self.bullet_speed_factor = 0.5
        self.bullet_width = 3
        self.bullet_height = 5
        self.bullet_color = 60, 60, 60
        self.bullets_allowed = 3

        # alien settings
        self.alien_speed_factor = 0.5
        self.fleet_drop_speed = 10
        # fleet_direction = 1 means right, -1 means left
        self.fleet_direction = 1



