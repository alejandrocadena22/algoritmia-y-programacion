#ejercicio_8
a= 0,0
b= 0,0
c= 0,0

#entrada

a= float(input("area a: "))
b= float(input("area b: "))
c= float(input("area c: "))

# Calcular el semiperímetro
s = (a + b + c) / 2

area = (s * (s - a) * (s - b) * (s - c))

print(f"el area del triangulo es: {area}")
