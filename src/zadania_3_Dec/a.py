from random import randint

w = [randint(0, 10**6) for _ in range(8 * 10**4)]

s = set(w)

counter = 0
for g in range(8 * 10**4):
    x = randint(0, 10**6)
    if x in s:
        counter += 1

print(counter)
