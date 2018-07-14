
alien_0 = {
    'color': 'green',
    'points': 5,
}

alien_1 = {
    'color': 'yellow',
    'points': 10,
}

alien_2 = {
    'color': 'red',
    'points': 15,
}

aliens = [alien_0, alien_1, alien_2]
print(aliens)

for alien in aliens:
    print(alien)

print('*' * 80)
aliens = []

for alien_number in range(30):
    new_alien = {'color': 'red', 'points': 15, 'speed': 'slow'}
    new_alien['num'] = alien_number
    aliens.append(new_alien)

print(aliens)


