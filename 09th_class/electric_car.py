
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
        self.gas_capacity = 100

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
        if miles > 0:
            self.odometer += miles


    def get_gas_capacity(self):
        '''
        获取油箱容量信息
        '''
        print('This car has a ' + str(self.gas_capacity) + '-L gas capicaty.')



class Battery():
    '''
    描述电动车电瓶
    '''
    def __init__(self, battery_size=70):
        '''
        初始化电瓶信息
        '''
        self.battery_size = battery_size

    def describe_battery(self):
        '''
        打印一条描述电瓶容量的的信息
        '''
        print('This car has a ' + str(self.battery_size) + '-kWh battery.')

    def get_range(self):
        '''
        指出电瓶续航里程
        '''
        if self.battery_size <= 70:
            car_range = 240
        elif self.battery_size <= 95:
            car_range = 400
        else:
            car_range = 600

        print('This car can go approximately ' + str(car_range) + ' miles on full charge.')


class ElectricCar(Car):
    '''
    电动汽车的独特之处
    '''
    def __init__(self, make, model, year):
        '''
        初始化父类的属性
        '''
        super().__init__(make, model, year)
        # self.battery = Battery()
        self.battery = Battery(95)

    def get_gas_capacity(self):
        '''
        重写父类方法
        电动汽车没有油箱
        '''
        print("Electric car don't have a gas capicaty!")



my_tesla = ElectricCar('tesla', 'model s', 2017)
print(my_tesla.get_descriptive_name())
my_tesla.get_gas_capacity()
# print(my_tesla.battery)
my_tesla.battery.describe_battery()
my_tesla.battery.get_range()
