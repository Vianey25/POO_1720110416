class Calculadora():
    
    '''
    Atributos
    '''
    marca  = None
    color   = None
    tipo_de_calculadora = None
    tamano = None
    tipo_de_corriente = None
    fabricacion  = None
    modelo = None
    material = None
    lenjuage = None
    

    def __init__(self):
        print("clase calculadora")
    
    '''
    Metodos
    '''
    
    def prender(self):
        print("Metodo encender")
    
    def apagar(self):
        print("Metodo apagar")

    def trabajar(self):
        print("Metodo trabajar")

    def calcular(self):
        print("Metodo calcular")

    def resultar(self):
        print("Metodo resultar")
   

# Creacion de un objeto basado en una clase
cientifica  = Calculadora()

# Asiganacion de valores a las propiedades
cientifica.marca = "Casio"
cientifica.color = "Negro"
cientifica.tipo_de_calculadora = "Cientifica"
cientifica.tamano = "Mediana"
cientifica.tipo_de_corriente = "Electrica atravez de las pilas"
cientifica.fabricacion = "si"
cientifica.modelo = "FX-991SPX II"
cientifica.material = "plastico"
cientifica.lenjuage = "TI-Basic"

# Imprimir valores de las propiedades
print(cientifica.marca)
print(cientifica.color)
print(cientifica.tipo_de_calculadora)
print(cientifica.tamano)
print(cientifica.tipo_de_corriente)
print(cientifica.fabricacion)
print(cientifica.modelo)
print(cientifica.material)
print(cientifica.lenjuage)

# Invocar metodos de la clase
cientifica.prender ()
cientifica.apagar ()
cientifica.trabajar ()
cientifica.calcular ()
cientifica.resultar ()
