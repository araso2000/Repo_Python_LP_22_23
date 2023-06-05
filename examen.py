#Ejercicio 1
ventas = {
    'tienda1': [('producto1', 10, 3), ('producto2', 20, 2), ('producto3', 30, 1)],
    'tienda2': [('producto1', 5, 2), ('producto2', 10, 4), ('producto3', 15, 1)],
    'tienda3': [('producto1', 15, 1), ('producto2', 30, 3), ('producto3', 45, 2)]
}

def calcular_total(diccionario):
    resultado = []
    for key,value in diccionario.items():
        suma = 0
        for lista in value:
            for tupla in lista:
                try:
                    if len(tupla) > 1:
                        pass
                except:
                    suma = suma + tupla
        resultado.append((key,suma))
    return(resultado)

print((calcular_total(ventas)))

#Ejercicio 2
def preproceso_tuits(*args):
    tupla = []
    for tuit in args:
        texto = ""
        for palabra in tuit.split():
            if palabra[0] not in "@#":
                texto = texto + palabra + " "
        tupla.append(texto.lower()[:-1])
    return(tuple(tupla))

#print(preproceso_tuits ('@antonio enhorabuena por el PAPER', 'muy buen trabajo en equipo #equipazo', 'VAMOS A POR EL SIGUIENTE @antonio #seguimos'))

#Ejercicio 3
class Empleado:
    def __init__(self,nombre,apellido,salario):
        self.nombre = nombre
        self.apellido = apellido
        self.salario = salario

    @classmethod
    def from_string(self,cadena):
        cadena.split("-")
        nuevoEmpleado = Empleado(cadena[0],cadena[1],cadena[2])
        return(nuevoEmpleado)

objeto = Empleado()
objeto.from_string("nombre-apellido-salario")
print(objeto)