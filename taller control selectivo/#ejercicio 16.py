#ejercicio 16
import math

def resolver_ecuacion_segundo_grado(a, b, c):
   
    d = b**2 - 4*a*c
    
    if d > 0:
        x1 = (-b + math.sqrt(d)) / (2 * a)
        x2 = (-b - math.sqrt(d)) / (2 * a)
        return f"Dos soluciones reales: X1 = {x1:.2f}, X2 = {x2:.2f}"
    elif d == 0:
        x = -b / (2 * a)
        return f"Una única solución real: X = {x:.2f}"
    else:
        return "No tiene solución en los números reales."


a = float(input("Ingrese el coeficiente A: "))
b = float(input("Ingrese el coeficiente B: "))
c = float(input("Ingrese el coeficiente C: "))

resultado = resolver_ecuacion_segundo_grado(a, b, c)
print(resultado)
