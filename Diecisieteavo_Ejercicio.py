#Determinar la hora de llegada a una ciudad B, dada la hora de salida de A (HH:MM: SS) 
# y el tiempo de viaje en segundos.
hora_de_salida = int(input("Ingrese la hora de salida:"))
minuto_de_salida = int(input("Ingrese los minutos de salida:"))
segundo_de_salida = int(input("Ingrese los segundos de salida:"))
viaje_en_segundo = int(input("Ingrese el tiempo que ha tardado en segundos:"))
segundo_inicial = hora_de_salida * 3600 + minuto_de_salida*60 + segundo_de_salida;
segundo_final = segundo_inicial + viaje_en_segundo;
hora_de_llegada = segundo_final // 3600;
minuto_de_llegada = (segundo_final % 3600) // 60;
segundo_de_llegada = (segundo_final % 3600) % 60;
print("La ho")
print("La hora de llegada es :",hora_de_llegada,":",minuto_de_llegada,":",segundo_de_llegada)


