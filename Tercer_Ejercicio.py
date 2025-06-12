#Dados los catetos de un triángulo rectángulo, calcular su hipotenusa.
import math
cateto_opuesto=float(input("Ingrese el cateto opuesto: "))
cateto_adyacente=float(input("Ingrese el cateto adyacente: "))
hipotenusa=math.sqrt(pow(cateto_adyacente,2)+pow(cateto_opuesto,2))
print("La hipotenusa es:",hipotenusa)