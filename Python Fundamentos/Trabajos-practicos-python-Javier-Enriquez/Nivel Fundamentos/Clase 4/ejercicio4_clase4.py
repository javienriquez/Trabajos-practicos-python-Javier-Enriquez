def total_factura():
    impuesto=21
    total_sin_iva=float(input("Ingrese el valor de la factura sin iva: "))
    calculo=total_sin_iva*impuesto/100
    print("El total de la factura con iva es",total_sin_iva+calculo)
    return
total_factura()
