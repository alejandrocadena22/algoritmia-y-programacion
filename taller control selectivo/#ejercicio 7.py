#ejercicio 7

km_recorridos = float(input("Ingrese la distancia recorrida en kilómetros: "))

if km_recorridos <= 300:
    costo = 50000  
elif km_recorridos <= 1000:
    costo = 70000 + (km_recorridos - 300) * 30000  
else:
    costo = 150000 + (km_recorridos - 1000) * 9000  

print(f"\nEl costo total a pagar es: ${costo:,.2f} COP")
