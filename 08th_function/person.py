

def build_person(first_name, last_name):
    '''
    返回一个字典，其中包含一个人的信息
    '''
    person = {'first': first_name.title(), 'last': last_name.title()}

    return person

me = build_person('li', 'hong')
print(me)


def build_person_2(first_name, last_name, age=''):
    '''
    返回一个字典，其中包含一个人的信息
    '''
    person = {'first': first_name.title(), 'last': last_name.title()}
    if age:
        person['age'] = age

    return person

me = build_person_2('li', 'hong')
print(me)

me = build_person_2('li', 'hong', age='27')
me = build_person_2('li', 'hong', age=27)
print(me)