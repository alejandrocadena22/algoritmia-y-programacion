Algoritmo normal_3
	Escribir "Ingrese un a�o:"
		Leer a�o
		Si (a�o mod 4 = 0 Y a�o mod 100 <> 0) O (a�o mod 400 = 0) Entonces
			Escribir "Es bisiesto"
		SiNo
			Escribir "No es bisiesto"
		FinSi

FinAlgoritmo