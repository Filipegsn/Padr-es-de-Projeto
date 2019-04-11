import abc

#c = Circulo // new Circulo()
#c.set_raio()

class Abstract(abc.ABC):

	@abc.abstractmethod
	def desenha(self):
	    pass

	
	@abc.abstractmethod
	def area(self):
	    pass
