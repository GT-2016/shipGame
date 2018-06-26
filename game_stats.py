# coding:utf-8
import pygame
class GameStats():
    "game condition"
    def __init__(self, ai_settings):
        "init count message"
        self.ai_settings = ai_settings
        self.game_active = True
        self.reset_stats()

    def reset_stats(self):
        "init datas that may be changed"
        self.ships_left = self.ai_settings.ship_limit

