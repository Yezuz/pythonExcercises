class Automovil:
    def __init__(self, tipoForma = "sedan", combustible = "gasolina", tipoTransmision = "automatico", sistemaDeEncendido = "inyeccion"):
        self.tipoForma = tipoForma
        self.combustible = combustible
        self.tipoTransmision = tipoTransmision
        self.sistemaDeEncendido = sistemaDeEncendido

    def __str__(self):
        return str(self.__class__) + ": " + str(self.__dict__)
        
    def encendidoMotor(self):
        print("arrancando motor utilizando " + self.sistemaDeEncendido + "con " + self.combustible + " como combustible")

    def acelerar(self):
        print("aumentando velocidad...")

celica = Automovil()
CRV = Automovil("camioneta", "electrico", "" , "inyeccionElectrica")


print(celica)
print(CRV)
