list = []
sort = []
while(True):
    resp = int(input("Desea ingresar numeros, digite uno si es asi: \n"))
    if (resp == 1):
        num = int(input("Ingrese un valor: "))
        list.append(num)
    else:
        break
for i in list:
    if (i % 2 == 0):
        sort.append(i)


print(sort)
