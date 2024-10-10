#Ejercicio 1: Contar palabras en una lista :)
def contar(lista):
    conteo = {}
    for palabra in lista:
        if palabra in conteo:
            conteo[palabra] += 1
        else:
            conteo[palabra] = 1
    return conteo

palabras = ["python", "java", "python", "c++"]
res = contar(palabras)
print(res)
print("----------------------------")
print()

#Ejercicio 2: Combinar dos diccionarios sumando valores comunes :)
def combinar(diccionario1, diccionario2):
    resultado = diccionario1.copy()
    for clave, valor in diccionario2.items():
        resultado[clave] = resultado.get(clave, 0) + valor
    return resultado

dic1 = {'a': 1, 'b': 2}
dic2 = {'b': 3, 'c': 4}
res_comb = combinar(dic1, dic2)
print(res_comb)
print("----------------------------")
print()

#Ejercicio 3: Contar la frecuencia de números en una lista :)
def frecuencia(numeros):
    frec_num = {}
    for numero in numeros:
        frec_num[numero] = frec_num.get(numero, 0) + 1
    return frec_num

numeros = [1, 1, 2, 3, 3, 3]
res = frecuencia(numeros)
print(res)
print("----------------------------")
print()

#Ejercicio 4: Filtrar palabras por longitud :)
def filtrar(palabras, long):
    return [palabra for palabra in palabras if len(palabra) > long and palabra == "programación"]

lista_pal = ["hola", "mundo", "python", "programación"]
resultado = filtrar(lista_pal, 5)
print(resultado)
print("----------------------------")
print()


#Ejercicio 5: Invertir una lista de tuplas :)
def invertir(tuplas):
    return [(y, x) for x, y in tuplas]

lista_tuplas = [(1, 2), (3, 4), (5, 6)]
resultado = invertir(lista_tuplas)
print(resultado)
print("----------------------------")
print()


#Ejercicio 6: Encontrar el número más frecuente en una lista :)
def num_frecuente(numeros):
    from collections import Counter
    return Counter(numeros).most_common(1)[0][0]

lista_num = [1, 2, 3, 1, 2, 1]
resultado = num_frecuente(lista_num)
print(resultado)
print("----------------------------")
print()

#Ejercicio 7: Comprobar si un conjunto es subconjunto de otro :)
def subconjunto(subconjunto, conjunto):
    return subconjunto.issubset(conjunto)

conj1 = {1, 2, 3}
conj2 = {1, 2, 3, 4, 5}
resultado = subconjunto(conj1, conj2)
print(resultado)
print("----------------------------")
print()

#Ejercicio 8: Agrupar personas por edad :)
def agrupar(personas):
    grupos = {}
    for persona in personas:
        grupos.setdefault(persona["edad"], []).append(persona["nombre"])
    return grupos

lista_personas = [{"nombre": "Ana", "edad": 25}, {"nombre": "Luis", "edad": 25}, {"nombre": "Carlos", "edad": 30}]
resultado = agrupar(lista_personas)
print(resultado)
print("----------------------------")
print()

#Ejercicio 9: Implementar Merge Sort :)
def ordenar(lista):
    if len(lista) <= 1:
        return lista
    medio = len(lista) // 2
    izquierda = ordenar(lista[:medio])
    derecha = ordenar(lista[medio:])
    return fusionar(izquierda, derecha)

def fusionar(izquierda, derecha):
    resultado = []
    while izquierda and derecha:
        if izquierda[0] < derecha[0]:
            resultado.append(izquierda.pop(0))
        else:
            resultado.append(derecha.pop(0))
    resultado.extend(izquierda or derecha)
    return resultado

numeros = [5, 3, 8, 6, 2]
resultado = ordenar(numeros)
print(resultado)
print("----------------------------")
print()

#Ejercicio 10: Eliminar elementos menores a un valor dado :)
def eliminar(lista, limite):
    return list(filter(lambda x: x >= limite, lista))

numeros = [1, 2, 3, 4, 5]
limite = 3
resultado = eliminar(numeros, limite)
print(resultado)
print("----------------------------")
print()

#Ejercicio 11: Aplanar una lista de listas :)
def aplanar(lis_lis):
    return [item for sublis in lis_lis for item in sublis]

listas = [[1, 2], [3, 4], [5]]
resultado = aplanar(listas)
print(resultado)
print("----------------------------")
print()

#Ejercicio 12: Calcular la mediana de una lista :)
def calc_mediana(lista_numeros):
    lista_numeros.sort()
    mitad = len(lista_numeros) // 2
    return lista_numeros[mitad] if len(lista_numeros) % 2 != 0 else (lista_numeros[mitad - 1] + lista_numeros[mitad]) / 2

numeros = [1, 3, 2, 4, 5]
resultado = calc_mediana(numeros)
print(resultado)
print("----------------------------")
print()

#Ejercicio 13: Duplicar elementos en una lista :)
def duplicar(lista):
    return [elemento for numero in lista for elemento in (numero, numero)]

numeros = [1, 2, 3]
resultado = duplicar(numeros)
print(resultado)
print("----------------------------")
print()

#Ejercicio 14: Contar palabras en frases :)
def contar_pal(frases):
    return {indice: len(frase.split()) for indice, frase in enumerate(frases)}

lista_frases = ["Hola mundo", "Python es genial", "Me gusta programar"]
resultado = contar_pal(lista_frases)
print(resultado)
print("----------------------------")
print()

#Ejercicio 15: Encontrar la clave con el valor máximo en un diccionario :)
def valor_maximo(diccionario):
    return max(diccionario, key=diccionario.get)

diccionario = {'a': 10, 'b': 20, 'c': 5}
resultado = valor_maximo(diccionario)
print(resultado)
print("----------------------------")
print()

#Ejercicio 16: Encontrar palíndromos en una lista de palabras :)
def palindromos(lista_palabras):
    return [palabra for palabra in lista_palabras if palabra == palabra[::-1]]

palabras = ["ana", "oso", "hola", "level"]
resultado = palindromos(palabras)
print(resultado)
print("----------------------------")
print()
