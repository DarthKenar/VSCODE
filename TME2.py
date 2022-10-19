#Entrada de datos:
#puntaje del item
#Tipo de concepto
#Salidas:
#Puntaje bruto por concepto
#Puntaje total
#Referencia de interpretacion (6)
from ast import While
from enum import auto
def totales(valores):
    total_cf = 0
    total_vf = 0
    total_a = 0
    total_sv = 0
    confianza_fundamental = (1,2,3,4,10,12,13,22,24,25,32,33,41,54)
    valor_fundamental = (16,18,20,23,28,30,31,35,39,46,48,49,51,53)
    autoestima = (5,7,8,9,11,14,15,17,26,29,36,38,42,43)
    sentido_de_vida = (6,19,21,27,34,37,40,44,45,47,50,52,55,56)
    for i in valores:
        if i in confianza_fundamental:

            total_cf += i

        elif i in valor_fundamental:

            total_vf += i

        elif i in autoestima:

            total_a += i

        elif i in sentido_de_vida:

            total_sv += i

    total = total_cf + total_sv + total_vf + total_a
    print("El total de puntaje es: ",(total))
    print("El total de confianza fundamental es: ", total_cf)
    print("El total de valor fundamental es: ", total_vf)
    print("El total de autoestima es: ", total_a)
    print("El total de sentido de vide es: ", total_sv)
    lista = [total_cf,total_vf,total_a,total_sv]
    return lista

def comprobacion_inverse(i, desicion, valores):
    invertidos = (4,10,13,24,25,32,33,54,16,18,20,30,31,53,7,8,14,15,38,43,19,21,27,37,40,45,47,52)
    if i in invertidos:
        if desicion == 1:
            desicion = 6
        elif desicion == 2:
            desicion = 5
        elif desicion == 3:
            desicion = 4
        elif desicion == 4:
            desicion = 3
        elif desicion == 5:
            desicion = 2
        elif desicion == 6:
            desicion = 1
    valores.append(desicion)
    return valores
    
def salida(list):
    for i,j in enumerate(list):
        if i == 0:
            print("Referencia de la confianza fundamental: ")
        elif i == 1:
            print("Referencia del valor fundamental: ")
        elif i == 2:
            print("Referencia del autoestima: ")
        elif i == 3:
            print("Referencia del sentido de vida:")
        
        if j <= 10:
            print("referencia: Muy bajo")
            print("interpretacion: Zona de bloqueo")
        elif j >= 11 and j <= 25:
            print("referencia: bajo")
            print("interpretacion: Reacciones automaticas")
        elif j >= 26 and j <= 40:
            print("referencia: promedio bajo")
            print("interpretacion: Actividad existencial intermedia")
        elif j >= 41 and j <= 60:
            print("referencia: promedio")
            print("interpretacion: Actividad existencial intermedia")
        elif j >= 61 and j <= 74:
            print("referencia: promedio alto")
            print("interpretacion: Orientacion hacia el logro")
        elif j >= 75 and j <= 89:
            print("referencia: alto")
            print("interpretacion: logro existencial")
        elif j >= 90:
            print("referencia: muy alto")
            print("interpretacion: plenitud existencial")
        print("-----------------------------------------") 






valores = []

for i in range(56):
    print("pregunta n°", i+1)
    print("Señala tu posicion: ")
    print("""
    (1) - De acuerdo
    (2) - Parcialmente de acuerdo
    (3) - Indeciso, pero más bien de acuerdo
    (4) - Indeciso, pero más bien en desacuerdo
    (5) - Parcialmente en desacuerdo
    (6) - En desacuerdo
    """)
    desicion = int(input("Respuesta: "))
    print("-----------------------------------------------------------")
    
    valores = comprobacion_inverse(i, desicion, valores)
    totales(valores)

lista = totales(valores)
salida(lista)
while True:
    for i,j in enumerate(valores):
        print("valor", i+1, " - ", j)

    print("Desea cambiar algún valor?: s/n")
    print("escribe's' para sí o 'n' para no (salir y mostrar resultados).")
    opcion = input("opcion: ")
    
    if opcion == "s":
        print("¿Que valor puntaje desea cambiar?")
        cambiar = int(input("indice n°: "))
        print("Para el indice n° ", cambiar)
        print("Elija un valor de respuesta: ")
        valorcambiar = int(input("valor: "))
        #comienza proceso de cambio
        valores[cambiar-1] = valorcambiar

        #REALIZAR LLAMADAS DE IMPRESION
        valores = comprobacion_inverse(cambiar, valorcambiar, valores)
        totales(valores)

        lista = totales(valores)
    elif opcion == "n":
        break
    else:
        print("Escribe una opcion correcta.")
    #IMPRIMIR TODAS LAS RESPUESTAS