
import json

filename = 'numbers.json'

try:
    with open(filename) as f_obj:
        numbers = json.load(f_obj)
except FileNotFoundError:
    print('No such file or directory')
else:
    print(numbers)

# 依然为数字列表
# print(numbers[0] + numbers[1])

