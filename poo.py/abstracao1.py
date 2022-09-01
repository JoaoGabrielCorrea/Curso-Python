from abc import ABC, abstractmethod

class Geometrica(ABC): #class mãe abstrata
    @abstractmethod
    def perimetro(self):
        pass
    @abstractmethod
    def area(self):
        pass
        

class Quadrado(Geometrica):
   
    def perimetro(self,lado):
        self.perimetro = (lado*4)
        return self.perimetro
  
    def area(self,lado):
        self.area=(lado**2)
        return self.area

class Pentagono(Geometrica):
   
    def perimetro(self,lado):
        self.perimetro = (lado*5)
        return self.perimetro
  
    def area(self,lado,apotema):
        self.area=(lado*5*apotema/2)
        return self.area


quadrado=Quadrado()
pentagono=Pentagono()

print (quadrado.perimetro(5))
print (quadrado.area(5))

print (pentagono.perimetro(5))
print (pentagono.area(5,6))


    
# class Retangulo(self,comprimento,largura):
#         self.comprimento=comprimento
#         self.largura=largura

# class Triangulo(Geometrica):
#        def area(self,lado):
#         self.lado=lado
#         lado= (lado*lado/2)
    
# class circulo(self):
#     pass
    