#ejercicio 8
P = int(input("Ingrese el valor de P: "))
Q = int(input("Ingrese el valor de Q: "))


expresion = (P**3) + (Q**4) - (2 * (P**2))


if expresion > 680:
    print("P = " + str(P) + " y Q = " + str(Q) + " satisfacen la expresión.")
else:
    print("P = " + str(P) + " y Q = " + str(Q) + " no satisfacen la expresión.")
