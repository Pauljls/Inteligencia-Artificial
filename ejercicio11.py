list = []
sum = 0
while(True):
    num = (int(input("Igrese el numero que desea sumar: ")))
    sum = sum+num
    list.append(num)
    if(sum > 100):
        break

print(
    f'La suma final de los elementos es {sum} su promedio es {sum/len(list)}')
