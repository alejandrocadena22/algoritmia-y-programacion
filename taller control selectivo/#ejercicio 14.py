#ejercicio 14
def calcular_pago(lectura_anterior, lectura_actual):
    consumo = lectura_actual - lectura_anterior
    total_pago = 0

    if consumo > 500:
        total_pago += (consumo - 500) * 120000
        consumo = 500
    if consumo > 300:
        total_pago += (consumo - 300) * 100000
        consumo = 300
    if consumo > 100:
        total_pago += (consumo - 100) * 80000
        consumo = 100
    if consumo > 0:
        total_pago += consumo * 4600

    return total_pago


lectura_anterior = int(input("Ingrese la lectura anterior del medidor (en Kwh): "))
lectura_actual = int(input("Ingrese la lectura actual del medidor (en Kwh): "))

monto_a_pagar = calcular_pago(lectura_anterior, lectura_actual)
print(f"El monto total a pagar por consumo eléctrico es: {monto_a_pagar:,} COP")
