#ejercicio 15 
def determinar_anemia(edad, sexo, hemoglobina):

    if 0 <= edad <= 1: 
        rango = (13, 26)
    elif 1 < edad <= 6: 
        rango = (10, 18)
    elif 6 < edad <= 12: 
        rango = (11, 15)
    elif 12 < edad <= 60: 
        rango = (11.5, 15)
    elif 60 < edad <= 120: 
        rango = (12.6, 15.5)
    elif 120 < edad <= 180: 
        rango = (13, 15.5)
    elif edad > 180 and sexo.lower() == "mujer": 
        rango = (12, 16)
    elif edad > 180 and sexo.lower() == "hombre": 
        rango = (14, 18)
    else:
        return "Datos inválidos"


    if hemoglobina < rango[0]:
        return "Positivo para Anemia"
    else:
        return "Negativo para Anemia"

edad_meses = int(input("Ingrese la edad en meses: "))
sexo = input("Ingrese el sexo (Hombre/Mujer): ")
hemoglobina = float(input("Ingrese el nivel de hemoglobina (g%): "))

resultado = determinar_anemia(edad_meses, sexo, hemoglobina)
print(f"Resultado del análisis: {resultado}")
