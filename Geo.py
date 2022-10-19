#funcion que ordena los numeros dependiendo de la opcion (op) seleccionada
def ordenamiento(lista,op):
    
    #realizamos una copia de los valores de la lista en otra lista que se usará para el traspaso de datos
    #hay que recordar que cuando se envía una lista a una funcion esta no realiza una copia local de la misma sino que la transfiere entera, de esta manera cualquier cambio en ella es realizado tambien en la lista original
    
    l = lista.copy()

    if op == 1:
        
        l.sort(reverse = True)
        return l

    else:

        l.sort()
        return l

#funcion de menú que devuelve la opcion elegida
def opcion():

    op_funcion = 0

    while True:

        print("""
        Ingrese la opcion deseada:
        -1- Ordenar numeros de mayor a menor
        -2- Ordenar numeros de menor a mayor
        """)
        op_funcion = int(input())

        if op_funcion == 1:

            print("Los numeros se ordenarán de mayor a menor")
            return op_funcion

        elif op_funcion == 2:

            print("Los numeros se ordenarán de menor a mayor")
            return op_funcion

        else:

            print("Ingrese una de las dos opciones válidas")

#Creacion de la lista en donde se guardarán los numeros
lista_local = []

#llamada a la funcion donde el usuario elige la opción
op_local = opcion()

while True:

    print("""
    Ingrese el numero que agregará a la lista
    o ingrese un caracter alfhabético para salír
    """)

    numero = input("numero: ")
    
    if numero.isnumeric() == True: #https://docs.python.org/es/3.9/library/stdtypes.html#str.isnumeric

        #convertimos el numero en tipo de dato numerico para que funcione correctamente el ordenamiento
        numero = int(numero)
        
        #comprobamos si el numero se encuentra en la lista utilizando el metodo count (de ser así no se agrega) https://docs.python.org/es/3.9/library/stdtypes.html#str.count
        if lista_local.count(numero) > 0:

            print("-El numero ingresado ya se encuentra en la lista-")
            print(lista_local)
        else:
            
            #Ingresamos el numero a la lista 
            lista_local.append(numero) #https://docs.python.org/es/3.9/library/stdtypes.html#mutable-sequence-types

            #Ordenamos la lista  y la mostramos
            lista_local = ordenamiento(lista_local,op_local)
            print(lista_local)
        
    else:

        print("La lista ha quedado de la siguiente manera: ")
        print("""
        ------------------------------------------
        {}
        ------------------------------------------
        """.format(lista_local)) #https://docs.python.org/es/3.9/library/stdtypes.html#str.format
        break
    



