x = []
y = []
sumx = 0
sumx2 = 0
sumy = 0
sumxy = 0
cap = int(input("Ingrese la cantidad de puntos para recta: "))
for x in range(cap):
    x = float(input("Ingrese el aprametro x del punto: "))
    sumx = sumx+x
    x2 = x**2
    sumx2 = sumx2+x2
    y = float(input("Ingrese el parametro y del punto: "))
    sumy = sumy+y
    xy = x*y
    sumxy = sumxy+xy

m = (sumxy-(sumx*sumy)/cap)/(sumx2-(sumx**2/cap))
b = y-m*x

print(f'La pendiente de la recta es: {m}\
        El intercepto es: {b}\
        La ecuacion es: y={m}x + {b}')
