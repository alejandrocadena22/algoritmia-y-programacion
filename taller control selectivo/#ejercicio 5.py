#ejercicio 5 

ventas_dep1 = float(input("Ingrese el monto de ventas del Departamento 1: "))
ventas_dep2 = float(input("Ingrese el monto de ventas del Departamento 2: "))
ventas_dep3 = float(input("Ingrese el monto de ventas del Departamento 3: "))


salario_bruto = float(input("Ingrese el salario bruto mensual de los vendedores: "))


ventas_totales = ventas_dep1 + ventas_dep2 + ventas_dep3

limite_incentivo = ventas_totales * 0.33


incentivo_dep1 = salario_bruto * 0.20 if ventas_dep1 > limite_incentivo else 0
incentivo_dep2 = salario_bruto * 0.20 if ventas_dep2 > limite_incentivo else 0
incentivo_dep3 = salario_bruto * 0.20 if ventas_dep3 > limite_incentivo else 0


salario_final_dep1 = salario_bruto + incentivo_dep1
salario_final_dep2 = salario_bruto + incentivo_dep2
salario_final_dep3 = salario_bruto + incentivo_dep3


print("\nResumen de pagos:")
print(f"Salario final por vendedor en Departamento 1: ${salario_final_dep1:,.2f} COP")
print(f"Salario final por vendedor en Departamento 2: ${salario_final_dep2:,.2f} COP")
print(f"Salario final por vendedor en Departamento 3: ${salario_final_dep3:,.2f} COP")
