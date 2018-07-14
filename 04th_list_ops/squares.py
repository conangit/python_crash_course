
squares = []

for value in range(1, 11):
    square = value ** 2
    squares.append(square)

print(squares)

squares = []

for value in range(1, 11):
    squares.append(value ** 3)

print(squares)


# python的强大之处
digits = list(range(1, 10000001))
# print(digits)
print(min(digits))
print(max(digits))
print(sum(digits))

squares = [value ** 2 for value in range(1, 11)]
print(squares)

