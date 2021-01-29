class Banco():
    
    '''
    Atributos
    '''
    lugar = None
    comapania = None
    clientes = None
    App = None
    Servicios = None
    Cajeros = None
    Ventanillas = None
    Personal = None
    Logo = None
    colores_de_uso = None

    def __init__(self):
        print("clase Banco")
    
    '''
    Metodos
    '''
    
    def abrir(self):
        print("Metodo abrir")
    
    def cerrar(self):
        print("Metodo cerrar")

    def crear_cuentas(self):
        print("Metodo crear cuentas")

    def importar_dinero(self):
        print("Metodo importar dinero")

    def exportar_dinero(self):
        print("Metodo exportar dinero")
   

# Creacion de un objeto basado en una clase
BBVA = Banco()

# Asiganacion de valores a las propiedades
BBVA.lugar = "Tulancingo de Bravo"
BBVA.compania = "BBVA"
BBVA.clientes = "si"
BBVA.app = "si"
BBVA.servicios = "si"
BBVA.cajeros = 20
BBVA.ventanillas = "10"
BBVA.personal = "si"
BBVA.logo = "si"
BBVA.colores_de_uso = "azul y blanco"

# Imprimir valore de las propiedades
print(BBVA.lugar)
print(BBVA.compania)
print(BBVA.clientes)
print(BBVA.app)
print(BBVA.servicios)
print(BBVA.cajeros)
print(BBVA.ventanillas)
print(BBVA.personal)
print(BBVA.logo)
print(BBVA.colores_de_uso)

# Invocar metodos de la clase
BBVA.abrir()
BBVA.cerrar()
BBVA.crear_cuentas()
BBVA.importar_dinero()
BBVA.exportar_dinero()
