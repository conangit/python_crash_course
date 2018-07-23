
import sys
from time import sleep

import pygame

from bullet import Bullet
from alien import Alien



def fire_bullet(ai_settings, screen, stats, ship, bullets):
    '''发射一颗子弹'''
    # 创建一颗子弹 并将其加入到编组bullets中
    # 游戏活动才可以发射子弹
    if stats.game_active and len(bullets) < ai_settings.bullets_allowed:
        new_bullet = Bullet(ai_settings, screen, ship)
        bullets.add(new_bullet)


def check_keydown_events(event, ai_settings, screen, stats, ship, bullets):
    '''响应按键按下'''
    if event.key == pygame.K_q:
        sys.exit()
    elif event.key == pygame.K_RIGHT:
        ship.moving_right = True
    elif event.key == pygame.K_LEFT:
        ship.moving_left = True
    elif event.key == pygame.K_SPACE:
        fire_bullet(ai_settings, screen, stats, ship, bullets)


def check_keyup_events(event, ship):
    '''响应按键松开'''
    if event.key == pygame.K_RIGHT:
        # 停止飞船向右移动
        ship.moving_right = False
    elif event.key == pygame.K_LEFT:
        ship.moving_left = False


def check_events(ai_settings, screen, stats, scoreboard, play_button, ship, aliens, bullets):
    '''监视键盘和鼠标事件'''
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
        elif event.type == pygame.KEYDOWN:
            check_keydown_events(event, ai_settings, screen, stats, ship, bullets)
        elif event.type == pygame.KEYUP:
            check_keyup_events(event, ship)
        elif event.type == pygame.MOUSEBUTTONDOWN:
            mouse_x, mouse_y = pygame.mouse.get_pos()
            ckeck_play_button(ai_settings, screen, stats, scoreboard, play_button, ship, aliens, bullets, mouse_x, mouse_y)


def ckeck_play_button(ai_settings, screen, stats, scoreboard, play_button, ship, aliens, bullets, mouse_x, mouse_y):
    '''单击Play按钮时重置整个游戏'''
    button_clicked = play_button.rect.collidepoint(mouse_x, mouse_y)
    if button_clicked and not stats.game_active:
        # 隐藏光标
        pygame.mouse.set_visible(False)
        # 游戏难度回归
        ai_settings.init_dynamic_settings()
        # 重置游戏统计信息 (注意此时并没有将信息更新到屏幕)
        stats.reset_stats()
        stats.game_active = True
        # 更新得分显示信息
        scoreboard.prep_score()
        scoreboard.prep_high_score()
        scoreboard.prep_level()
        scoreboard.prep_ships()

        aliens.empty()
        bullets.empty()
        create_fleet(ai_settings, screen, ship, aliens)
        ship.center_ship()


def get_number_aliens_x(ai_settings, alien_width):
    '''计算每行可容纳多少外星人'''
    available_space_x = ai_settings.screen_width - 2 * alien_width
    number_aliens_x = int(available_space_x / (2 * alien_width))
    return number_aliens_x


def get_number_rows(ai_settings, ship_height, alien_height):
    '''计算屏幕可容纳多少行外星人'''
    available_space_y = ai_settings.screen_height - 3 * alien_height - ship_height
    number_rows = int(available_space_y / (2 * alien_height))
    return number_rows


def creat_alien(ai_settings, screen, aliens, alien_number, row_number):
    '''创建一个外星人'''
    alien = Alien(ai_settings, screen)

    alien_width = alien.rect.width
    alien_height = alien.rect.height

    alien.x = alien_width + 2 * alien_width * alien_number
    alien.rect.x = alien.x
    alien.rect.y = alien_height + 2 * alien_height * row_number

    aliens.add(alien)


def create_fleet(ai_settings, screen, ship, aliens):
    '''创建外星人群'''
    alien = Alien(ai_settings, screen)

    alien_width = alien.rect.width
    alien_height = alien.rect.height
    ship_height = ship.rect.height

    number_aliens_x = get_number_aliens_x(ai_settings, alien_width)
    number_rows = get_number_rows(ai_settings, ship_height, alien_height)

    # 创建外星人群
    for row_number in range(number_rows):
        for alien_number in range(number_aliens_x):
            creat_alien(ai_settings, screen, aliens, alien_number, row_number)


