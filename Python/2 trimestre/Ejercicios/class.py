class X:
    def __init__(self, a , b):
        self.a = a
        self.b = b
    
    def sumar(self):
        return f"la suma es: {self.a + self.b}"
    
class Y():
    def __init__(self, c):
        self.c = c

class Z(X,Y):
    def __init__(self, a,b,c,d):
        X.__init__(self,a,b)
        Y.__init__(self,c)
        self.d = d

    def sumartodos(self):
        return f"la suma total es: {self.a + self.b + self.c + self.d}"

xyz1 = Z(1, 2, 3, 4)

print(xyz1.sumartodos())