num = int(input("Ingrese la cantidad de numeros que va digitar: "))
list = []
for i in range(num):
    list.append(int(input("Ingrese un numero: ")))
    if list[i] % 2 == 0:
        print(f'el numero {list[i]} es par')
    else:
        print(f'el numero {list[i]} no es par')
print(list)
