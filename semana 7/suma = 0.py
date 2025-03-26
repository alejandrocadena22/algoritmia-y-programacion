suma = 0
k = 1
contador = 0

while suma + k <= 1000:
    suma += k
    contador += 1
    k += 1  

print("Número de términos necesarios:", contador)
