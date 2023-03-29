def listaATupla(lista):
    indexed_data = [(i+1, lista[i]) for i in range(len(lista))]
    return indexed_data

print(listaATupla(["examen", "de", "python"]))