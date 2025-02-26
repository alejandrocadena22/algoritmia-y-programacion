#ejercicio 13
from datetime import datetime

signos = {
    "Capricornio":  ((12, 22), (1, 20)),
    "Acuario":      ((1, 21), (2, 19)),
    "Piscis":       ((2, 20), (3, 19)),
    "Aries":        ((3, 21), (4, 20)),
    "Tauro":        ((4, 21), (5, 21)),
    "Géminis":      ((5, 22), (6, 21)),
    "Cáncer":       ((6, 22), (7, 22)),
    "Leo":          ((7, 23), (8, 23)),
    "Virgo":        ((8, 24), (9, 22)),
    "Libra":        ((9, 23), (10, 22)),
    "Escorpión":    ((10, 23), (11, 21)),
    "Sagitario":    ((11, 22), (12, 21))
}


fecha_nacimiento = input("Ingrese su fecha de nacimiento (DD/MM/AAAA): ")
dia, mes, anio = map(int, fecha_nacimiento.split("/"))


signo = ""
for s, ((mes_inicio, dia_inicio), (mes_fin, dia_fin)) in signos.items():
    if (mes == mes_inicio and dia >= dia_inicio) or (mes == mes_fin and dia <= dia_fin):
        signo = s
        break


hoy = datetime.today()
edad = hoy.year - anio - ((hoy.month, hoy.day) < (mes, dia))

print(f"Su signo zodiacal es: {signo}")
print(f"Su edad es: {edad} años")
