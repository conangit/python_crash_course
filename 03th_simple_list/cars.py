
# sort()对列表永久性的修改排序
cars = ['bwm', 'audi', 'toyota', 'subaru']
cars.sort()
print(cars)

cars = ['bwm', 'audi', 'toyota', 'subaru']
cars.sort(reverse=True)
print(cars)

# 对列表进行临时排序
cars = ['bwm', 'audi', 'toyota', 'subaru']
print('Here is the origianl list:')
print(cars)
print('Here is the sorted list:')
print(sorted(cars))
print('Here is the origianl list again:')
print(cars)

print(sorted(cars, reverse=True))

print()
cars = ['bwm', 'audi', 'toyota', 'subaru']
print(cars)
# 反转列表 永久性修改
cars.reverse()
print(cars)

print(len(cars))


