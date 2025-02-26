#ejercicio 3

A = int(input("Ingrese el valor de A: "))
B = int(input("Ingrese el valor de B: "))
C = int(input("Ingrese el valor de C: "))
D = int(input("Ingrese el valor de D: "))

# Verificar la condición de D y calcular el resultado
if D == 0:
    resultado = (A - C) ** 2
else:  # D > 0
    resultado = ((A - B) ** 3) / D

# Mostrar el resultado
print("El resultado es:", resultado)
