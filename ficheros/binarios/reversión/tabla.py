from multiprocessing import connection
import sqlite3
connection : object = sqlite3.connect("registro.db")

cursor = connection.cursor()

#cursor.execute("CREATE TABLE usuarios (id INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL, usuario VARCHAR(50) NOT NULL, edad INTEGER NOT NULL, email VARCHAR(255) NOT NULL)") #Consulta en formato SQL
cursor.execute("INSERT INTO usuarios (usuario, edad, email) VALUES ('Ricardo',32,'ricardovich@hotmail.com')")
connection.commit()
connection.close()