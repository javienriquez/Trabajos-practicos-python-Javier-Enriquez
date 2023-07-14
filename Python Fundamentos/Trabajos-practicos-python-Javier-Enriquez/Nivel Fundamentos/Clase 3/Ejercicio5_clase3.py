edad = int(input("Ingrese su edad "))
if edad < 2:
    valor = 0 
elif edad == 2 and edad <= 4:
    valor = 100
elif edad >4 and edad <= 10:
    valor = 200
elif edad > 10 and edad <= 18:
    valor = 400
elif  edad > 18 and edad <= 64:
    valor = 1000
else:
    valor = 5002
    print("Usted debe abonar ", valor)


