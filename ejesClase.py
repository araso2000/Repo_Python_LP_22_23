import random,os,argparse
#import operator,requests
from datetime import date, time, datetime

#Ejercicios del listado
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
def encriptar(texto):
    fichero = open(texto, "r").read()
    archivo = open("/Users/alvaroraso/Downloads/encrypt.txt" , "w")
    for i in list(fichero):
        archivo.write(f"{ord(i)} ")

    archivo.close()

#encriptar("/Users/alvaroraso/Downloads/texto.txt")

def desencriptar(fichero):
    leido = list(open(fichero, "r").read().split(" "))[:-1]
    resultado = ""
    for i in leido:
        resultado = resultado + chr(int(i))
    print(resultado)

#desencriptar("/Users/alvaroraso/Downloads/encrypt.txt")

#Ejercicio 20
def myxml(*args):
    resultado = ""
    argumentos = args
    if len(argumentos) == 1:
        resultado = f"<{argumentos[0]}></{argumentos[0]}>"
    elif len(argumentos) == 2:
        resultado = f"<{argumentos[0]}>{argumentos[1]}</{argumentos[0]}>"
    else:
        resultado = resultado + f"<{argumentos[0]}"
        for i in argumentos[2:]:
            resultado = resultado + f" {i.split('=')[0]}=\"{i.split('=')[1]}\""
        resultado = resultado + f">{argumentos[1]}</{argumentos[0]}>"
    return resultado

#print(myxml('foo','bar', 'a=1', 'a=2'))

#Ejercicio 21
def copyfile(origen,*destinos):
    fileOrigen = open(origen,'r')
    contenido = fileOrigen.read()
    for i in destinos:
        fileDestino = open(i, 'w')
        fileDestino.write(contenido)
        fileDestino.close()
    print("Copiado!")

#copyfile("/Users/alvaroraso/Downloads/encrypt.txt","/Users/alvaroraso/Downloads/copy1.txt","/Users/alvaroraso/Downloads/copy2.txt","/Users/alvaroraso/Downloads/copy3.txt")

#Ejercicio 22

def create_password_generator(caracteres_permitidos):
    def generate_password(longitud):
        password = ''
        for _ in range(longitud):
            password += random.choice(caracteres_permitidos)
        return password
    return generate_password

alpha_password = create_password_generator('abcdef')
symbol_password = create_password_generator('!@#$%')

"""
print(alpha_password(5))    # Ejemplo de contraseña alfabética de longitud 5
print(alpha_password(10))   # Ejemplo de contraseña alfabética de longitud 10

print(symbol_password(5))   # Ejemplo de contraseña con símbolos de longitud 5
print(symbol_password(10))  # Ejemplo de contraseña con símbolos de longitud 10
"""

#Code Labs
#CodeLab 1

facebook_stocks = """Date,Open,High,Low,Close,Volume,Adj Close
2012-05-18,42.05,45.0,38.0,38.23,573576400,38.23
2012-05-21,36.53,36.66,33.0,34.03,168192700,34.03
2012-05-22,32.61,33.59,30.94,31.0,101786600,31.0
2012-05-23,31.37,32.5,31.36,32.0,73600000,32.0
2012-05-24,32.95,33.21,31.77,33.03,50237200,33.03
2012-05-25,32.9,32.95,31.11,31.91,37149800,31.91
2012-05-29,31.48,31.69,28.65,28.84,78063400,28.84
2012-05-30,28.7,29.55,27.86,28.19,57267900,28.19
2012-05-31,28.55,29.67,26.83,29.6,111639200,29.6
2012-06-01,28.89,29.15,27.39,27.72,41855500,27.72
2012-06-04,27.2,27.65,26.44,26.9,35230300,26.9
2012-06-05,26.7,27.76,25.75,25.87,42473400,25.87
"""

def cierre():
    lineas = facebook_stocks.replace('\n',',').split(',')
    print(lineas)
    print(facebook_stocks.index("Close"))

#cierre()

#CodeLab2

def listaATupla(lista):
    indexed_data = [(i+1, lista[i]) for i in range(len(lista))]
    return indexed_data

#print(listaATupla(["examen", "de", "python"]))

