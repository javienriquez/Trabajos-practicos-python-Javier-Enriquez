def promedio(lista):
    suma = sum(lista)
    if len(lista) == 0:
        return 0
    return suma /len(lista)
numeros = [6,8,7]
resultado = promedio(numeros)
print(resultado)