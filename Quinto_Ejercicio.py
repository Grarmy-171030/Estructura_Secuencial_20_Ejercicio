#Convertir un valor dado en grados Fahrenheit a grados Celsius usando la formula
import math
valor_en_farenheit=float(input("Ingrese el valor en fahrenheit: "))
valor_en_celsius=math.fsum([valor_en_farenheit, -32]) * 5 / 9
print("Grado celsius", valor_en_celsius, "°")