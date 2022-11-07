import sys


try:
    
    argumento_1 = int(sys.argv[1])
    argumento_2 = int(sys.argv[2])
    if argumento_1 > 1 and argumento_1 < 10 and argumento_2 > 1 and argumento_2 < 10:
        for i in range(argumento_1):
            for j in range(argumento_2):
                print(" * ",end = "")
            print(" ")
    else:

        print("Debe ingresar dos argumentos que sean mayores a 0 y menores a 10.")
except:
    print("Debe ingresar dos argumentos como cadenas de texto, mayores a 0 y menores a 10")	

finally:
    print("Gracias por utilizar el script - 'Tabla Random'")
