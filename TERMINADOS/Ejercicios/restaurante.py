import sqlite3

def init_db():
    
    con = sqlite3.Connection("restaurante.db")
    cur = con.cursor()
    try:
        cur.execute('''
        CREATE TABLE categoria ( 
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        nombre VARCHAR(100) UNIQUE NOT NULL
        )
        ''')
        con.commit()
    except:
        print("La tabla categoría ya existe.")
    try:
        cur.execute('''
        CREATE TABLE plato (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        nombre VARCHAR(100) UNIQUE NOT NULL,
        categoria_id INTEGER NOT NULL,
        FOREIGN KEY(categoria_id) REFERENCES categoria(id)
        )
        ''')
        con.commit()
    except:
        print("La tabla plato ya existe.")
    con.close()

def add_category():

    #BUSCAR LA SOLUCION OPTIMA
    #LA SENTENCIA SQL NO ES LA OPTIMA, PORQUE METER LA CATEGORIA EN UNA LISTA?
    category = input("Ingrese el nombre de la categoría: ")
    category_list = []
    category_list.append(category)
    con = sqlite3.connect("restaurante.db")
    cur = con.cursor()

    try:
        cur.execute("INSERT INTO categoria VALUES (null,?)", category_list)
    except Exception as e:
        print(type(e).__name__)
    else:
        con.commit()
    finally:
        con.close()

add_category()