list = [8, 10, 14, 7, 2]

for i in range(5):
    for j in range(5):
        if list[i] > list[j]:
            aux = list[i]
            list[i] = list[j]
            list[j] = aux

print(list)
