#ejercicio_7
metros = float(input("escribir cantidad en metros: "))

pulgadas = metros * 39.27
pies = (pulgadas) / 12
pulgadas_restantes = pulgadas - (pies*12) 

print(f"la conversion es: {pies}) , (pies y", pulgadas_restantes, (f"pulgadas: {pulgadas}"))