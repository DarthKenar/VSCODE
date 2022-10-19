class Vehiculo:

    def __init__(self, color, ruedas):
        
        self.color = color
        self.ruedas = ruedas
    
    def __str__(self):

        return ( f" El Vehículo --> ruedas: {self.ruedas}, color: {self.color}, " )

class Coche(Vehiculo):

    def __init__(self, color, ruedas, velocidad, cilindrada):
        
        Vehiculo.__init__(self, color, ruedas)
        self.velocidad = velocidad
        self.cilindrada = cilindrada

    def __str__(self):
        
        return ( super().__str__()  + f" velocidad: {self.velocidad} Km/h, cilindrada: {self.cilindrada}cc" )

class Camioneta(Coche):

    def __init__(self, color, ruedas, velocidad, cilindrada, carga):

        Coche.__init__(self, color, ruedas, velocidad, cilindrada)    
        self.carga = carga

    def __str__(self):
        
        return ( super().__str__() + f", Tipo = Camioneta")  

class Bicicleta(Vehiculo):

    def __init__(self, color, ruedas, tipo):
        
        Vehiculo.__init__(self, color, ruedas)
        self.tipo = tipo
        #Como puedo hacer para que el atributo tipo admita solo dos tipos, deportiva o urbana.
    
    def __str__(self):

        return (super().__str__() + f" tipo: {self.tipo} ")

class Motocicleta(Bicicleta):

    def __init__(self, color, ruedas, tipo, velocidad, cilindrada):

        Bicicleta.__init__(self, color, ruedas, tipo)
        self.velocidad = velocidad
        self.cilindrada = cilindrada

    def __str__(self):

        return (super().__str__() + f" velocidad: {self.velocidad} km/h, cilindrada: {self.cilindrada}cc")

"""def catalogar(lista):
    for vehiculo in lista:

        print("-"*100)
        print(f"clase: { type(vehiculo).__name__ }, {vehiculo} ")
"""
def catalogar(lista):
    
    for vehiculo in lista:

        print(f"El vehiculo: {type(vehiculo).__name__} tiene {vehiculo.ruedas} ruedas.")

a = Coche("Azul",4,160,1200)
b = Camioneta("Roja",4,240,1900,4000) 
c = Bicicleta("Negro", 2, "urbana")
d = Motocicleta("Amarilla", 2, "deportiva", 320, 600)

vehiculos = [a, b, c, d]

catalogar(vehiculos)


