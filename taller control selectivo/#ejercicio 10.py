#ejercicio 10
aumentos = {
    1: 0.10,
    2: 0.15,
    3: 0.20,
    4: 0.40,
    5: 0.60
}


categoria = int(input("Ingrese la categoría del trabajador (1-5): "))
sueldo_bruto = float(input("Ingrese el sueldo bruto del trabajador en COP: "))


if categoria in aumentos:

    aumento = sueldo_bruto * aumentos[categoria]
    nuevo_sueldo = sueldo_bruto + aumento

    print("\n--- Información del Trabajador ---")
    print(f"Categoría: {categoria}")
    print(f"Sueldo Bruto Original: ${sueldo_bruto:,.2f} COP")
    print(f"Aumento Aplicado: ${aumento:,.2f} COP")
    print(f"Nuevo Sueldo Bruto: ${nuevo_sueldo:,.2f} COP")
else:
    print("Categoría inválida. Ingrese un número del 1 al 5.")
