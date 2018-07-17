

from name_function import get_formatted_name

print("Enter 'q' to quit at a any time.")
while True:
    first = input('\nPlease input your first name: ')
    if first == 'q':
        break
    last = input('\nPlease input your last name: ')
    if last == 'q':
        break
    formated_name = get_formatted_name(first, last)
    print(formated_name)