
import sys

import pygame

from bullet import Bullet
from alien import Alien



def fire_bullet(ai_settings, screen, ship, bullets):
    '''发射一颗子弹'''
    # 创建一颗子弹 并将其加入到编组bullets中
    if len(bullets) < ai_settings.bullets_allowed:
        new_bullet = Bullet(ai_settings, screen, ship)
        bullets.add(new_bullet)


def check_keydown_events(event, ai_settings, screen, ship, bullets):
    '''响应按键按下'''
    if event.key == pygame.K_RIGHT:
        ship.moving_right = True
    elif event.key == pygame.K_LEFT:
        ship.moving_left = True
    elif event.key == pygame.K_SPACE:
        fire_bullet(ai_settings, screen, ship, bullets)
    elif event.key == pygame.K_q:
        sys.exit()


def check_keyup_events(event, ship):
    '''响应按键松开'''
    if event.key == pygame.K_RIGHT:
        # 停止飞船向右移动
        ship.moving_right = False
    elif event.key == pygame.K_LEFT:
        ship.moving_left = False


def check_events(ai_settings, screen, ship, bullets):
    '''监视键盘和鼠标事件'''
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
        elif event.type == pygame.KEYDOWN:
            check_keydown_events(event, ai_settings, screen, ship, bullets)
        elif event.type == pygame.KEYUP:
            check_keyup_events(event, ship)


def update_bullets(bullets):
    '''更新子弹位置，并删除消失的子弹'''
    # 更新子弹位置
    # 对编组调用update()时，编组将对其中的每个精灵调用update()，即bullet.update()
    bullets.update()

    # 删除已消失的子弹
    for bullet in bullets.copy():
        if bullet.rect.bottom <= 0:
            bullets.remove(bullet)
    # print(len(bullets))


def get_number_aliens_x(ai_settings, alien_width):
    '''计算每行可容纳多少外星人'''
    available_space_x = ai_settings.screen_width - 2 * alien_width
    number_aliens_x = int(available_space_x / (2 * alien_width))
    return number_aliens_x


def creat_alien(ai_settings, screen, aliens, alien_number):
    '''创建一个外星人'''
    alien = Alien(ai_settings, screen)
    alien_width = alien.rect.width
    alien.x = alien_width + 2 * alien_width * alien_number
    alien.rect.x = alien.x
    aliens.add(alien)


def create_fleet(ai_settings, screen, aliens):
    '''创建外星人群'''
    alien = Alien(ai_settings, screen)
    alien_width = alien.rect.width
    number_aliens_x = get_number_aliens_x(ai_settings, alien_width)
    for alien_number in range(number_aliens_x):
        creat_alien(ai_settings, screen, aliens, alien_number)

    # 创建一行外星人
    for alien_number in range(number_aliens_x):

        alien.x = alien_width + 2 * alien_width * alien_number
        alien.rect.x = alien.x
        aliens.add(alien)


def update_screen(ai_settings, screen, ship, aliens, bullets):
    '''更新屏幕上的图像,并切换到新屏幕'''
    # 设备背景颜色
    screen.fill(ai_settings.bg_color)

    # 绘制子弹
    for bullet in bullets.sprites():
        bullet.draw_bullet()

    # 描绘飞船
    ship.blitme()

    # 描绘外星人群
    # 对编组调用draw()时，Pygame自动绘制编组里面的每个元素
    # 绘制位置由元素的rect决定
    aliens.draw(screen)

    # 最近绘制的屏幕可见
    pygame.display.flip()



