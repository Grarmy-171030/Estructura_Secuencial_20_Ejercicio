#Calcular el tiempo (en minutos) en que un vehículo más rápido alcanza a otro, 
# dada la distancia d y velocidades v1 y v2.
velocidad_uno=float(input("Ingrese la primera velocidad 1:"))
velocidad_dos=float(input("Ingrese la segunda velocidad 2: "))
distancia = float(input("Ingrese la distancia entre los vehiculos:"))
tiempo_en_horas = distancia / abs(velocidad_uno - velocidad_dos)
tiempo_en_minutos= tiempo_en_horas * 60
print("Lo alcanza en",tiempo_en_minutos,"minutos.")
