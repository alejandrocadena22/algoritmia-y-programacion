#ejercicio 2
def calcular_sueldo (sueldo_actual):
    if sueldo_actual < 900000:
        aumento=sueldo_actual * 0.15
    else:
        sueldo_actual > 900000
        aumento = sueldo_actual * 0.12

        nuevo_sueldo = sueldo_actual + aumento
    return nuevo_sueldo

sueldo = float(input("Ingrese el sueldo actual del trabajador: "))
nuevo_sueldo = (sueldo)
print(f"El nuevo sueldo del trabajador es: ${nuevo_sueldo:,.2f} COP")
