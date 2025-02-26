#ejercicio 9
nombre = input("Ingrese el nombre del cliente: ")
monto_compra = float(input("Ingrese el monto de la compra en COP: "))


if monto_compra < 50000:
    descuento = 0
elif monto_compra <= 100000:
    descuento = 0.05
elif monto_compra <= 700000:
    descuento = 0.11
elif monto_compra <= 1500000:
    descuento = 0.18
else:
    descuento = 0.25


monto_descuento = monto_compra * descuento
monto_a_pagar = monto_compra - monto_descuento


print("\n--- Factura de Compra ---")
print(f"Cliente: {nombre}")
print(f"Monto de la compra: ${monto_compra:,.2f} COP")
print(f"Descuento aplicado: ${monto_descuento:,.2f} COP")
print(f"Total a pagar: ${monto_a_pagar:,.2f} COP")
