from typing import *
def inicializacion() -> None:
    
    try:    

        with open("contador.txt", "r") as contador:
            
            numero: int = int(contador.readline())
            print(f"El contador es: {numero}")

    except Exception as e:

        print("Error -->", type(e).__name__)
        print("El archivo contador.txt no existe, crearemos uno.")

        with open("contador.txt", "w+") as contador:

            contador.write("0")
            print("Contador inicializado en 0")

def inc_dec(valor: str) -> None: #incrementa o decrementa según "valor" dado por usuario

    if valor == "inc":
        
        try:

            with open("contador.txt", "r+") as contador:
                
                numero: int = int(contador.readline())
                print(f"Numero antes: {numero}, Numero despues: {numero + 1}")
                numero += 1
                
            with open("contador.txt", "w") as contador:
                
                contador.write(str(numero))
                
        except Exception as e:
            
            print("El cambio no ha podido realizarse --> Error: ", type(e).__name__)


    elif valor == "dec":

        try:

            with open("contador.txt", "r+") as contador:

                numero = int(contador.readline())
                print(f"Numero antes: {numero}, Numero despues: {numero + 1}")
                numero -= 1

            with open("contador.txt", "w") as contador:

                contador.write(str(numero))

        except Exception as e:

            print("El cambio no ha podido realizarse --> Error: ", type(e).__name__)

    else:

        inicializacion()

while True:

    inicializacion()
    valor : int = int(input("Ingrese la opción deseada: \n1 - Incrementar\n2 - Decrementar\n3 - Salir\n"))
    
    if valor == 1:
    
        inc_dec("inc")
        
    
    elif valor == 2:
    
        inc_dec("dec")
        
    
    else:   
        inicializacion()
        break
