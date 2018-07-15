

def make_pizza(*toppings):
    '''
    打印顾客点的所有配料
    '''
    print('\nMaking a pizza with the following topppings:')
    for topping in toppings:
        print('- ' + topping)


# make_pizza('apple')
# make_pizza('apple', 'orange', 'banana')


def make_pizza_2(size, *toppings):
    '''
    概述要制作的pizza
    '''
    print('\nMaking a ' + str(size) + '-inch piaaz with the following toppings:')
    for topping in toppings:
        print('- ' + topping)


# make_pizza_2(24, 'apple')
# make_pizza_2(30, 'apple', 'orange', 'grape')
