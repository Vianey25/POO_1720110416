from math import sqrt

class Punto:
   def __init__(self, x, y):
    self.x =x
    self.y =y
def calcular_distancia(p1, p2):
    return sqrt((p1.x-p2.x)** + (p1.y - p2.y)**2)  

punto1 = Punto(3, 4)
punto2 = Punto(4, 7)   




print(calcular_distancia(punto1, punto2))







