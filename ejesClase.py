import random,os
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

#Ejercicio 11
def palabraLetrasMayor(lista):
    palabras = lista.split()
    maximoRepe = 0
    maxPalabra = ""

    for palabra in palabras:
        letras = {}
        for letra in palabra:
            if letra in letras:
                letras[letra] += 1
            else:
                letras[letra] = 1

            maximoLetraPalabra = max(letras.values())

        if maximoLetraPalabra > maximoRepe:
            maximoRepe = maximoLetraPalabra
            maxPalabra = palabra

    print(f"Palabra con más ocurrencias: {maxPalabra}")

#palabraLetrasMayor("Esta función divide la cadena de texto en utilizando el método split(). Para cada palabra, se crea un diccionario letras_repetidas que almacena el número de ocurrencias de cada letra. Se itera a través de cada letra de la palabra y se actualiza el valor correspondiente en el diccionario.")

#Ejercicio 12
PEOPLE = [('Donald', 'Trump', 7.85), ('Vladimir', 'Putin', 3.626), ('Jinping', 'Xi', 10.603)]

def format_sort_records(lista):
    resultado = ""
    for i in lista:
        resultado = resultado + i[1] + "\t" + i[0] + "\t" + str(int(i[2])) + "." + (str(i[2]).split('.')[1][0:2]) + "\n"
    print(resultado)

#format_sort_records(PEOPLE)

#Ejercicio 13
MENU = {"sandwich":10,"tea":7}
def restaurante():
    cuenta = 0
    while (1):
        entrada = input("Ingrese un plato (pulse Enter para salir):")
        if entrada == "":
            break

        try:
            cuenta = cuenta + MENU[entrada]
            print(f"{entrada} cuesta {MENU[entrada]}. Cuenta acumulada: {cuenta}")
        except:
            print("No existe ese plato")

    print(f"Total: {cuenta}")

#restaurante()

#Ejercicio 14
def dictdiff(d1, d2):
    diff = {}
    keys = d1.keys() | d2.keys()
    for key in keys:
        if d1.get(key) != d2.get(key):
            diff[key] = [d1.get(key), d2.get(key)]
    print(diff)

d1 = {'a': 1, 'b': 2, 'c': 3}
d2 = {'a': 1, 'b': 2, 'c': 4}
d3 = {'a': 1, 'b': 2, 'd': 3}
d4 = {'a': 1, 'b': 2, 'c': 4}
d5 = {'a': 1, 'b': 2, 'd': 4}

#dictdiff(d1,d5)

#Ejercicio 15
def extensiones(directorio):
    dic = {}
    for file in os.walk(directorio):
        if '.' in file:
            extension = file.split('.')[1]
            if extension not in dic.keys():
                dic[extension] = 1
            else:
                dic[extension] += 1
    print(dic)

#extensiones("/Users/alvaroraso/Desktop")
def extensiones2(directorio):
    dic = {}
    for root, dirs, files in os.walk(directorio):
        for file in files:
            if '.' in file:
                extension = file.split('.')[-1]
                if extension not in dic.keys():
                    dic[extension] = 1
                else:
                    dic[extension] += 1
    for key, value in dic.items():
        print(f"{key}\t{value}")

#extensiones2("/Users/alvaroraso/Documents")

#Ejercicio 16
def tail(ruta):
    fichero = open(ruta)
    resultado = fichero.read().split("\n")[-10:]
    print(resultado)
    print(len(resultado))

#tail("/Users/alvaroraso/Downloads/texto.txt")

#Ejercicio 17
def read_sum(ruta):
    fichero = open(ruta).read().split()
    acumulador = []
    for num in fichero:
        try:
            acumulador.append((int(num)))
        except:
            pass
    print(f"Suma: {sum(acumulador)}")

#read_sum("/Users/alvaroraso/Downloads/numeros.txt")

#Ejercicio 18
def passwd_to_dict(file_path):
    users_dict = {}
    with open(file_path, 'r') as file:
        for line in file:
            if not line.strip() or line.startswith('#'):
                continue
            user_info = line.split(':')
            username, user_id = user_info[0], user_info[2]
            users_dict[username] = int(user_id)
    return users_dict

#passwd_to_dict("/Users/alvaroraso/Downloads/numeros.txt")

#Ejercicio 19
