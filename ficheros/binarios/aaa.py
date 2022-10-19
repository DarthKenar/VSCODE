import pickle

diccionario = dict(uno = "1", dos = "2", tres = "3")
lista = [1,2,3]
variable = "hola"

with open("nada.pckl","wb") as archivo:
    pickle.dump(variable,archivo)

with open("nada.pckl","rb") as archivo:
    pickle.load(archivo)
    print(archivo)