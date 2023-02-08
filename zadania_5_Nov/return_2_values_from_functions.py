def max_min_x(a: int, b: int, c: int):
    mi = min(a, b, c)
    mx = max(a, b, c)
    return mi, mx


print(max_min_x(1, 2, 3))


MI, MX = max_min_x(1, 2, 3)
print(MI)
print(MX)
