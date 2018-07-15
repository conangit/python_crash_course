
def describe_pet(animal_type, pet_name):
    '''
    显示宠物信息
    '''
    print('\nI have a ' + animal_type + '.')
    print('My ' + animal_type + "'s name is " + pet_name + '.')

describe_pet('hamster', 'harry')
describe_pet('cat', 'meimei')



describe_pet(pet_name='qiu', animal_type='dog')

print('*' * 80)

def describe_pet_2(pet_name, animal_type='dog'):
    '''
    显示宠物信息
    '''
    print('\nI have a ' + animal_type + '.')
    print('My ' + animal_type + "'s name is " + pet_name + '.')

describe_pet_2('erha')
describe_pet_2('erha', 'dog')
describe_pet_2(pet_name='erha')
describe_pet_2(animal_type= 'dog', pet_name='erha')

