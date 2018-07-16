

# 关键字with在不需要访问文件后将其关闭
with open('pi_digits.txt') as file_object:
    contents = file_object.read()
    print(contents)


with open('pi_digits.txt') as file_object:
    contents = file_object.read()
    print(contents.rstrip())

with open('pi_digits.txt') as file_object:
    contents = file_object.read()
    print(contents.lstrip())

with open('pi_digits.txt') as file_object:
    contents = file_object.read()
    print(contents.strip())


file_path = r'D:\Program\Python\python_crash_course\10th_file\pi_digits.txt'

with open(file_path) as file_object:
    contents = file_object.read()
    print(contents)

    

