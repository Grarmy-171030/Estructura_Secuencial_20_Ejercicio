#Calcular la distancia entre dos puntos (x1, y1) y (x2, y2) en el plano.
import math
print("Ingrese las coordenadas X:")
coordenada_x1 = int(input("x1: "))
coordenada_x2= int(input("x2: "))
print("Ingrese las coordenadas Y:")
coordenada_y1 = int(input("y1: "))
coordenada_y2 = int(input("y2: "))
distancia = math.sqrt(pow( coordenada_x2- coordenada_x1, 2) + pow(coordenada_y2 - coordenada_y1, 2))
print("Distancia:", round(distancia,2))