#Invertir un número de dos cifras (ejemplo: 23 → 32).
numero_de_dos_cifras= int(input("Ingrese un número de dos cifras: "))
# Divide el número entre 10 y toma solo la parte entera
decenas = numero_de_dos_cifras // 10
#obtiene el resto de dividir entre 10
unidades = numero_de_dos_cifras % 10
invertido = unidades * 10 + decenas
print("Número invertido:", invertido)