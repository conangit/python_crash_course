

import pygame.font
from pygame.sprite import Group

from ship import Ship


class Scoreboard():
    '''显示游戏得分信息'''

    def __init__(self, ai_settings, screen, stats):
        self.ai_settings = ai_settings
        self.screen = screen
        self.screen_rect = screen.get_rect()
        self.stats = stats

        self.text_color = (30, 30, 30)
        self.font = pygame.font.SysFont(None, 48)

        # 初始化得分图像
        self.prep_score()
        # 初始化最高得分图像
        self.prep_high_score()
        # 显示玩家等级
        self.prep_level()
        # 显示玩家剩余飞船数目
        self.prep_ships()

    def prep_score(self):
        '''将得分渲染成图像'''
        # 将stats.score值圆整到10的整数倍
        rounded_score = int(round(self.stats.score, -1))
        # 
        score_str = '{:,}'.format(rounded_score)
        self.score_image = self.font.render(score_str, True, self.text_color, self.ai_settings.bg_color)

        # 将得分放在屏幕右上角
        self.score_rect = self.score_image.get_rect()
        self.score_rect.right = self.screen_rect.right - 20
        self.score_rect.top = 20

    def prep_high_score(self):
        '''将最高得分渲染成图像'''
        rounded_high_score = int(round(self.stats.high_score, -1))
        high_score_str = '{:,}'.format(rounded_high_score)
        self.high_score_image = self.font.render(high_score_str, True, self.text_color, self.ai_settings.bg_color)

        # 将最高得分放在屏幕顶部中央
        self.high_score_rect = self.high_score_image.get_rect()
        self.high_score_rect.centerx = self.screen_rect.centerx
        # 不影响外星人的显示
        self.high_score_rect.top = self.screen_rect.top

    def prep_level(self):
        '''将玩家等级渲染成图像'''
        level_str = str(self.stats.level)
        self.level_image = self.font.render(level_str, True, self.text_color, self.ai_settings.bg_color)

        # 将等级放置在得分下方
        self.level_rect = self.level_image.get_rect()
        self.level_rect.right = self.score_rect.right
        self.level_rect.top = self.score_rect.bottom + 10

    def prep_ships(self):
        '''显示还剩下多少飞船'''
        self.ships = Group()
        for ship_number in range(self.stats.ships_left):
            ship = Ship(self.ai_settings, self.screen)
            ship.rect.x = 10 + ship_number * ship.rect.width
            ship.rect.y = 10
            self.ships.add(ship)

    def show_score(self):
        '''在屏幕上显示得分'''
        self.screen.blit(self.score_image, self.score_rect)
        self.screen.blit(self.high_score_image, self.high_score_rect)
        self.screen.blit(self.level_image, self.level_rect)
        # 对编组调用draw()时，Pygame自动绘制编组里面的每个元素 同aliens
        self.ships.draw(self.screen)


