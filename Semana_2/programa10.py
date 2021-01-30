class Google_classroom():
    
    '''
    Atributos
    '''
    logo  = None
    uso   = None
    almacenamiento = None
    version = None
    programa = None
    archivos  = None
    links = None
    grupos = None
    personas = None
    
    def __init__(self):
        print("clase Google_classroom")
    
    '''
    Metodos
    '''
    
    def descargar(self):
        print("Metodo descargar")
    
    def atender(self):
        print("Metodo atender")

    def recibir(self):
        print("Metodo recibir")

    def almacenar(self):
        print("Metodo almacenar")

    def gestionar(self):
        print("Metodo estionar")
   

# Creacion de un objeto basado en una clase
classroom = Google_classroom()

# Asiganacion de valores a las propiedades
classroom.logo = "si"
classroom.uso = "Enviar trabajos,poestear,recibir calificaciones"
classroom.almacenamiento = "22.43MB"
classroom.version = "6.12.501.02.30"
classroom.programa = "classroom"
classroom.archivos = "si"
classroom.links = "si"
classroom.grupos = "Ingresar con codigo"
classroom.personas= "si"


# Imprimir valores de las propiedades
print(classroom.logo)
print(classroom.uso)
print(classroom.almacenamiento)
print(classroom.version)
print(classroom.programa)
print(classroom.archivos)
print(classroom.links)
print(classroom.grupos)
print(classroom.personas)

# Invocar metodos de la clase
classroom.descargar()
classroom.atender()
classroom.recibir ()
classroom.almacenar ()
classroom.gestionar ()
