
def get_formatted_name(first_name, last_name):
    '''
    帮助返回简洁的姓名
    '''
    full_name = first_name + ' ' + last_name
    return full_name.title()

name = get_formatted_name('li', 'hong')
print(name)

name = get_formatted_name('wen', 'qiuping')
print(name)



def get_formatted_name_2(first_name, last_name, middle_name=''):
    '''
    帮助返回简洁的姓名
    '''
    if middle_name:
        full_name = first_name + ' ' + middle_name + ' ' + last_name
    else:
        full_name = first_name + ' ' + last_name

    return full_name.title()

name = get_formatted_name_2('li', 'hong')
print(name)

name = get_formatted_name_2('Wen', 'ping', 'qiu')
print(name)