def change_fleet_direction(ai_settings, aliens):
    '''将整群外星人下移，并改变移动方向'''
    for alien in aliens.sprites():
        alien.rect.y += ai_settings.fleet_drop_speed
    ai_settings.fleet_direction *= -1


def check_fleet_edges(ai_settings, aliens):
    '''由外星人到达边缘时采取的措施'''
    for alien in aliens.sprites():
        if alien.check_edges():
            change_fleet_direction(ai_settings, aliens)
            break


def check_alien_collisions(ai_settings, screen, stats, scoreboard, ship, aliens, bullets):
    # 检测子弹是否击中外星人
    # 第一个True表示碰撞后bullet是否消失
    # 第二个True表示碰撞后alien是否消失
    # #返回值为一个字典 key:bullet value:alien
    collisions = pygame.sprite.groupcollide(bullets, aliens, True, True)

    # 统计游戏分数
    if collisions:
        for alien in collisions.values():
            stats.score += ai_settings.alien_points
            scoreboard.prep_score()
        check_high_score(stats, scoreboard)

    if len(aliens) == 0:
        # 删除现有的所有子弹
        bullets.empty()
        # 增加游戏难度
        ai_settings.increase_speed()
        # 提高玩家等级
        stats.level += 1
        scoreboard.prep_level()
        # 并产生新的一群外星人
        create_fleet(ai_settings, screen, ship, aliens)


def check_aliens_bottom(ai_settings, screen, stats, scoreboard, ship, aliens, bullets):
    '''检测是否有外星人到达底部'''
    screen_rect = screen.get_rect()
    for alien in aliens.sprites():
        if alien.rect.bottom >= screen_rect.bottom:
            # 效果等同于飞船撞击
            ship_hit(ai_settings, screen, stats, scoreboard, ship, aliens, bullets)
            break


def update_bullets(ai_settings, screen, stats, scoreboard, ship, aliens, bullets):
    '''更新子弹位置，并删除消失的子弹'''
    # 更新子弹位置
    # 对编组调用update()时，编组将对其中的每个精灵调用update()，即bullet.update()
    bullets.update()

    # 删除已消失的子弹
    for bullet in bullets.copy():
        if bullet.rect.bottom <= 0:
            bullets.remove(bullet)
    # print(len(bullets))
    
    check_alien_collisions(ai_settings, screen, stats, scoreboard, ship, aliens, bullets)


def ship_hit(ai_settings, screen, stats, scoreboard, ship, aliens, bullets):
    '''响应外星人撞击飞船'''
    if stats.ships_left > 0:
        stats.ships_left -= 1

        #更新玩家剩余飞船
        scoreboard.prep_ships()

        aliens.empty()
        bullets.empty()

        create_fleet(ai_settings, screen, ship, aliens)
        ship.center_ship()

        # 游戏暂停1秒
        sleep(1)
    else:
        stats.game_active = False
        # 显示光标 以便单击开始
        pygame.mouse.set_visible(True)


def check_high_score(stats, scoreboard):
    '''检测是否诞生了最高分'''
    if stats.score > stats.high_score:
        stats.high_score = stats.score
        scoreboard.prep_high_score()


def update_aliens(ai_settings, screen, stats, scoreboard, ship, aliens, bullets):
    '''更新外新人群中的所有外星人位置'''
    check_fleet_edges(ai_settings, aliens)
    aliens.update()

    # 外星人与飞船撞击检测
    if pygame.sprite.spritecollideany(ship, aliens):
        # print('Shit hit!!!')
        ship_hit(ai_settings, screen, stats, scoreboard, ship, aliens, bullets)

    # 外星到达底部
    check_aliens_bottom(ai_settings, screen, stats, scoreboard, ship, aliens, bullets)


def update_screen(ai_settings, screen, stats, scoreboard, ship, aliens, bullets, play_button):
    '''更新屏幕上的图像,并切换到新屏幕'''
    # 设备背景颜色
    screen.fill(ai_settings.bg_color)

    # 描绘飞船
    ship.blitme()

    # 绘制子弹
    for bullet in bullets.sprites():
        bullet.draw_bullet()

    # 描绘外星人群
    # 对编组调用draw()时，Pygame自动绘制编组里面的每个元素
    # 绘制位置由元素的rect决定
    aliens.draw(screen)

    # 显示得分
    scoreboard.show_score()

    # 如果游戏处于非活动状态就绘制play按钮
    if not stats.game_active:
        play_button.draw_button()

    # 最近绘制的屏幕可见
    pygame.display.flip()

