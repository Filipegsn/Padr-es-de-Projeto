#from geo.Quadrado import Quadrado
#from geo.Circulo import Circulo
from forma.fabrica import Fabrica as f

q = f.produz("quadrado")
q.set_lado(2)
q.area()
q.desenha()

c = f.produz("circulo")
c.set_raio(2)
c.area()
c.desenha()

r = f.produz("retangulo")
r.set_base(4)
r.set_altura(8)
r.area()
r.desenha()

t = f.produz("triangulo")
t.set_base(6)
t.set_altura(6)
t.area()
t.desenha()
