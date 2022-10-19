
import pickle

class Caballos:
    
    __nombre = None
    __tipo = None


    def __init__(self, nombre, tipo):

        self.__nombre = nombre
        self.__tipo = tipo

    def __str__(self) -> str:
        return f"El nombre es: {self.__nombre} y tipo: {self.__tipo}"
    def get_nombre(self):
        return self.__nombre
    def get_tipo(self):
        return self.__tipo
    def set_nombre(self, nombre):
        self.__nombre = nombre
    def set_tipo(self, tipo):
        self.__tipo = tipo
    
    @classmethod
    def guardar(cls):

       
        try:
            caballos = open("users.pckl","wb")
            datos = f"Nombre: {cls.get_nombre},Tipo: {cls.get_tipo}".split(",")
            pickle.dump(datos,caballos)
        except:
            print("Los datos no fueron guardados.")
        else:
            print("Los datos fueron guardados correctamente.")
        finally:
            caballos.close()
            del(caballos)
    @staticmethod  
    def mostrar():
        try:
            archivo = open("users.pckl", "rb")
            archivo_lineas = pickle.load(archivo)
            print(archivo_lineas)
        except:
            print("No se pudo leer el archivo")
        finally:
            archivo.close()
            del(archivo)
        

a = Caballos("Pedro","Alazhan")

print(a)
a.set_nombre("Carolo")
print(a)
Caballos.guardar()

caballos2 = open("users.pckl","wb")
datos = "Nombre: ,Tipo: "
pickle.dump(datos,caballos2)
caballos2.close()
archivo2 = open("users.pckl", "rb")
archivo_lineas2 = pickle.load(archivo2)
print(archivo_lineas2)
archivo2.close()