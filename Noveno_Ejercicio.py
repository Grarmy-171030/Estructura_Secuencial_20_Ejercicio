#Calcular el precio final de una compra aplicando un descuento del 15%
import math
precio_original = float(input("Ingrese el precio de su compra: "))
print("Precio final:", math.prod([precio_original, 0.85]),)
