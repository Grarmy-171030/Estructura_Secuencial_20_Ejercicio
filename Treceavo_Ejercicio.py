#Leer un número y mostrar su raíz cuadrada y cúbica 
# (sin usar funciones predefinidas para la raíz cúbica).
import math
numero = int(input("Ingreseel número: "))
print("Raíz cuadrada:",round(math.sqrt(numero),2))
print("Raíz cúbica:",numero ** (1 / 3))
