
motorcycles = ['handa', 'yamaha', 'suzuki']
print(motorcycles)

motorcycles[0] = 'ducati'
print(motorcycles)

motorcycles = ['handa', 'yamaha', 'suzuki']
motorcycles.append('duccati')
print(motorcycles)

motorcycles = []
motorcycles.append('handa')
motorcycles.append('yamaha')
motorcycles.append('suzuki')
print(motorcycles)

motorcycles = ['handa', 'yamaha', 'suzuki']
motorcycles.insert(0, 'ducati')
print(motorcycles)


motorcycles = ['handa', 'yamaha', 'suzuki']
print(motorcycles)
del motorcycles[0]
print(motorcycles)

motorcycles = ['handa', 'yamaha', 'suzuki']
print(motorcycles)
del motorcycles[1]
print(motorcycles)


motorcycles = ['handa', 'yamaha', 'suzuki']
print(motorcycles)
popped_motorcycle = motorcycles.pop()
print(motorcycles)
print(popped_motorcycle)

motorcycles = ['handa', 'yamaha', 'suzuki']
last_owner = motorcycles.pop()
print('The last motorcycle I owned was a ' + last_owner.title() + '.')

motorcycles = ['handa', 'yamaha', 'suzuki']
first_owner = motorcycles.pop(0)
print(motorcycles)
print('The first motorcycle I owned was a ' + first_owner.title() + '.')

motorcycles = ['handa', 'yamaha', 'suzuki']
motorcycles.remove('yamaha')
print(motorcycles)


motorcycles = ['handa', 'yamaha', 'suzuki', 'ducati']
print(motorcycles)
too_expensive = 'ducati'
motorcycles.remove(too_expensive)
print(motorcycles)
print('\nA ' + too_expensive.title() + ' is too expensive for me.')

# 出现3次yamaha
motorcycles = ['handa', 'yamaha', 'suzuki', 'ducati', 'yamaha', 'fenghuang', 'yamaha']
motorcycles.remove('yamaha')    # 只删除了第2个位置的yamaha
print(motorcycles)