# Calcular la media de tres números pedidos por teclado
import math
numero_uno=float(input("Ingrese un numero: "))
numero_dos=float(input("Ingrese un numero: "))
numero_tres=float(input("Ingrese un numero: 6"))
media= math.fsum([numero_uno,numero_dos,numero_tres])/3
print("La media es: " ,media)