#CodeLab3
text = "Durante el hiato de la banda, se embarcó en una carrera como solista en 2004 al lanzar su álbum de estudio debut Love. Angel. Music. Baby. inspirado en la música pop de la década de 1980, tuvo éxito comercial y de crítica. Engendró seis sencillos, incluidos «What You Waiting For?», «Rich Girl», «Hollaback Girl» y «Cool». «Hollaback Girl» alcanzó el número uno en la lista Billboard Hot 100 y también se convirtió en la primera canción en vender en formato digital un millón de copias. En 2006, lanzó su segundo álbum de estudio, The Sweet Escape. Entre los sencillos están «Wind It Up» y «The Sweet Escape», este último ha sido el número tres en la lista Billboard Hot 100 de fin de año del 2007. Su tercer disco en solitario, This Is What the Truth Feels Like (2016), fue su primer álbum solista en alcanzar el número uno en la lista Billboard 200. Su cuarto y primer álbum navideño, You Make It Feel Like Christmas, lanzado en 2017 y se ubicó en 19 pistas en la lista Holiday Digital Song Sales de Billboard en los Estados Unidos. Ha lanzado varios sencillos con Blake Shelton, incluido «Nobody but You» (2020), que alcanzó el número 18 en los EE. UU."

def contarPalabras():
    signos_puntuacion = [".", ",", ";", ":", "!", "?", "¡", "¿", "(", ")", "[", "]", "{", "}", "<", ">", "'", "\"", "-", "–", "—", "/", "\\", "|", "«", "»"]

    filtrado = text
    for i in signos_puntuacion:
        filtrado = filtrado.replace(i,'')
    palabras = filtrado.split()
    diccionario = {}

    for i in palabras:
        if i in diccionario.keys():
            diccionario[i] = diccionario[i] + 1
        else:
            diccionario[i] = 1

    print(diccionario)
    print(len(text))
    print(len(diccionario))

#contarPalabras()

#CodeLab4
def interseccion(inter1, inter2):
    inter3 = []
    for i in inter1:
        if i in inter2:
            inter3.append(i)
    print(inter3)

"""
interseccion([1, 2, 3, 4], [3, 5, 0, 4])
interseccion((1, 2, 3, 4), (1, -1))
interseccion("hola", "hola mundo")
interseccion({"r.cabido": 4, "s.montalvo": 10, "d.concha": 2}, {'juan.perez', 'r.cabido'})
"""

#CodeLab5 (4.5)
def intersecciones(*args):
    inter1 = args[0]
    resultado = []
    for i in args[1:]:
        for j in i:
            if j in inter1 and j not in resultado:
                resultado.append(j)
    print(resultado)

#intersecciones([1, 2, 3, 4],[1, 88, 99],[1, 2],[55,66,77])

#CodeLab6
def shells(ruta):
    lista = open(ruta,'r').readlines()
    print(lista)
    lineas = []
    for i in lista:
        lineas.append(i.strip().split(':'))
    diccionario = {}
    for i in lineas:
        if i[6] in diccionario.keys():
            diccionario[i[6]] = diccionario[i[6]] + 1
        else:
            diccionario[i[6]] = 1

    print(diccionario)

#shells("/Users/alvaroraso/Downloads/passwd.txt")

#TEORIA DATETIME
# Crear un objeto de fecha para el 12 de mayo de 2023
fecha = date(2023, 5, 12)

# Crear un objeto de tiempo para las 9:30 AM
hora = time(9, 30)

# Crear un objeto de fecha y hora para el 12 de mayo de 2023 a las 9:30 AM
fecha_hora = datetime(2023, 5, 12, 9, 30)

# Obtener la fecha y hora actual
fecha_hora_actual = datetime.now()

# Obtener el año actual
año_actual = datetime.now().year

# Formatear una fecha como una cadena
fecha_formateada = datetime.now().strftime("%d/%m/%Y %H:%M:%S")

#TEORIA ARGPARSER
parser = argparse.ArgumentParser()
parser.add_argument("-n", "--nombre", help="Especifica el nombre")
args = parser.parse_args()
nombre = args.nombre

#CodeLab7 -> GitHub API
"""def api():
    gitlab_user = "XXXXXXXX"
    gitlab_api_url = "https://gitlab.com/api/v4/"
    projects_endpoint = f"users/{gitlab_user}/projects"
    response = requests.get(gitlab_api_url + projects_endpoint)
    # print(response)
    # print(response.text)
    # print(response.json())
    projects = response.json()  # type of projects?
    sorted_projects = sorted(projects, key=operator.itemgetter("last_activity_at"), reverse=True)
    result = [(project["name"], project["last_activity_at"]) for project in sorted_projects]
    print("\n".join(map(str, result)))"""

#POO
class Point2d:
 def __init__(self, x=0, y=0):
    self.x = x
    self.y = y
 def __str__(self):
    return f"({self.x},{self.y})"
 def __add__(self):
    return self.x + self.y + 1 + 5
 def getx(self):
    return self.x
 def gety(self):
    return self.y
 def shift(self, x_offset, y_offset):
    self.x += x_offset
    self.y += y_offset

