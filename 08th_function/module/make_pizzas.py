

import pizza
pizza.make_pizza('apple')
pizza.make_pizza_2(30, 'banana', 'grape')


print('*' * 80)

from pizza import make_pizza, make_pizza_2
make_pizza('apple')
make_pizza_2(30, 'banana', 'grape')

print('*' * 80)

import pizza as p
p.make_pizza('apple')
p.make_pizza_2(30, 'banana', 'grape')


print('*' * 80)

from pizza import make_pizza as mp
mp('apple', 'grape')

# 不推荐的方式
# from pizza import *
