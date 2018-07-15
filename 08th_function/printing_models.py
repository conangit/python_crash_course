

unprinted_designs = ['iphone case', 'rebot pendant', 'dodecahedron']
completed_models = []

while unprinted_designs:
    current_design = unprinted_designs.pop()

    print('Printing model: ' + current_design + ' ...')
    completed_models.append(current_design)

print(completed_models)


print('*' * 80)

unprinted_designs = ['iphone case', 'rebot pendant', 'dodecahedron']
completed_models = []

def print_modules(unprinted_designs, completed_models):
    while unprinted_designs:
        current_design = unprinted_designs.pop()

        print('Printing model: ' + current_design + ' ...')
        completed_models.append(current_design)

def show_modules(completed_models):
    for completed_model in completed_models:
        print(completed_model)


# 列表已被修改
'''
print_modules(unprinted_designs, completed_models)
show_modules(completed_models)

print(unprinted_designs)
print(completed_models)
'''

# 传入副本 不改变列表
print_modules(unprinted_designs[:], completed_models)
show_modules(completed_models)

print(unprinted_designs)
print(completed_models)