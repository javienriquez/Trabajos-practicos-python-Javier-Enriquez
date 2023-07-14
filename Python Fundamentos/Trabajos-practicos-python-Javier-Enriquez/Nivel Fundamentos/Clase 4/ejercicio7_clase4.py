

def buscar_pares(lista):
    pares = [numero for numero in lista if numero % 2 == 0]
    return pares
numeros = [20,21,22,23,24,25,26,27,28,29,30]
pares = buscar_pares(numeros)
print(pares)