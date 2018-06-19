# coding:utf-8

# 创建实例类
import pygame
class Ship():
    def __init__(self, ai_settings, screen):
        """初始化飞船并设置其初始位置"""
        self.ai_settings = ai_settings
        self.screen = screen

        # 加载飞船图像并获取其外接矩形
        self.image = pygame.image.load('image/ship.bmp')
        self.rect = self.image.get_rect()
        self.screen_rect = screen.get_rect()

        # 将每艘新飞船放到屏幕底部中央
        self.rect.centerx = self.screen_rect.centerx
        self.rect.bottom = self.screen_rect.bottom

        self.center = float(self.rect.centerx)

        # move flag
        self.moving_right = False
        self.moving_left = False
    def update(self):
        if self.moving_left:
            self.center -= self.ai_settings.ship_speed_factor
        if self.moving_right:
            self.center += self.ai_settings.ship_speed_factor
        self.rect.centerx = self.center
        # print('screen rect', self.rect.centerx)


    def blitme(self):
        """redraw ship with image in a place"""
        self.screen.blit(self.image, self.rect)
