


def ordenar (lista):
    lista2 = lista.copy()
    lista2.sort()
    return lista2

lista = ['8', '7', '651', '6', '5', '4', '321', '2', '19', '18', '17', '16', '153', '15', '14', '136', '131', '13', '123', '12', '11', '10', '1', '00']
print(lista)
print(ordenar(lista))
lista.append(2)
print(lista)