if __name__ == "__main__":
    point = Point2d(0, 0)
    print(point)
    point.shift(3, 4)
    print(point)
    print(point.x)

#Uso de __call__ -> Permite usar un objeto como una funcion
class MiClase:
    def __call__(self, *args, **kwargs):
        print("¡La instancia ha sido invocada como una función!")
        print("Argumentos posicionales:", args)
        print("Argumentos con nombre:", kwargs)

# Crear una instancia de MiClase
objeto = MiClase()

# Llamar a la instancia como una función
objeto(1, 2, nombre="Juan", edad=25) #objeto no es una funcion, si no un objeto con una funcion auto ejecutable

#Herencia
class Person:
    def __init__(self, name, job=None, pay=0):
        self._name = name
        self._job = job
        self._pay = pay
    def lastname(self):
        return self._name.split()[-1]
    def giveraise(self, percent):
        self._pay = int(self._pay * (1 + percent))
    def __str__(self): #Sirve para imprimir, como el toString de Java
        return f'[Person: {self._name}, {self._pay}]'
class Manager(Person): #Manager hereda de Person
    def giveraise(self, percent, bonus=.10): #Tambien puedo sobreescribir metodos ya heredados de la clase padre
        Person.giveraise(self, percent + bonus)
        super().giveraise(percent + bonus) #super como en java

if __name__ == '__main__':
    bob = Person('Bob Smith')
    sue = Person('Sue Jones', job='dev', pay=100000)
    sue.giveraise(.10)
    tom = Manager('Tom Jones', 'mgr', 50000)

#TEORIA EXCEPCIONES
#Se pueden hacer propias excepciones basándose en la herencia de la clase Exception
"""class Error(Exception):
    Base class for exceptions in this module.
    pass
class InputError(Error):
    Exception raised for errors in the input. Attributes:
        expression -- input expression in which the error occurred
        message -- explanation of the error
    def __init__(self, expression, message):
        self.expression = expression
        self.message = message"""

#Ejercicios de exámenes
def my_zip(*sequences):
    # Determinar la longitud mínima de las secuencias
    min_length = min(len(seq) for seq in sequences)
    # Crear la lista de tuplas
    result = [(seq[i] for seq in sequences) for i in range(min_length)]
    print(result)

my_zip([10,20,30],"abc")

def funcion(dic):
    if even(dic[1]):
        return False
    else:
        return True
def dict_partition(diccionario,funcion):
    dic1 = {}
    dic2 = {}
    for i in diccionario.items():
        if funcion(i):
            dic1[i[0]] = i[1]
        else:
            dic2[i[0]] = i[1]
    print(dic1)
    print(dic2)

dict_partition({'hola':1, 'adios':2},funcion)


import argparse

def tail(file_path, num_lines=10):
    try:
        with open(file_path, 'r') as file:
            lines = file.readlines()
            last_lines = lines[-num_lines:]
            for line in last_lines:
                print(line.rstrip())
    except FileNotFoundError:
        print(f"El archivo '{file_path}' no existe.")

if __name__ == '__main__':
    # Crear el objeto ArgumentParser
    parser = argparse.ArgumentParser(description='Programa para mostrar las últimas líneas de un archivo.')

    # Agregar los argumentos
    parser.add_argument('--file', required=True, help='Ruta del archivo')
    parser.add_argument('--lines', type=int, default=10, help='Número de líneas a mostrar')

    # Parsear los argumentos de la línea de comandos
    args = parser.parse_args()

    # Llamar a la función tail con los argumentos proporcionados
    tail(args.file, args.lines)

#Random:
"""
import random
value1 = random.randrange(1, 100)
value2 = random.randrange(1, 100)
"""

#Listas
"""
error_message = "NameError: name 'a' is not defined."
print(error_message[-1]) # last item in the sequence
print(error_message[-2:]) # last two items in the sequence
print(error_message[:-2]) # all items except the last two
print(error_message[::-1]) # all items in the sequence, reversed
"""

#Listas por compresión
#dp_numbers = [number*2 for number in numbers if number >= 0]
#dp_numbers = [number*2 if number >= 0 else number*-2 for number in some_numbers]
#combinations = [[x, y] for x in [1,2,3] for y in [3,1,4] if x != y]

"""
for i in range(5):
    transposed.append([row[i] for row in matrix])
transposed = [[row[i] for row in matrix] for i in range(5)]
"""

#for key,value in goals_by_player.items():

