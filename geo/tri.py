import forma.abstract as abs

class Triangulo(abs.Abstract):
    def set_base(self, b):
        self.b = b

    def set_altura(self, h):
        self.h = h

    def area(self):
        print("Area %.2f" % ((self.b * self.h)/2))

    def desenha(self):
        print("sou trianguloo")
        
