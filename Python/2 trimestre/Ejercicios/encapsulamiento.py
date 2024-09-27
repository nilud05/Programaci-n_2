class Persona: 
    def __init__(self,nombre,edad,nacionalidad):
        self._nombre = nombre
        self._edad = edad
        self._nacionalidad = nacionalidad

personal = Persona("lisbeth",32,"Colombiana")
print(personal)