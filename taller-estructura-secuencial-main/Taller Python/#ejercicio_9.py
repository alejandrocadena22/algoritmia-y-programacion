#ejercicio_9

horastrabajadas=float(input("escribir las horas trabajadas: "))
precio_por_horas = float(input("escribir el precio de la horas: "))

salario_bruto=horastrabajadas * precio_por_horas
descuento = salario_bruto * 0.20
salarioneto = salario_bruto - descuento

print(f"el salario bruto es: {salario_bruto}")
print(f"el salario neto es: {salarioneto}")
print(f"el descuento por impuestos es: {descuento}")
