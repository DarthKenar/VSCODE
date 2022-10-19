import this
from math import sqrt as raiz
def linea():
    print(f"-"*100)

class Punto:

    def __init__(self, x = 0, y = 0):

        self.x = x
        self.y = y

    def __str__(self):


        return (f"( {self.x} , {self.y} )")
    
    def cuadrante(self):

        if self.x > 0 and self.y > 0:

            print(f"{self}, Se encuentra en el primer cuadrante")

        elif self.x < 0 and self.y > 0:

            print(f"{self}, Se encuentra en el segundo cuadrante")

        elif self.x < 0 and self.y < 0:

            print(f"{self}, Se encuentra en el tercer cuadrante")

        elif self.x > 0 and self.y < 0:


            print(f"{self}, Se encuentra en el cuarto cuadrante")

        elif self.x == 0 and self.y == 0:

            print(f"{self}, El punto se encuentra en el eje de coordenadas")

        elif self.y == 0:

            print(f"{self}, El punto se encuentra sobre el eje y")

        elif self.x == 0:

            print(f"{self}, El punto se encunetra sobre el eje x")

    def vector(self,punto):

        print(f"El vector resultante es: ( {self.x - punto.x} , {self.y - punto.y} )")
    
    def distancia(self, punto):

        print(f"La distancia entre el punto: {self} y {punto} es:  { raiz( ( ( punto.x - self.x)**2 + ( punto.y - self.y)**2 ) ) }")
        return raiz( ( ( punto.x - self.x)**2 + ( punto.y - self.y)**2 ) )

class Rectangulo():

    def __init__(self, punto_inicial, punto_final):

        self.punto_inicial = punto_inicial
        self.punto_final = punto_final

    def base(self):
        
        self.base = abs( self.punto_inicial.x - self.punto_final.x )
        print(f"La base del rectangulo es: { abs( self.punto_inicial.x - self.punto_final.x ) }")
        

    def altura(self):

        self.altura = abs( self.punto_inicial.y - self.punto_final.y )
        print(f"La altura del rectangulo es: { abs( self.punto_inicial.y - self.punto_final.y ) }")
        
    def area(self):

        print(f"El area del rectangulo es: { self.base * self.altura }")

A  = Punto(2,3)
B = Punto(5,5)
C = Punto(-3,-1)
D = Punto(0,0)

linea()
linea()

print(f"{A}\n{B}\n{C}\n{D}\n")

linea()

A.cuadrante()
B.cuadrante()
C.cuadrante()
D.cuadrante()

linea()

A.vector(B)
B.vector(A)

linea()

A.distancia(B)
B.distancia(A)

linea()

mayor = [A.distancia(D),B.distancia(D),C.distancia(D)]

linea()

mayor.sort()
print(f"El punto mas lejos del punto de origen es: {mayor[-1]}")

linea()

forma = Rectangulo(A,B)
forma.altura()
forma.base()
forma.area()
