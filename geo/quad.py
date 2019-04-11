import forma.abstract as abs

class Quadrado(abs.Abstract):

    def set_lado(self,l):
        self.l = l
 
    def area(self):
        print("Area %.2f" % (self.l **2)) 

    def desenha(self):
        print("Eu sou um quadrad")
