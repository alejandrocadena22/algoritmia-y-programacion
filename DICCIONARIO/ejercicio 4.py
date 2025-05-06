estudiantes = {}
max_estudiantes = 10

print("Introduce los datos de los estudiantes (máximo 10):")

for i in range(1, max_estudiantes + 1):
    print(f"\nEstudiante {i}:")
    nombre = input("Nombre: ").strip()
    while True:
        try:
            nota = float(input("Nota: "))
            if 0 <= nota <= 10:
                break
            else:
                print("La nota debe estar entre 0 y 10.")
        except ValueError:
            print("Por favor, introduce un número válido para la nota.")
    
    estudiantes[str(i)] = {
        "nombre": nombre,
        "nota": nota
    }

aprobados = []
suspendidos = []
suma_notas = 0

for datos in estudiantes.values():
    nota = datos["nota"]
    suma_notas += nota
    if nota >= 5:
        aprobados.append(datos["nombre"])
    else:
        suspendidos.append(datos["nombre"])

media = suma_notas / len(estudiantes)


print("\nEstudiantes Aprobados:")
for nombre in aprobados:
    print(f"- {nombre}")

print("\nEstudiantes Suspendidos:")
for nombre in suspendidos:
    print(f"- {nombre}")

print(f"\nNota media de la clase: {media:.2f}")
