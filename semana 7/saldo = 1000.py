saldo = 1000 

while True:

    print("\n--- Cajero Automático ---")
    print("1. Depositar dinero")
    print("2. Retirar dinero")
    print("3. Consultar saldo")
    print("4. Salir")


    opcion = input("Seleccione una opción (1-4): ")

    if opcion == "1":
 
        deposito = float(input("Ingrese el monto a depositar: "))
        if deposito > 0:
            saldo += deposito
            print(f"Depósito exitoso. Nuevo saldo: {saldo:.2f}")
        else:
            print("El monto debe ser mayor a 0.")

    elif opcion == "2":

        retiro = float(input("Ingrese el monto a retirar: "))
        if 0 < retiro <= saldo:
            saldo -= retiro
            print(f"Retiro exitoso. Nuevo saldo: {saldo:.2f}")
        elif retiro > saldo:
            print("Fondos insuficientes.")
        else:
            print("El monto debe ser mayor a 0.")

    elif opcion == "3":
 
        print(f"Su saldo actual es: {saldo:.2f}")

    elif opcion == "4":
 
        print("Gracias por usar el cajero automático.")
        break

    else:
        print("Opción no válida. Intente nuevamente.")
