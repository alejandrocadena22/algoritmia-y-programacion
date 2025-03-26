estudiantes = []


n = int(input("Ingrese la cantidad de estudiantes: "))


if n <= 0:
    print("Debe haber al menos un estudiante.")
else:

    for i in range(n):
        nombre = input(f"Ingrese el nombre del estudiante {i+1}: ")
        puntaje = float(input(f"Ingrese el puntaje de {nombre}: "))
        estudiantes.append((nombre, puntaje))

    puntajes = [p[1] for p in estudiantes]

    max_puntaje = max(puntajes)
    min_puntaje = min(puntajes)
    promedio = sum(puntajes) / n

    estudiante_max = [p[0] for p in estudiantes if p[1] == max_puntaje][0]
    estudiante_min = [p[0] for p in estudiantes if p[1] == min_puntaje][0]

    debajo_promedio = sum(1 for p in puntajes if p < promedio) / n * 100
    encima_promedio = sum(1 for p in puntajes if p > promedio) / n * 100
    
    print("\nResultados del análisis:")
    print(f"Estudiante con el puntaje más alto: {estudiante_max} ({max_puntaje})")
    print(f"Estudiante con el puntaje más bajo: {estudiante_min} ({min_puntaje})")
    print(f"Puntaje máximo obtenido: {max_puntaje}")
    print(f"Puntaje mínimo obtenido: {min_puntaje}")
    print(f"Promedio de puntajes: {promedio:.2f}")
    print(f"Porcentaje de estudiantes por debajo del promedio: {debajo_promedio:.2f}%")
    print(f"Porcentaje de estudiantes por encima del promedio: {encima_promedio:.2f}%")

