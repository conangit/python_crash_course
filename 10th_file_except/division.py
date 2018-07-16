
try:
    print(5 / 0)
except ZeroDivisionError:
    print('You can not divide by zero!')


print('Give me two numbers, and I will divide them')
print("Enter 'q' to quit.")

while True:
    first_number = input('\nFirst number: ')
    if first_number == 'q':
        break
    second_number = input('\nSecond number: ')
    if second_number == 'q':
        break
    try:
        # 可能引起异常的代码块
        answer = int(first_number) / int(second_number)
    except ZeroDivisionError:
        print('You can not divide by zero!')
    else:
        # try代码块执行成功后运行的代码块
        print(answer)