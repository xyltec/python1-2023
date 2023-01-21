w = [4, 1, 2, 3, 1, 1, 3, 2]

# jak dostać unikalne elementy listy 'w'

s = set()
for x in w:
    s.add(x)

print(s)
print(5 in s)
print(4 in s)
print(4 in w)  # bardzo wolna

s.remove(4)
print(s)
print(len(s))
