#Mostrar las iniciales de una persona a partir de su nombre y dos apellidos.
nombre = input("Ingrese su nombre:")
apellido_uno = input("Ingrese su primer apellido:")
apellido_dos = input("Ingrese su segundo apellido:")
inicial = nombre[0]
inicial = inicial + apellido_uno[0]
inicial = inicial + apellido_dos[0]
print("Las iniciales son:",inicial)
