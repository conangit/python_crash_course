
alien_0 = {'color': 'green', 'point': 5}

print(alien_0)
print(alien_0['color'])
print(alien_0['point'])

alien_0['x_position'] = 0
alien_0['y_position'] = 25

print(alien_0)

alien_0 = {'x_position': 0, 'y_position': 25, "speed": 'medium'}
print(alien_0)

# alien_0['speed'] = 'slow'
alien_0['speed'] = 'high'

if alien_0['speed'] == 'slow':
    x_increment = 1
elif alien_0['speed'] == 'medium':
    x_increment = 2
else:
    x_increment = 3

alien_0['x_position'] = alien_0['x_position'] + x_increment
print(alien_0)

print('*' * 80)
alien_0 = {'x_position': 0, 'y_position': 25, "speed": 'medium'}
print(alien_0)

del alien_0['speed']
print(alien_0)

print('*' * 80)
favorite_languages = {
    'yaya': 'Java',
    'lihong': 'Python',
    'qiuping': 'C',
    'gougou': 'C',
}

print("Lihong's favorite language is " + favorite_languages['lihong'] + '.')

print('*' * 80)
for name, language in favorite_languages.items():
    print(name.title() + "'s favorite language is " + language + '.')


print('*' * 80)
for name in favorite_languages.keys():
    print(name)

# 默认遍历字典的所有键
print('*' * 80)
for k in favorite_languages:
    print(k)

print('*' * 80)
print(favorite_languages.items())
print(favorite_languages.keys())
print(favorite_languages.values())

print('*' * 80)
for name in sorted(favorite_languages.keys()):
    print(name.title())

print('*' * 80)
for language in favorite_languages.values():
    print(language)

# 方法set()作用于列表
print('*' * 80)
for language in set(favorite_languages.values()):
    print(language)