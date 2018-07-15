
pormpt = 'Please enter the name of a city you have visited.'
pormpt += "\nEnter 'quit' when you are finished.\n"

cities = []

while True:
    message = input(pormpt)

    if (message == 'quit'):
        break;
    else:
        cities.append(message)

if cities:
    for city in cities:
        print(city.title())
else:
    print('you input null.')
