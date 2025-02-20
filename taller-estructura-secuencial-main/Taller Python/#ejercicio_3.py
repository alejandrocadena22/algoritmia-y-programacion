#ejercicio_3
sueldobase = float(input("ingrese sueldo base:"))
venta1 = float(input("ingrese venta 1: "))
venta2 = float(input("igrese venta 2: "))
venta3 = float(input("ingrese venta 3: "))

comision = (venta1 + venta2 +venta3) * 0.10
total = sueldobase + comision 

print(f"la comision total es : {comision}")
print(f"el total a pagar es: {total}")

                           
