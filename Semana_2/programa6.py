class Futbolista():
    
    '''
    Atributos
    '''
    nombre  = None
    edad  = None
    peso = None
    estatura = None
    numero_celular = None
    equipo = None
    probabilidad = None
    posicion_que_juega = None
    lugar_de_nacimiento = None
    tiempo_jugando = None

    def __init__(self):
        print("clase Futbolista")
    
    '''
    Metodos
    '''
    
    def comer(self):
        print("Metodo comer")
    
    def ejercitar_su_cuerpo(self):
        print("Metodo Ejercitar")

    def jugar(self):
        print("Metodo jugar")

    def descansar(self):
        print("Metodo descansar")

    def dormir(self):
        print("Metodo dormir")
   

# Creacion de un objeto basado en una clase
Memo_Ochoa  = Futbolista()

# Asiganacion de valores a las propiedades
Memo_Ochoa.nombre = "GUILLERMO OCHOA MAGAÑA"
Memo_Ochoa.edad = "35 años"
Memo_Ochoa.peso = "78kg"
Memo_Ochoa.estatura = "1,85m"
Memo_Ochoa.numero_celular = "7751481259"
Memo_Ochoa.equipo = "America"
Memo_Ochoa.probabilidad = "93%"
Memo_Ochoa.posicion_que_juega = "Portero"
Memo_Ochoa.lugar_de_nacimiento = "Guadalajara.Mexico"
Memo_Ochoa.tiempo_de_juego= "17 años"

# Imprimir valores de las propiedades
print(Memo_Ochoa.nombre)
print(Memo_Ochoa.edad)
print(Memo_Ochoa.peso)
print(Memo_Ochoa.estatura)
print(Memo_Ochoa.numero_celular)
print(Memo_Ochoa.equipo)
print(Memo_Ochoa.probabilidad)
print(Memo_Ochoa.posicion_que_juega)
print(Memo_Ochoa.lugar_de_nacimiento )
print(Memo_Ochoa.tiempo_de_juego )

# Invocar metodos de la clase
Memo_Ochoa.comer ()
Memo_Ochoa.ejercitar_su_cuerpo()
Memo_Ochoa.jugar()
Memo_Ochoa.descansar ()
Memo_Ochoa.dormir()

