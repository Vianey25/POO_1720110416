class Estudiante():
    
    '''
    Atributos
    '''
    nombre = None
    edad = None
    domicilio = None
    numero_celular = None
    estatura = None
    tez = None
    forma_de_cara = None
    peso = None
    tipo_de_cabello = None
    rasgos = None

    def __init__(self):
        print("clase Estudiante")
    
    '''
    Metodos
    '''
    
    def estudiar(self):
        print("Metodo Estudiar")
    
    def trabajar(self):
        print("Metodo Trabajar")

    def comer(self):
        print("Metodo crear Comer")

    def despertar(self):
        print("Metodo Despertar")

    def analizar(self):
        print("Metodo Analizar")
   

# Creacion de un objeto basado en una clase
Universitaria = Estudiante()

# Asiganacion de valores a las propiedades
Universitaria.nombre = "Vianey Gonzalez Guzman"
Universitaria.edad = 18
Universitaria.domicilio = "Acatlan Hgo"
Universitaria.num_celular = "7751892294"
Universitaria.peso = "54kg"
Universitaria.estatura = "1.57"
Universitaria.tez = "morena clara"
Universitaria.forma_de_cara = "ovalada"
Universitaria.tipo_de_cabello = "ondulado"
Universitaria.rasgos = "lunar en la mejilla izquierda"

# Imprimir valore de las propiedades
print(Universitaria.nombre )
print(Universitaria.edad)
print(Universitaria.domicilio)
print(Universitaria.num_celular)
print(Universitaria.peso)
print(Universitaria.estatura)
print(Universitaria.tez)
print(Universitaria.forma_de_cara)
print(Universitaria.tipo_de_cabello)
print(Universitaria.rasgos)

# Invocar metodos de la clase
Universitaria.estudiar()
Universitaria.trabajar()
Universitaria.comer()
Universitaria.despertar()
Universitaria.analizar()