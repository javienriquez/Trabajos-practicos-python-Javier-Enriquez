harina = float(input("Ingrese la cantidad de Kg harina disponible "))
azucar = float(input("Ingrese la cantidad de Kg de azúcar disponible "))
manteca = float(input("Ingrese la cantidad de Kg de manteca disponible "))
if harina>= 5 and azucar>=1 and manteca>=2:
    print("Usted podrá realizar la receta")
else:
    print("Faltan ingredientes")