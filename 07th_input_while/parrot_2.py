
pormpt = 'If you tell us who you are, we can presonalize the message you see.'
pormpt += "\nEnter 'quit' to end the program. \n"

'''
message = ''

while message != 'quit':
    message = input(pormpt)
    if message != 'quit':
        print('Hello, ' + message + '!\n')
'''

active = True

while active:
    message = input(pormpt)

    if (message == 'quit'):
        active = False
    else:
        print('Hello, ' + message + '.\n')



