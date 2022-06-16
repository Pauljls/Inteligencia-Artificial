
while(True):
    num = int(input("Ingrese un numero cualquiera: "))
    if(num > 0):
        break


for i in range(1, num+1):
    if num % i == 0:
        print(i)
