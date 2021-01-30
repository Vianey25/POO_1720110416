class Cajero_Automatico():
    
    '''
    Atributos
    '''
    marca  = None
    lugar   = None
    establecimiento = None
    colores = None
    tamaño = None
    funcionamiento  = None
    tiempo_de_funcionamiento = None
    modelo = None
    almacenamiento = None
    sistema_operativo = None
    
    

    def __init__(self):
        print("clase Cajero_Automatico")
    
    '''
    Metodos
    '''
    
    def prender(self):
        print("Metodo encender")
    
    def apagar(self):
        print("Metodo apagar")

    def recibir(self):
        print("Metodo recibir")

    def trabajar(self):
        print("Metodo trabajar")

    def guardar(self):
        print("Metodo guardar")
   

# Creacion de un objeto basado en una clase
cajero = Cajero_Automatico()

# Asiganacion de valores a las propiedades
cajero.marca = "CitiBanamex"
cajero.lugar = "Tulancingo Hgo"
cajero.establecimiento = "BBVA"
cajero.colores = "Azul y blanco"
cajero.tamano = "Grande"
cajero.funcionamiento = "Bueno"
cajero.tiempo_de_funcionamiento = "15 años"
cajero.modelo = "SXK11"
cajero.almacenamiento = "si"
cajero.sistema_operativo = "Windows XP"


# Imprimir valores de las propiedades
print(cajero.marca)
print(cajero.lugar)
print(cajero.establecimiento)
print(cajero.colores)
print(cajero.tamano)
print(cajero.funcionamiento)
print(cajero.tiempo_de_funcionamiento)
print(cajero.modelo)
print(cajero.modelo)
print(cajero.sistema_operativo)

# Invocar metodos de la clase
cajero.prender()
cajero.apagar ()
cajero.recibir ()
cajero.trabajar ()
cajero.guardar ()

