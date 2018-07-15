

pets = ['cat', 'cat', 'cat', 'cat', 'dog', 'pig', 'cat']
print(pets)

# pets.remove('cat')
# print(pets)


# 我的实现1 错误
'''
pets_len = len(pets)
i = 0

while i < pets_len:
    if pets[i] == 'cat':
        del pets[i]
    i += 1

print(pets)
'''

# 列表在动态变化 pets[i]超出索引

# 我的实现2
'''
r_indexs = []
pets_len = len(pets)
i = 0

while i < pets_len:
    if pets[i] == 'cat':
        r_indexs.append(i)
    i += 1

# print(r_indexs)
for r_index in r_indexs:
    pets.pop(r_index)

print(pets)
'''

# 再次失败 列表是动态变化的 pets.pop(r_index)超出范围

i = len(pets)

while i >= 0:
    i -= 1
    if pets[i] == 'cat':
        pets.pop(i)

print(pets)


pets = ['cat', 'cat', 'cat', 'cat', 'dog', 'pig', 'cat']

while 'cat' in pets:
    pets.remove('cat')

print(pets)