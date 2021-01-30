class Serie_TV():
    
    '''
    Atributos
    '''
    transmitido  = None
    Canal_de_transmisión  = None
    tiempo_de_duracion = None
    tiempo_de_serie = None
    numero_de_episodios = None
    numero_de_temporadas = None
    tiempo_de_episodio = None
    origen = None
    director = None
    personajes = None

    def __init__(self):
        print("clase Serie_TV")
    
    '''
    Metodos
    '''
    
    def planear(self):
        print("Metodo Planear")
    
    def cotizar(self):
        print("Metodo cotizar")

    def actuar(self):
        print("Metodo actuar")

    def dedicar(self):
        print("Metodo dedicar")

    def transmitir(self):
        print("Metodo transmitir")
   

# Creacion de un objeto basado en una clase
Anime  = Serie_TV()

# Asiganacion de valores a las propiedades
Anime.transmitida = "TV"
Anime.canal_de_transmicion = 7
Anime.tiempo_de_serie= "2hrs"
Anime.numero_de_episodios = 100
Anime.numero_de_temporadas = 3
Anime.tiempo_de_episodio = "Cada mes"
Anime.origen = "Chinese"
Anime.director = "Carlos Velazquez Orquidia"
Anime.personajes = "si"

# Imprimir valores de las propiedades
print(Anime.transmitida)
print(Anime.canal_de_transmicion)
print(Anime.tiempo_de_serie)
print(Anime.numero_de_episodios)
print(Anime.numero_de_temporadas)
print(Anime.tiempo_de_episodio)
print(Anime.origen)
print(Anime.director)
print(Anime.personajes )

# Invocar metodos de la clase
Anime.planear ()
Anime.cotizar ()
Anime.actuar ()
Anime.dedicar ()
Anime.transmitir ()
