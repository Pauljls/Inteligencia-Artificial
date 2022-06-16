list = []
while True:
    val = int(input("Ingrese un valor: "))
    list.append(val)
    if val == 0:
        break

for i in range(len(list)):
    for j in range(5):
        if list[i] > list[j]:
            aux = list[i]
            list[i] = list[j]
            list[j] = aux

print(list)
