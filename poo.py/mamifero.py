from abc import ABC, abstractmethod
from pickle import TRUE

class Mamifero(ABC): #class mãe abstrata
    @abstractmethod
    def mama(self):
        pass
    
    def parto(self):
        pass

   
    def locomocao(self):
        pass
        
class Cachorro(Mamifero):
    
    def mama(self,bebe_leite):
        if bebe_leite == "sim":
            return True
        else:
            return False
            

    # def parto(self,desenvolvimento):
    #     self.desenvolvimento=desenvolvimento
    #     desenvolvimento=(True)
    #     return "Uterino"

animal=Cachorro()


print (animal.mama("ops"))
