import random
def listaATupla(lista):
    indexed_data = [(i+1, lista[i]) for i in range(len(lista))]
    return indexed_data

#print(listaATupla(["examen", "de", "python"]))

#Ejercicio 1
def guessing_game():
    numero = random.randint(0,100)
    while(1):
        entrada = int(input("Por favor ingrese un número entero: "))

        if (entrada < numero):
            print("El número introducido es más pequeño.")
        elif (entrada > numero):
            print("El número introducido es más grande.")
        else:
            print("Correcto!!!")
            break
#guessing_game()

#Ejercicio 2
def mySum(*args):
    resultado = 0
    for i in args:
        resultado = resultado + i
    print(f"Resultado: {resultado}")

#mySum(10,20,30,40,50,60,70,80)

#Ejercicio 3
def run_timing():
    resultado = 0
    acumulador = []

    while(1):
        entrada = input("Ingrese un tiempo (en minutos) de una carrera (pulse Enter para salir):")
        if entrada == "":
            break

        acumulador.append(int(entrada))

    for i in acumulador:
        resultado = resultado + i

    print(f"Numero de carreras: {len(acumulador)}. Tiempo medio en las carreras: {resultado/len(acumulador)}")

#run_timing()

#Ejercicio 4
def pig_latin(cadena):
    vocales = ['a','e','i','o','u','A','E','I','O','U']
    palabras = cadena.split(' ')
    resultado = []
    for i in palabras:
        if (i[0] in "aeiouAEIOU"):
            resultado.append(i + "way")
        else:
            resultado.append(i[1:] + i[0] + "ay")
    print(resultado)

#pig_latin("air python")

#Ejercicio 5
def ordenarAlfabeticamente(cadena):
    palabras = cadena.split(' ')
    print(f"Palabras ordenadas: {sorted(palabras)}")

    resultado = palabras[0]
    for i in palabras[1:]:
        if len(i) > len(resultado):
            resultado = i

    print(f"Palabra más larga: {resultado} | Longitud: {len(resultado)}")

#ordenarAlfabeticamente("que reciba una cadena de caracteres y devuelva todas las palabras que la componen ordenadas")

#Ejercicio 6
def even_odd_sums(lista):
    pares = 0
    impares = 0

    for indice,numero in enumerate(lista):
        if even(indice):
            pares = pares + numero
        else:
            impares = impares + numero

    tupla = (pares,impares)

    print(f"Resultado: {tupla}")

def even(numero):
    if numero % 2 == 0:
        return True
    else:
        return False

#even_odd_sums([10, 20, 30, 40, 50, 60])

#Ejercicio 7
def plus_minus(lista):
    resultado = lista[0]

    for indice,numero in enumerate(lista[1:]):
        if even(indice):
            resultado = resultado + numero
        else:
            resultado = resultado - numero

    print(f"Resultado: {resultado}")

#plus_minus([10, 20, 30, 40, 50, 60])

#Ejercicio 8
def myzip(lista1,lista2):
    resultado = []
    longitud = min(len(lista1),len(lista2))

    for i in range(longitud):
        resultado.append((lista1[i],lista2[i]))

    print(f"Resultado: {resultado}")

#myzip([10,20,30],'abc')

#Ejercicio 9
def agruparDiccionarios(lista):
    resultado = {}
    for diccionario in lista:
        for key, value in diccionario.items():
            if key in resultado:
                if isinstance(resultado[key], list):
                    resultado[key].append(value)
                else:
                    resultado[key] = [resultado[key], value]
            else:
                resultado[key] = value

    print(resultado)

#agruparDiccionarios([{'first': 'Reuven', 'last': 'Lerner','email': 'reuven@lerner.co.il'},{'first': 'Donald', 'last': 'Trump','email': 'president@whitehouse.gov'},{'first': 'Vladimir', 'last': 'Putin','email': 'president@kremvax.ru'}])

#Ejercicio 10
def alphabetize_names(lista):
    print(sorted(lista,key = lambda x: (x['last'], x['first'])))

#alphabetize_names([{'first': 'Reuven', 'last': 'Lerner', 'email': 'reuven@lerner.co.il'},{'first': 'Donald', 'last': 'Trump', 'email': 'president@whitehouse.gov'},{'first': 'Vladimir', 'last': 'Putin', 'email': 'president@kremvax.ru'}])

