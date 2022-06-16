list = []
while True:
    val = int(input("Ingrese un valor: "))
    list.append(val)
    if val == 0:
        break

a = 0

for i in range(len(list)):
    a = a+list[i]

print(f'El valor de la suma de todos los elementos de la lsita es: {a}')
