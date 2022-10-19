import pickle

class Personaje:

    personaje_info = dict(nombre = "", vida = 0, ataque = 0, defensa = 0, alcance = 0)

    def __init__(self, nombre, vida, ataque, defensa, alcance):

        if vida > 0 and ataque > 0 and defensa > 0 and alcance > 0:
            
            #cada clase de personaje estará dentro de un diccionario
            self.personaje_info["nombre"] = nombre
            self.personaje_info["vida"] = vida
            self.personaje_info["ataque"] = ataque
            self.personaje_info["defensa"] = defensa
            self.personaje_info["alcance"] = alcance

            print("-"*100)
            print("El personaje cargado tiene las sigientes caracteristicas:")

            for i in self.personaje_info:

                print(f"{i}: {self.personaje_info[i]}")

        
        else:

            print("El personaje no fué creado, alguno de sus atributos no es positivo")

class Gestor:

    def build_file_pckl(): #Crea el archivo ingresando una lista vacía en él
            
            lista_vacia = []
            pckl_file = open("personajes.pckl","wb")
            pickle.dump(lista_vacia,pckl_file)
            pckl_file.flush() #fuerza la entrada de los datos modificados al archivo antes de q este se cierre (en este caso no cumple ninguna función, es una muestra de ejemplo)
            
            print("Archivo creado")

            pckl_file.close()

    def mostrar_pj(): #Muestra todos los personajes
        
        try:

            with open("personajes.pckl","rb") as pckl_file: 

                lista_pj_dict = pickle.load(pckl_file)
                for indice, pj in enumerate(lista_pj_dict): #Bucle que mostrará los personajes de la lista
                    
                    print(indice)
                    print(pj)
                    
        except FileNotFoundError:

            print("El archivo no existe!")

            Gestor.build_file_pckl()
        
        except EOFError as e:

            print("El archivo se encuentra vacío")

            Gestor.build_file_pckl()
    
    def añadir_pj(personaje_info): #añade el personaje creado a la DB

        try:

            with open("personajes.pckl","rb") as pckl_file:

                lista_pj_dict = pickle.load(pckl_file) 
                lista_pj_dict.append(personaje_info) #Ingresa al tipo de personaje que esta en formato dict a la lista q está dentro del archivo

                print("Datos obtenidos")

            with open("personajes.pckl","wb") as pckl_file:

                pickle.dump(lista_pj_dict,pckl_file)

                print("Personaje añadido correctamente")

        except FileNotFoundError as e:

            print("El archivo no existe!")

            Gestor.build_file_pckl()

        except EOFError as e:
            
            print("El archivo se encuentra vacío")

            Gestor.build_file_pckl()

    def borrar_pj(nombre): #borra por nombre

        try:

            pckl_file = open("personajes.pckl", "rb")
            lista_pj_dict = pickle.load(pckl_file)
            pckl_file.close()

            print("Datos obtenidos")

        except FileNotFoundError as e:

            print("El archivo no existe!")

            Gestor.build_file_pckl()

        except EOFError as e:
            
            print("El archivo se encuentra vacío")

            Gestor.build_file_pckl()

        except Exception as e:
            
            print("Error --> ", type(e).__name__)
            print("No se pudo leer el archivo")
        
        else:
            
            for indice, pj in enumerate(lista_pj_dict): #continúa la eliminacion del objeto
                
                if pj["nombre"] == nombre:
                    lista_pj_dict.pop(indice)

                    print("Clase de personaje encontrado!")
                
            with open("personajes.pckl","wb") as pclk_file:
                pickle.dump(lista_pj_dict,pclk_file)

                print("Clase de personaje eliminado!")

#Gestor.build_file_pckl()
Gestor.mostrar_pj()
primer_pj = Personaje("Caballero", 4, 2, 4, 2) 
Gestor.añadir_pj(primer_pj.personaje_info)
Gestor.mostrar_pj()
primer_pj = Personaje("Guerrero", 2, 4, 2, 4)
Gestor.añadir_pj(primer_pj.personaje_info)
primer_pj = Personaje("Arquero", 2, 4, 1, 8)
Gestor.añadir_pj(primer_pj.personaje_info)
Gestor.mostrar_pj()
Gestor.borrar_pj("Arquero")
Gestor.mostrar_pj()


            
        
                    





                




    

        
                
                


