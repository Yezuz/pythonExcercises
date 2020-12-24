from abc import ABCMeta, abstractmethod


class FiguraRegular:
    
    __metaclass__ = ABCMeta
    __nombreClase = "FiguraRegular"
    
    def __init__(self, area, lado = 3):
        self.lado = lado
        self.__area = area 
        print('Se mando a llamar el metodo __init__ de la clase: ' + self.__nombreClase)

    def get_area(self): return self.__area

    def get_nombre_clase(self): return __nombreClase
    

    @abstractmethod
    def calcularArea(self): pass


class Triangulo(FiguraRegular):

    def __init__(self, base, altura):
        self.base = base
        self.altura = altura
        self.__area = self.calcularArea()
        super().__init__(self.__area)
    
    def calcularArea(self): 
        return float(self.base * self.altura) / 2


t = Triangulo(3, 4)
print(t.get_area())

