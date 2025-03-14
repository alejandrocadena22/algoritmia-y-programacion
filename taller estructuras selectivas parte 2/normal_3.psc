Algoritmo normal_3
	Escribir "Ingrese un año:"
		Leer año
		Si (año mod 4 = 0 Y año mod 100 <> 0) O (año mod 400 = 0) Entonces
			Escribir "Es bisiesto"
		SiNo
			Escribir "No es bisiesto"
		FinSi

FinAlgoritmo