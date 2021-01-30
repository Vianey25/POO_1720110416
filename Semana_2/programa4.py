class Vacaciones():
    
    '''
    Atributos
    '''
    lugar = None
    tipo = None
    tiempo = None
    diversion = None
    periodo_vacacional = None
    numero_de_personas = None
    ambiente = None
    fotografias = None
    juegos = None
    conocimientos = None

    def __init__(self):
        print("clase vacaciones")
    
    '''
    Metodos
    '''
    
    def planear(self):
        print("Metodo Planear")
    
    def cotizar(self):
        print("Metodo cotizar")

    def viajar(self):
        print("Metodo viajar")

    def disfrutar(self):
        print("Metodo disfrutar")

    def regresar(self):
        print("Metodo regresar")
   

# Creacion de un objeto basado en una clase
Playa  = Vacaciones()

# Asiganacion de valores a las propiedades
Playa.lugar = "Veracruz"
Playa.tipo = "primaverales"
Playa.tiempo = "24/7"
Playa.diversion = "Buena"
Playa.periodo_vacacional = "25-abril - 30-abril"
Playa.numero_de_personas = "20"
Playa.ambiente = "caluroso"
Playa.juegos = "boleibol y futbol"
Playa.conocimientos = "Historia"
Playa.fotografias = "si"

# Imprimir valores de las propiedades
print(Playa.lugar )
print(Playa.tipo)
print(Playa.tiempo)
print(Playa.diversion)
print(Playa.periodo_vacacional)
print(Playa.numero_de_personas)
print(Playa.ambiente)
print(Playa.juegos)
print(Playa.conocimientos)
print(Playa.fotografias)

# Invocar metodos de la clase
Playa.planear()
Playa.cotizar()
Playa.viajar()
Playa.disfrutar()
Playa.regresar()
