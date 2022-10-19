class Persona:
    personas = []
    def __init__(self, id, nombre):
        self.id = id
        self.nombre = nombre
class Profesional:
    def __init__(self, id, nombre, dni, especialidad = None):
        self.id = id
        self.nombre = nombre
        self.dni = dni
        self.especialidad = especialidad
a = Profesional(1,"Pedro","23332123")
b = Profesional(2,"Ricardo","1231233")
for i in Profesional:
    print(i)

