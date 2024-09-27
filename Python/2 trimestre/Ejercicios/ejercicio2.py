class Persona:
    def __init__ (self, nombre, edad, estrato):
        self.__nombre = nombre
        self.__edad = edad
        self.__estrato = estrato

class Vendedor(Persona): 
    def __init__(self, nombre, edad, estrato, venta, comision):
        Persona.__init__ (self, nombre, edad, estrato)
        self.__venta = venta
        self.__comision = comision
        self.cambiar_comision()
    
    @property
    def comision(self):
        return self.__comision
    
    @property
    def venta(self):
        return self.__venta

    @comision.setter
    def comision(self, nueva_comision):
        self.__comision = nueva_comision
    
    def cambiar_comision(self):
        if self.__venta > 5000:
            self.__comision = 0.11
    
l1 = Vendedor("Juan", 30, 3, 7000, 0.08)

print(l1.comision)
