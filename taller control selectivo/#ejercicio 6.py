#ejercicio 6 

A = int(input("Ingrese el valor de A: "))
B = int(input("Ingrese el valor de B: "))
C = int(input("Ingrese el valor de C: "))
D = int(input("Ingrese el valor de D: "))


N = A * 1000 + B * 100 + C * 10 + D


redondeado = round(N, -2)


print(f"\nEl número formado es: {N}")
print(f"El número redondeado a la centena más cercana es: {redondeado}")
