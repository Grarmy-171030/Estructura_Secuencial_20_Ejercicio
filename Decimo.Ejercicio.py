#Calcular la calificación final de un alumno en Algoritmos, considerando:
# 55% promedio de tres parciales.
# 30% examen final.
# 15% trabajo final. 
parcial_uno=float(input("Ingrese su nota del primer parcial"))
parcial_dos=float(input("Ingrese su nota del segundo parcial"))
parcial_tres=float(input("Ingrese su nota del tercer parcial"))
examen_final=float(input("Ingrese su nota del examen final"))
trabajo_final=float(input("Ingrese su nota del trabajo final"))
calificacion_final = ((parcial_uno + parcial_dos + parcial_tres) / 3) * 0.55 + examen_final * 0.30 + trabajo_final * 0.15
print("Calificación final:", round(calificacion_final, 2))