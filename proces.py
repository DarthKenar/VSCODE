def recortar(lista):
    if len(lista) > 2:
        lista = lista[1:-1]
        return lista
    else:
        return None
    
calculos = [666,1,5,10,20,30,40,23,50,10,50,7,666]
nombre = "pependEnt"
recortar(calculos)
print(calculos)
calculos.sort()
print (calculos)
nombre = nombre.capitalize()
print (nombre)

