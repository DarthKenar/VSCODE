from Gestor import *
while True:

    
    print("Opciones:\n1) Crear\n2) Borrar\n3) Mostrar\n")
    op : int = int(input(""))
    if  op == 1:
        nombre : str = input("Nombre: ")
        vida : int = int(input("Vida: "))
        ataque : int = int(input("Ataque: "))
        defensa : int = int(input("Defensa: "))
        alcance : int = int(input("Alcance: "))
        pj = Personaje(nombre,vida,ataque,defensa,alcance)
        Gestor.añadir_pj(pj.personaje_info)


    elif op == 2:

        try: 

            nombre = input("Ingrese el nombre del personaje a borrar: ")
            Gestor.borrar_pj(nombre)

        except Exception as e:

            print(f"Error: {type(e).__name__}")
            continue

    elif op == 3:

        Gestor.mostrar_pj()

    else:

        break