
class Usuario:

    nickname = "Nombre de usuario"
    password = "Contraseña de usuario"
    admin = False

    def __init__(self,nickname,password,admin = False):

        if len(password) < 8 or password.isalpha() == True or password.islower() == True:

            print("""
            ¡Invalid password! - please enter a valid password
            La contraseña, por mayor seguridad, debe cumplir con las siguientes condiciones:
                -Debe contener al menos 8 caracteres
                -Debe contener al menos 1 letra mayúscula
                -Debe contener al menos 1 caracter no alfabético (numero o símbolo)
            """)
        else:
            
            self.nickname = nickname
            self.password = password
            self.admin = admin

#u = Usuario("DarthKenar","locomoco22")
while True:
    print("""Ingrese la opcion deseada: 
    1 - Registrarse en el sistema
    2 - Salir
    """)
    opcion = input("opcion: ")
    if opcion == "1":
        print("")
        usuario = input("Nombre de Usuario: ")
        contraseña = input("Contraseña: ")
        u = Usuario(usuario,contraseña)
    else:
        break
print(Usuario)





