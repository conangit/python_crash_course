
responses = {}

polling_active = True

while polling_active:
    name = input("\nWhat's your name? ")
    response = input('Which mountian would you like to climb someday? ')

    responses[name] = response

    repeat = input('Would you loke to let another person respond? (yes/no)')
    if repeat == 'no':
        polling_active = False

for name, mountian in responses.items():
    print('name: ' + name.title() + ', would like to climb ' + mountian + '.')