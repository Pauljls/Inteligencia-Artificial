num = int(input("Ingrese la cantidad de numeros que va digitar: "))
list = [float(input("Ingrese un numero: ")) for i in range(num)]
print(list)
a = 0
for x in range(num):
    a = a+list[x]
a = a/num
print(f'el promedio de los numeros ingresados es: {a} ')
