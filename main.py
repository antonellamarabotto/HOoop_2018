import random
class Fila(object):
    """Clase base de fila"""

    def __init__(self):
         """constructor de la clase Fila """
         self.enfila= 0
         self.fila = []
         self.maxenfila=6

class FilaPreferencial(Fila):
    """Clase de la fila de los clientes preferenciales"""        
    
    def insertar(self, cliente=1):
        """Inserta un nuevo cliente en la fila preferencial"""
        self.enfila+=cliente
        self.fila=[1]*cliente
        pass

    def atender(self):
        """Atiende al proximo cliente prederencial"""
        self.enfila-=1
        self.fila.pop(0)
    
    def abrircajanueva(self,maxenfila,filanueva):
        """Si maxenfila es menor que la cantidad de clientes actualmente en espera, abro nueva caja"""
        if self.maxenfila<self.enfila:
            self.filanueva=self.enfila-self.maxenfila
        pass
    
    
    
class FilaGeneral(Fila):
    """Clase que mantiene una fila de clientes no preferenciales"""

    def insertar(self, cliente):
        """Inserta un nuevo cliente en la fila no preferencial"""
        self.enfila+=cliente
        self.fila=[1]*cliente
        pass

    def atender(self):
        """Atiende al proximo cliente prederencial"""
        self.enfila-=1
        self.fila.pop(0)
        pass      

    

class cliente(object):
     """clase cliente """
    def __init__(self,dni):
         """ constructor de la clase cliente """
        self.dni=dni
        self.categoria=None
    def modificarcategoria(self, categoria):
        """modifica el atributo categoria del cliente """
	res=random.randrange(2)
	if res==1:
		self.categoria="preferencial"
	else:
		self.categoria="General"
        
        pass
  
    
if __name__ == "__main__":
    """ simular una fila en una entidad bancaria"""
    ###Como me refiero a una clase particular? Porque las funciones en la fila general o en la fila preferencial se llaman iguales.
	lenfila=Fila()
	
	
    pass
