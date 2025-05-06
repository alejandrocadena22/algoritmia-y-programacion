numeros = [12, 23, 5, 12, 92, 5, 12, 5, 29, 92, 64, 23]

conteo = {}

for numero in numeros:
    if numero in conteo:
        conteo[numero] += 1
    else:
        conteo[numero] = 1

print("Conteo de apariciones:")
print(conteo)
