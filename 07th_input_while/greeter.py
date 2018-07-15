
pormpt = 'If you tell us who you are, we can presonalize the message you see.'
pormpt += "\nWhat's your name? " 

# 将输入解析为字符串
message = input(pormpt)
print('\nHello, ' + message + '!\n')

print('*' * 80)

age = input('How old are you? ')
# age = int(age)
if (age >= 18):
    print('You are a adult.')