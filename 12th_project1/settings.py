
class Settings():
    '''存储游戏的所有设置选项'''
    
    def __init__(self):
        '''初始化游戏的静态设置'''
        # 屏幕设置
        self.screen_width = 750
        self.screen_height = 500
        # self.screen_width = 900
        # self.screen_height = 600
        self.bg_color = (230, 230, 230)

        # 飞船设置
        # 可失误3次 相当于有4条命
        self.ship_limit = 3

        # 子弹设置
        self.bullet_width = 3
        # self.bullet_width = self.screen_width
        self.bullet_height = 15
        # self.bullet_color = (60, 60, 60)
        self.bullet_color = (255, 0, 0)

        # 外星人设置
        # fleet_direction为1表示右移 -1表示左移
        self.fleet_direction = 1

        # 游戏难度增加设置 同时提高杀死外星人得分点数
        self.speedup_scale = 1.1
        self.score_scale = 1.5

        # 游戏动态设置
        self.init_dynamic_settings()

    def init_dynamic_settings(self):
        '''游戏动态设置'''
        self.ship_speed_factor = 0.5
        self.bullet_speed_factor = 1.0
        self.alien_speed_factor = 0.5
        
        self.fleet_drop_speed = 100
        self.bullets_allowed = 3

        self.alien_points = 10

    def increase_speed(self):
        '''加速设置'''
        # self.ship_speed_factor *= self.speedup_scale
        
        self.alien_speed_factor *= self.speedup_scale

        if self.bullet_speed_factor < 3:
            self.bullet_speed_factor *= self.speedup_scale

        self.fleet_drop_speed *= self.speedup_scale
        self.bullets_allowed = int(self.bullets_allowed * (self.speedup_scale ** 30))

        self.alien_points = int(self.alien_points * self.score_scale)


