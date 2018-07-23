

import pygame
from pygame.sprite import Group

from settings import Settings
from ship import Ship
import game_functions as gf
from game_stats import GameStats
from button import Button
from scoreboard import Scoreboard



def run_game():
    '''初始化游戏并创建一个游戏对象'''
    pygame.init()
    # 连发
    # 注意某个时刻下 只能响应一个连续按键事件
    # 即持续按下space键后 再持续按下right键 将响应right键的持续按下
    pygame.key.set_repeat(10)

    ai_settings = Settings()
    screen = pygame.display.set_mode((ai_settings.screen_width, ai_settings.screen_height))
    pygame.display.set_caption('Alien Invasion')

    # 创建飞船对象
    ship = Ship(ai_settings, screen) 

    # 创建一个用于存储子弹的编组
    bullets = Group()

    #创建存储外星人的编组
    aliens = Group()

    # 创建外星人群
    gf.create_fleet(ai_settings, screen, ship, aliens)

    # 创建一个用于统计游戏信息的实例
    stats = GameStats(ai_settings)

    #创建一个按钮
    play_button = Button(ai_settings, screen, 'Play')

    # 创建游戏得分实例
    scoreboard = Scoreboard(ai_settings, screen, stats)


    # 开始游戏的主循环
    while True:
        gf.check_events(ai_settings, screen, stats, scoreboard, play_button, ship, aliens, bullets)

        if stats.game_active:
            ship.update()
            gf.update_bullets(ai_settings, screen, stats, scoreboard, ship, aliens, bullets)
            gf.update_aliens(ai_settings, screen, stats, scoreboard, ship, aliens, bullets)

        gf.update_screen(ai_settings, screen, stats, scoreboard, ship, aliens, bullets, play_button)


run_game()


'''
bug改进
<1>在游戏非活动状态时，飞船仍可以发射子弹
<2>按Play键，再次游戏，得分没有立马更新 -- 检测按钮Play时更新
<3>玩家生命数量的问题
'''

