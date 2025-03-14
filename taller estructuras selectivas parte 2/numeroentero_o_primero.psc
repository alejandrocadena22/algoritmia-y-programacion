Algoritmo numeroentero_o_primero
	escribir "numero entero "
	leer numero 
	si numero <= 1 Entonces
		escribir"no es primo"
	sino 
		esPrimo <- verdadero
		para i <- 2 hasta numero - 1 Hacer
		 
		     si numero mod i = 0 Entonces
			esPrimo <- falso
		FinSi
	finpara
	
	si esPrimo Entonces
		escribir"es primo"
	SiNo
		escribir"no es primo"
	FinSi
	finsi
	
FinAlgoritmo

