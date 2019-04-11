from geo.quad import Quadrado 
from geo.circ import Circulo
from geo.ret import Retangulo
from geo.tri import Triangulo

# p = Fabrica.produz("circulo")

class Fabrica(object):

    def produz(tipo):
        if tipo == "circulo":
            return Circulo()

        if tipo ==  "quadrado":
            return Quadrado()

        if  tipo == "retangulo":
            return Retangulo()

        if tipo == "triangulo":
            return Triangulo()

    produz = staticmethod(produz)
