
class Car():
    '''
    一次模拟汽车的简单尝试
    '''

    def __init__(self, make, model, year):
        '''
        初始化描述汽车的属性
        '''
        self.make = make
        self.model = model
        self.year = year
        # 类的每个属性都必须有初始值
        self.odometer = 0

    def get_descriptive_name(self):
        '''
        返回整洁的描述信息
        '''
        long_name = str(self.year) + ' ' + self.make + ' ' + self.model
        return long_name.title()

    def read_odometer(self):
        '''
        打印一条汽车的里程信息
        '''
        print('This car has ' + str(self.odometer) + ' miles on it.')

    def update_odometer(self, miles):
        '''
        设置汽车里程值，并禁止回调
        '''
        if miles >= self.odometer:
            self.odometer = miles
        else:
            print("You cann't roll back an odometer")

    def increment_odometer(self, miles):
        '''
        将里程表增加指定值
        '''
        # 程序漏洞 可通过次方法 “回调”里程
        self.odometer += miles


my_car = Car('audi', 'a4', 2018)
print(my_car.get_descriptive_name())
my_car.read_odometer()

# 直接修改属性的值
my_car.odometer = 20
my_car.read_odometer()

# 通过方法修改属性值
# my_car.update_odometer(30)
my_car.update_odometer(10)
my_car.read_odometer()

my_car.increment_odometer(150)
my_car.read_odometer()

