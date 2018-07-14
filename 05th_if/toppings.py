
requested_topping = 'mushrooms'

if (requested_topping != 'anch'):
    print('Hold the anch')


age_0 = 22
age_1 = 18
print((age_0 >= 21) and (age_1 >= 21))
print((age_0 >= 21) or (age_1 >= 21))



requested_toppings = ['apple', 'banana', 'orange']
print('lihong' in requested_toppings)
print('apple' in requested_toppings)

print('lihong' not in requested_toppings)
print('apple' not in requested_toppings)


requested_toppings = ['apple', 'banana', 'orange']

if 'apple' in requested_toppings:
    print('Addding apple')
if 'grape' in requested_toppings:
    print('Addding grape')
if 'orange' in requested_toppings:
    print('Addding orange')


for requested_topping in requested_toppings:
    if requested_topping == 'banana':
        print('Sorry, we have no banana!')
    else:
        print('Adding ' + requested_topping + '.')

requested_toppings = []

if requested_toppings:
    for requested_topping in requested_toppings:
        print('Adding ' + requested_topping + ' ...')
    print('Finished making pizza!')
else:
    print('Are you sure you want a plain pizza?')


available_toppings = ['apple', 'banana', 'grape']
requested_toppings = ['apple', 'banana', 'grape', 'orange']

for requested_topping in requested_toppings:
    if requested_topping in available_toppings:
        print('Adding ' + requested_topping + ' ...')
    else:
        print("We don't bave " + requested_topping + ' !')
