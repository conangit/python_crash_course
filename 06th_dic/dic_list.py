
pizza  = {
    'crust': 'thick',
    'toppings': ['apple', 'banana', 'grape'],
}

print('you ordered a ' + pizza['crust'] + '-crust pizza ' + 'with the following toppings:')
for topping in set(pizza['toppings']):
    print('\t' + topping)

print('*' * 80)

favorite_languages = {
    'lihong': ['C', 'C++', 'Python'],
    'yaya': ['Java'],
    'ping': ['JavaSript', 'Python', 'C#'],
}

for name, languages in favorite_languages.items():
    print(name.title() +"'s favorite language are:")
    for language in languages:
        print('\t' + language)