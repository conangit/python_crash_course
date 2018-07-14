

users = {
    'lihong': {
        'first': 'li',
        'last': 'hong',
        'age': 26,
    },

    'qiuping': {
        'first': 'wen',
        'last': 'ping',
        'age': 24,
    },
}

for username, user_info in users.items():
    print('Username: ' + username.title())
    full_name = user_info['first'] + ' ' + user_info['last']
    age = user_info['age']
    print('\tFull name: ' + full_name)
    print('\tage: ' + str(age))