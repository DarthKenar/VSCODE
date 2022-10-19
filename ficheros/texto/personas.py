from datetime import date
import io


personas = []
with open("personas.txt", "r",encoding="utf-8") as archivo:

    lineas = archivo.readlines()

    for linea in lineas:
        
        datos = linea.split(";") 
        diccionario = dict( id = datos[0], name = datos[1], last_name = datos[2], date = datos[3])
        personas.append(diccionario)
        
    print(personas)

for persona in personas:
    print("Id: "+ persona["id"] + ", Nombre: " + persona["name"] + ", Apellido: " + persona["last_name"] + ", Fecha: " + persona["date"])