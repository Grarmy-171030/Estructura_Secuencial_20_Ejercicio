#Convertir una cantidad de minutos a horas y minutos (ejemplo: 1000 minutos →16 horas y 40 minutos)
minutos=int(input("Ingrese la cantidad en minutos: "))
conversor_horas=minutos//60 
conversor_minutos=minutos%60
print(conversor_horas,"horas" ,"y",conversor_minutos,"minutos")
