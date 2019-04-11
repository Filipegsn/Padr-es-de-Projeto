import forma.abstract as abs

class Circulo(abs.Abstract):
    def set_raio(self,r):
        self.r = r
    def area(self):
        print('Area: %.2f' %((self.r**2) * 3.14))
    def desenha(self):
        print("sou circulo AAAAAAAEEEEEOOOWWW")
