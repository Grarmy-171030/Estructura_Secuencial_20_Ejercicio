# Calcular el sueldo total de un vendedor con un sueldo base más un 10% extra
# por comisión de tres ventas
import math
sueldo_base = float(input("Ingrese el sueldo base: "))
primera_venta = float(input("Ingrese el valor de la primera venta: "))
segunda_venta = float(input("Ingrese el valor de la segunda venta: "))
tercera_venta = float(input("Ingrese el valor de la tercera venta: "))
comision = 0.10 * math.fsum([primera_venta, segunda_venta, tercera_venta])
sueldo_total = sueldo_base + comision
print("El sueldo total es:", round(sueldo_total, 2))
