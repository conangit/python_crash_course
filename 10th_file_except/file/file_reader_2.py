
file_path = r'D:\Program\Python\python_crash_course\10th_file\pi_digits.txt'

with open(file_path) as file_object:
    for line in file_object:
        print(line)

with open(file_path) as file_object:
    for line in file_object:
        print(line.rstrip())

print('*' * 80)

with open(file_path) as file_object:
    lines = file_object.readlines()

print(lines)

for line in lines:
    print(line.rstrip())
