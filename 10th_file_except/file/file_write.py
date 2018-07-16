

file_path = 'programming.txt'

with open(file_path, 'w') as file_object:
    file_object.write('I love Python\n')
    file_object.write('Lihong is a good man\n')

# with open(file_path, 'w') as file_object:
with open(file_path, 'a') as file_object:
    file_object.write('You are a beautiful girl\n')