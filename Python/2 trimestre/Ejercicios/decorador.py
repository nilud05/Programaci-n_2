class Persona:
    def __init__(self, nombre, edad, nacionalidad):
        self.__nombre = nombre
        self.__edad = edad
        self.__nacionalidad = nacionalidad

    @property
    def nombre(self):
        return self.__nombre
    
    @nombre.setter
    def nombre(self, nuevo_nombre):
        self.__nombre = nuevo_nombre

p1 = Persona("Julia", 30, "Colombiano")

print(p1.nombre)
p1.nombre= "Lucia"

print(f"El nuevo nombre es: {p1.nombre}")