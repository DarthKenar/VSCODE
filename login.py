
class Accounts:
    
    #acc (hace referencia a la cuenta) Diccionario (atributo de clase)
    acc = {}

    #metodo constructor 
    def __init__(self):

        #uss (hace referencia al nombre de usuario) variable
        #pss (hace referencia a la contraseña password) variable    
        uss = input("Ingrese el usuario: ")
        pss = input("Ingrese la contraseña: ")
        self.acc[uss] = pss

    def mostrar(self):

        for i in self.acc:

            print("Nombre de usuario: ", i, " - Contraseña: ", self.acc[i])

    def entrar(self, acc, nombre, contraseña):

        encontrado = False

        for i in self.acc:

            if i == nombre:

                encontrado == True
                objeto = i
                
        if encontrado == True:

            print("- Nombre de usuario encontrado -")
            if self.acc[objeto] == contraseña:

                print("Contraseña correcta")
                print("Ingresando al sistema...")

        else: 

            print("- El nombre de usuario no se encuentra en el registro")

while True:

    try:

        op = int(input(""" 
        Ingrese la opcion deseada:
        1) Registrarse
        2) Consultar registro
        """))

    except ValueError:

        print("Ingrese una opcion válida...")
        pass
    
    try:

        if op == 1:

            acc = Accounts()

        elif op == 2:

            acc.mostrar()
            
        else:
            print("Saliendo del sistema")
            break

    except NameError:
        
        print("No hay usuarios en el registro temporal")
        