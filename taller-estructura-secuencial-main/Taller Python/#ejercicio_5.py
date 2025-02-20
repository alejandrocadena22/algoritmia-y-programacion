#ejercicio_5
calificacion1 = float(input("escribir calificacion 1: "))
calificacion2 = float(input("escribir calificacion 2: "))
calificacion3 = float(input("ingrese calificacion  3: "))

examenfinal = float(input("ingrese examen final: "))
trabajofinal = float(input("ingrese trabajo final. "))

promedio_de_calificacion = (calificacion1 + calificacion2 + calificacion3)/3
notafinal = (promedio_de_calificacion * 0.55) + (examenfinal*0.30) + (trabajofinal * 0.15)

print(f"la nota final del estudiante es: {notafinal}")


