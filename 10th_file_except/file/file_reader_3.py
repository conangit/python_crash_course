
file_path = r'D:\Program\Python\python_crash_course\10th_file\pi_digits.txt'

with open(file_path) as file_object:
    lines = file_object.readlines()

print(lines)

pi_string = ''

for line in lines:
    pi_string += line.strip()

print(len(pi_string))
print(pi_string[:17])

# 保留15位小数
pi_float = float(pi_string)
print(pi_float)