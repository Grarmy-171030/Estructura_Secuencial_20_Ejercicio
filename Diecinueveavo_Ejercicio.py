#Calcular la nota final de un estudiante según:
# Respuesta correcta: +5 puntos.
# Incorrecta: -1 punto.
#  En blanco: 0 puntos.
respuestas_correctas   = int(input("Ingrese la cantidad de respuestas correctas: "))
respuestas_incorrectas = int(input("Ingrese la cantidad de respuestas incorrectas: "))
nota_final = respuestas_correctas * 5 + respuestas_incorrectas * (-1)
print("La nota final es:", nota_final)