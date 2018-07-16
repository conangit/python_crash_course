import json

filename = 'username.json'

try:
    with open(filename) as f_obj:
        username = json.load(f_obj)
except FileNotFoundError:
    print('No such file or directory')
else:
    print('Welcome back, ' + username)
