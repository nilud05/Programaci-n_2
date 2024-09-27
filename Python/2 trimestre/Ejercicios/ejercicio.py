class PERSONA:
    def __init__(self,nombre,edad,nacionalidad):
        self.nombre = nombre
        self.edad = edad
        self.nacionalidad = nacionalidad

class EMPLEADO:
    def __init__(self, sucursal, salario):
        self.sucursal = sucursal
        self.salario = salario

class PLANTA(PERSONA,EMPLEADO):
    def __init__(self, nombre, edad, nacionalidad, sucursal, salario, bono, saldo_h_extras, desc_seguridad):
        PERSONA.__init__(self, nombre, edad, nacionalidad)
        EMPLEADO.__init__(self, sucursal, salario)
        self.bono = bono
        self.saldo_h_extras = saldo_h_extras
        self.desc_seguridad = desc_seguridad

    def calcular_salario_neto(self):
        return (self.salario + self.bono * self.saldo_h_extras) - self.desc_seguridad

class CONTRATISTA(PERSONA,EMPLEADO):
    def __init__(self, nombre, edad, nacionalidad, sucursal, salario, retefuente):
         PERSONA.__init__(self, nombre, edad, nacionalidad)
         EMPLEADO.__init__(self, sucursal, salario)
         self.retefuente = retefuente

    def calcular_salario_contra(self):
        return self.salario * 0.97

planta = PLANTA("Danitzha", 18, "Colombiana", "jsdxjsjx", 2432000, 780, 2111, 4300)
contratista = CONTRATISTA("Lucia", 23, "Rusa", 343, 34240000, "hshchs")

print(f"El de planta es: {planta.nombre}, y su salario es: {planta.calcular_salario_neto()}")
print(f"El contratista es: {contratista.nombre}, y su salario es: {contratista.calcular_salario_contra()}")