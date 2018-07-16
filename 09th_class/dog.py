


class Dog():
    '''
    一次模拟小狗的简单尝试
    '''

    def __init__(self, name, age):
        '''
        初始化属性name和age
        '''
        self.name = name
        self.age = age

    def sit(self):
        '''
        模拟小狗被命令时蹲下
        '''
        print(self.name.title() + ' is now sitting.')

    def roll_over(self):
        '''
        模拟小狗被明令时打滚
        '''
        print(self.name.title() + ' rolled over!')


my_dog = Dog('erha', 5)
print(my_dog)
print('My dog name is ' + my_dog.name.title() + '.')
print('My dog age is ' + str(my_dog.age) + '.')
my_dog.sit()
my_dog.roll_over()

print('*' * 80)

yaya_dog = Dog('yaya', 3)
print(yaya_dog)
print('My dog name is ' + yaya_dog.name.title() + '.')
print('My dog age is ' + str(yaya_dog.age) + '.')
yaya_dog.sit()
yaya_dog.roll_over()