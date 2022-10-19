import sys as cmd


try:
    numero_str = str(cmd.argv[1])
    longitud = len(numero_str)
    for i,j in enumerate(numero_str):
        print({}.format(i, j))
    
     
except:
    print("Debe ingresar un argumento que sea un entero positivo")	

finally:
    print("Gracias por utilizar el script - 'Tabla Random'")

