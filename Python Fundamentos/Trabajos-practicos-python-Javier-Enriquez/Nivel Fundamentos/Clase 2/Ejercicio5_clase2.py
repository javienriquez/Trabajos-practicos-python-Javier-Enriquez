personas = int(input("Ingrese la cantidad de personas que van a almorzar: "))
dineroComenzal = float(input("Ingrese la cantidad de dinero que va a gastar cada comenzal "))
precioPlato = float(input("Ingrese el precio de cada plato elegido"))
cantidadDePlatos = int((personas * dineroComenzal) / precioPlato)
print("Gastando todo el dinero, pueden consumir ",cantidadDePlatos, "platos" )





