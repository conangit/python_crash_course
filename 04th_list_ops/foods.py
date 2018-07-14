
my_foods = ['pizza', 'falafel', 'carrot cake']
friend_foods = my_foods[:]
print(my_foods)
print(friend_foods)

my_foods.append('apple')
friend_foods.append('banana')
print(my_foods)
print(friend_foods)

my_foods = ['pizza', 'falafel', 'carrot cake']
friend_foods = my_foods
my_foods.append('apple')
print(my_foods)
print(friend_foods)
