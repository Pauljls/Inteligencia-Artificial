lista = []
for i in range(4):
    aux = int(input("Ingrese un numero: "))
    lista.append(aux)

for x in range(4):
    if lista[x] % 2 == 1:
        print("el numero es impar")
    else:
        print("El nuemro es par")
