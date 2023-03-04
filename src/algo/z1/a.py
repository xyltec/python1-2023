def f(x):
    return x ** 2


def exec(fn, x):
    return fn(x)


print(exec(f, 10))

w = ((1, 0), (0, 1))

g = sorted(w, key=lambda x: x[1])
print(g)
