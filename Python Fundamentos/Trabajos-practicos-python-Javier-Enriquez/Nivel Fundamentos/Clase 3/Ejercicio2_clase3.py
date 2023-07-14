nacimiento = int( input("Ingrese su año de nacimiento "))
anioActual = 2023
edad = anioActual - nacimiento
if edad >= 18:
    print("Usted es mayor de edad")
else:
    print("Usted es menor de edad")