numero = int(input("Ingrese un número: "))

# Generar y mostrar la tabla de multiplicar del 1 al 10
print(f"Tabla de multiplicar del {numero}:")
for i in range(1, 11):
    print(f"{numero} x {i} = {numero * i}")