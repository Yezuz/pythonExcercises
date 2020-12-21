class FiguraRegular:
    
    def __init__(self, lado = 3, base = 1):
        self.lado = lado
        self.__area = 0
        self.base = base
        self.verArea()
        self.__calcularArea()

    def verArea(self):
        return self.__area

    def calcularArea(self):
        __area = (base * altura) / 2

    __calcularArea = calcularArea


class Cuadrado(FiguraRegular):

    def __init__(self, lado, base):
        self.lado = lado
        self.base = base

    def calcularArea(self):
        __area = (base * base)


cuadrado1= Cuadrado(4, 2)
cuadrado1.calcularArea()
print(int(cuadrado1.verArea()))
