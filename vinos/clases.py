
class Vinos:
    
    nombre = ""

    cuerpo = None
    dulzor = None
    taninos = None
    acidez = None
    alcohol = None

class Blanco(Vinos):

    comidas = dict(vegetales=False, vegetales_asados=False, Masas_panes = False, pescados=False, quesos_suaves=False, quesos_maduros=False, embutidos=False, postres=False, mariscos=False, aves=False)
    

class Blanco_seco(Blanco):
    
    
    comidas = dict(vegetales=True, vegetales_asados=True, Masas_panes = True, pescados=True, quesos_suaves=False, quesos_maduros=False, embutidos=False, postres=False, mariscos=False, aves=False)

    def __init__(self, nombre, cuerpo, dulzor, taninos, acidez, alcohol):
        
        self.nombre = nombre
        self.cuerpo = cuerpo
        self.dulzor = dulzor
        self.taninos = taninos
        self.acidez = acidez
        self.alcohol = alcohol
    
    def __str__(self):

        print(f"Nombre: {self.nombre}\nCuerpo: {self.cuerpo}Dulzor: {self.dulzor}Taninos: {self.taninos}Acidez: {self.acidez}Alcohol: {self.alcohol}")
    

class Blanco_dulce(Blanco):
    
    comidas = dict(vegetales=False, vegetales_asados=False, Masas_panes = False, pescados=False, quesos_suaves=True, quesos_maduros=True, embutidos=True, postres=True, mariscos=False, aves=False)

class Blanco_rich(Blanco):
    
    comidas = dict(vegetales=False, vegetales_asados=False, Masas_panes = True, pescados=True, quesos_suaves=True, quesos_maduros=False, embutidos=False, postres=False, mariscos=True, aves=True)

