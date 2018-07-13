
# <2.3.1>
name = 'ada lovelace'
print(name.title())
print(name.upper())
print(name.lower())

# <2.3.2> 字符串拼接
fist_nmae = 'ada'
last_name = 'lovelace'
full_name = fist_nmae + ' ' + last_name
print(full_name)
print('Hello, ' + full_name.title() + '!')

message = 'Hello, ' + full_name.title() + '!'
print(message)

print('Python')
print('\tPython')

print('Languages:\nPython\nC\nJavaScript')
print('Languages:\n\tPython\n\tC\n\tJavaScrip')

favorite_language = 'python '
print(favorite_language)
favorite_language.rstrip()
print(favorite_language.rstrip())
# 暂时性地删除
print(favorite_language)

# 将作用地结果存回变量
favorite_language = favorite_language.rstrip()
print(favorite_language)

favorite_language = '  My love  '
print(favorite_language.rstrip())
print(favorite_language.lstrip())
print(favorite_language.strip())
