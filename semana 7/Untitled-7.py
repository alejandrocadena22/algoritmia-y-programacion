n = int(input("Ingrese la cantidad de estudiantes: "))

if n <= 0:
    print("Debe haber al menos un estudiante.")
else:
    max_altura = 0
    for i in range(n):
        altura = float(input(f"Ingrese la altura del estudiante {i+1}: "))
        if altura > max_altura:
            max_altura = altura
    print(f"La mayor altura es: {max_altura} metros")
