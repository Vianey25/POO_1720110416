class Coche():
    
    '''
    Atributos
    '''
    color  = None
    marca   = None
    número_de_serie = None
    máxima_velocidad = None
    motor = None
    frenos  = None
    transmisión = None
    tipo_de_combustible = None
    kilometraje = None
    quemacocos = None

    def __init__(self):
        print("clase Coche")
    
    '''
    Metodos
    '''
    
    def encender(self):
        print("Metodo encender")
    
    def apagar(self):
        print("Metodo apagar")

    def acelerar(self):
        print("Metodo acelerar")

    def frenar(self):
        print("Metodo frenar")

    def transportar(self):
        print("Metodo transportar")
   

# Creacion de un objeto basado en una clase
vocho  = Coche()

# Asiganacion de valores a las propiedades
vocho.color = "Blanco"
vocho.marca = "volkswagen"
vocho.numero_de_serie = "5lk3m"
vocho.maxima_velocidad = "165km/h"
vocho.motor = "1 motor"
vocho.frenos = "si"
vocho.transmision = "trasera manual 4 velocidades"
vocho.tipo_de_combustible= "Gasolina"
vocho.kilometraje = "si"
vocho.quemacocos = "si"


# Imprimir valores de las propiedades
print(vocho.color)
print(vocho.marca)
print(vocho.numero_de_serie)
print(vocho.maxima_velocidad)
print(vocho.motor)
print(vocho.frenos)
print(vocho.transmision)
print(vocho.tipo_de_combustible)
print(vocho.kilometraje)
print(vocho.quemacocos )

# Invocar metodos de la clase
vocho.encender ()
vocho.apagar()
vocho.acelerar()
vocho.frenar ()
vocho.transportar()
