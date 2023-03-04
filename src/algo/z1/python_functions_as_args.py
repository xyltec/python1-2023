def sqare(x):
    return x * x


def cube(x):
    return x ** 3


def calculator(operation, argument):
    return operation(argument)


print(sqare(4))
print(cube(4))

print('-----------')

print(calculator(sqare, 5))
print(calculator(cube, 5))
print(calculator(print, 5))