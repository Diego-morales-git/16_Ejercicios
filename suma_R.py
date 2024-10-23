def suma_facturas(facturas, estados, minimo, n, indice=0):
    if indice == n:
        return 0
    if estados[indice] == 1 and facturas[indice] >= minimo:
        return facturas[indice] + suma_facturas(facturas, estados, minimo, n, indice + 1)
    else:
        return suma_facturas(facturas, estados, minimo, n, indice + 1)

n = int(input("Ingresa el número de facturas: "))
while n < 1 or n > 100000:
    n = int(input("Error. Ingresa un número de facturas valido: "))

facturas = input("Ingresa los valores de las facturas: ").split()
while len(facturas) != n:
    facturas = input(f"Error. Debes ingresar exactamente {n} valores: ").split()
facturas = [int(valor) for valor in facturas]

estados = input("Ingresa los estados de las facturas").split()
while len(estados) != n or any(e not in ['0', '1'] for e in estados):
    estados = input(f"Error. Debes ingresar exactamente {n} valores: ").split()
estados = [int(estado) for estado in estados]

minimo = int(input("Ingresa el valor mínimo permitido"))
while minimo < 1 or minimo > 10000:
    minimo = int(input("Error. Ingresa un valor mínimo válido: "))

resultado = suma_facturas(facturas, estados, minimo, n)
print(resultado)

