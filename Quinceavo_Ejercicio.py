#Intercambiar los valores de dos variables \(A\) y \(B\) e imprimir el resultado.
valor_de_a= input("Ingrese el valor de A: ")
valor_de_b = input("Ingrese el valor de B: ")
valor_temporal = valor_de_a
valor_de_a = valor_de_b
valor_de_b= valor_temporal
print("Valor de A después del intercambio:", valor_de_a)
print("Valor de B después del intercambio:", valor_de_b)
