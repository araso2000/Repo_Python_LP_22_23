def get_value(item):
    return item[1]

def dicts2list(*diccionarios):
    resultado = []
    for dic in diccionarios:
        for i in dic.items():
            resultado.append((i[0],i[1]))
    sorted(resultado, key=get_value, reverse=False)
    print(resultado)

dicts2list ({'Pedro':10, 'Antonio':5}, {'Ana':7}, {'Pepe':0})