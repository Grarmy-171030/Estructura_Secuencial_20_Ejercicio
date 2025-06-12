#Calcular el dinero total en euros y céntimos a partir de monedas de 2€, 1€, 50¢, 20¢ y 10¢.
monedas_2_euros   = int(input("Ingrese numero de monedas de 2€: "))
monedas_1_euro    = int(input("Ingrese numero  de monedas de 1€: "))
monedas_50_cent   = int(input("Ingrese numero  de monedas de 50¢: "))
monedas_20_cent   = int(input("Ingrese numero  de monedas de 20¢: "))
monedas_10_cent   = int(input("Ingrese numero de monedas de 10¢: "))
total_euros = monedas_2_euros * 2 + monedas_1_euro
total_centimos = monedas_50_cent * 50 + monedas_20_cent * 20 + monedas_10_cent* 10
total_euros = total_euros + total_centimos // 100
total_centimos = total_centimos % 100
print(total_euros," euros y",total_centimos," céntimos.")
