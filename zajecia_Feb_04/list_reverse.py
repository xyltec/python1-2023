w = [2, 4, 8, 10]
w_obrocona = []  # 10, 8, 4, 2

for e in w:
    w_obrocona = [e] + w_obrocona

# print(w_obrocona)

print(w[::-1])

# print(w[0:4:2])
# print(w[10:0:-1])  # w[a:b:c]
