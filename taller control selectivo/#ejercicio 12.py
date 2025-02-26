#ejercicio 12
denominaciones = [100000, 50000, 20000, 10000, 5000, 2000, 1000, 500, 200, 100, 50]

cantidad = int(input("Ingrese la cantidad en COP: "))

cantidad = (cantidad // 50) * 50

resultado = []


for valor in denominaciones:
    if cantidad >= valor:
        resultado.append(str(valor)) 
        cantidad -= valor

print("Salida:", ",".join(resultado))
