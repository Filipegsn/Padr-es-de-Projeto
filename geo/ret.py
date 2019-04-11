import forma.abstract as abs

class Retangulo(abs.Abstract):
    def set_base(self, b):
        self.b = b
    def set_altura(self, h):
        self.h = h
    def area(self):
        print("Area %s" % (self.b*self.h))
    def desenha(self):
        print("eu sou um retanguloo")
