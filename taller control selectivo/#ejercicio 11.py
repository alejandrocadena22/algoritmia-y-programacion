#ejercicio 11
temperatura = float(input("Ingrese la temperatura en grados Fahrenheit: "))


if temperatura > 85:
    deporte = "Natación"
elif 70 < temperatura <= 85:
    deporte = "Tenis"
elif 32 < temperatura <= 70:
    deporte = "Golf"
elif 10 < temperatura <= 32:
    deporte = "Esquí"
else:
    deporte = "Marcha"


print(f"A una temperatura de {temperatura}°F, el deporte recomendado es: {deporte}.")
