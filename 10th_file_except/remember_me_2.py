
import json


def get_stored_username():
    '''
    如果存储了用户名，就获取它
    '''
    filename = 'username.json'
    try:
        with open(filename) as f_obj:
            username = json.load(f_obj)
            return username
    except FileNotFoundError:
        return None

def get_new_username():
    '''
    提示用户输入用户名
    '''
    username = input("What's your name? ")
    filename = 'username.json'
    with open(filename, 'w') as f_obj:
        json.dump(username, f_obj)

    return username

def greet_user():
    '''
    问候用户，并指出其名字
    '''
    username = get_stored_username()
    if username:
        print('Welcome back, ' + username)
    else:
        username = get_new_username()
        print('We will remember you.')





greet_user()