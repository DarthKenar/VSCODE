import sqlite3


class Personaje:

    nombre : str
    vida : int
    ataque : int
    defensa : int 
    alcance : int

    personaje_info : dict = dict(nombre= "", vida = 0, ataque = 0, defensa = 0, alcance = 0)

    def __init__(self, nombre : str, vida: int, ataque: int, defensa: int, alcance: int) -> None:

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

    @staticmethod
    def build_db() -> None: #Crea el archivo ingresando una lista vacía en él

        try:
            con = sqlite3.connect("personajes.db")
            cur = con.cursor()
            cur.execute("CREATE TABLE personajes (id INTEGER PRIMARY KEY AUTOINCREMENT, nombre VARCHAR(50) NOT NULL,vida INTEGER NOT NULL,ataque INTEGER NOT NULL, defensa INTEGER NOT NULL, alcance INTEGER NOT NULL)")
            con.commit()
            cur.close()
        except sqlite3.OperationalError:
            print("La tabla ya existe")
            cur.close()

    @staticmethod
    def mostrar_pj() -> None: #Muestra todos los personajes
            Gestor.build_db()
            con = sqlite3.connect("personajes.db")
            cur = con.cursor()
            cur.execute("SELECT * FROM personajes")
            personajes = cur.fetchall()
            for personaje in personajes:
                print(personaje)

            cur.close()
        

    @staticmethod
    def añadir_pj(personaje_info : dict) -> None: #añade el personaje creado a la DB
        personaje_info_list : list = []
        #subprograma transforma dic en list
        for key, value in personaje_info.items():
            print(f"{key}: {value}")
            personaje_info_list.append(value)
        
        con = sqlite3.connect("personajes.db")
        cur = con.cursor()
        cur.execute("INSERT INTO personajes VALUES(null,?,?,?,?,?)", personaje_info_list)
        con.commit()
        cur.close()

    @staticmethod
    def borrar_pj(nombre): #borra por nombre
        pass

                    
Gestor.mostrar_pj()