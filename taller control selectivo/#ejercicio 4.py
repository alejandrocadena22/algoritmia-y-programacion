#ejercicio 4

monto_compra = float(input("Ingrese el monto total de la compra en COP: "))

# Definir variables
if monto_compra > 5000000:
    inversion_empresa = monto_compra * 0.55
    prestamo_banco = monto_compra * 0.30
    credito_fabricante = monto_compra * 0.15
else:
    inversion_empresa = monto_compra * 0.70
    prestamo_banco = 0
    credito_fabricante = monto_compra * 0.30

# Calcular intereses del crédito
intereses = credito_fabricante * 0.20

# Mostrar resultados
print("\nResumen de pagos:")
print(f"Inversión de la empresa: ${inversion_empresa:,.2f} COP")
print(f"Cantidad a crédito con el fabricante: ${credito_fabricante:,.2f} COP")
print(f"Monto por intereses: ${intereses:,.2f} COP")

if prestamo_banco > 0:
    print(f"Cantidad prestada al banco: ${prestamo_banco:,.2f} COP")
