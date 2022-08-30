class Bomba_Combustivel:
    def __init__(self,tipoCombustivel,valorLitro,quantidadeCombustivel):
        self.tipoCombustivel=tipoCombustivel
        self.valorLitro=valorLitro
        self.quantidadeCombustivel=quantidadeCombustivel 

    def abastecervalor(self,valor):
        self.valor = valor/self.valorLitro
        valor = valor/self.valorLitro
        return valor
    
    def abastecidovalor(self,valor):
        self.valor = valor
        valor/self.valorLitro
        return valor

    def abastecerlitros(self,litros):
        self.litros=litros
        litros = litros*self.valorLitro
        return litros
    
    def abastecidolitros(self,litros):
        self.litros=litros
        return litros

    def atualizarcombustivelbomba(self):
        disponivel=self.quantidadeCombustivel-(self.abastecidolitros(self.litros)+self.abastecidovalor(self.valor))
        self.quantidadeCombustivel = disponivel
        return disponivel


bomba1=Bomba_Combustivel("etanol",5,150) #atribuindo combustivel,preço,quantidade

# print (bomba1.tipoCombustivel) #mostrar tipo de Combustivel da bomba
# print (bomba1.valorLitro) #mostrar preço de Combustivel da bomba
# print (bomba1.quantidadeCombustivel) #mostrar quantidade de Combustivel da bomba

print (bomba1.abastecerlitros(5)) #mostra valor quando abastecido em litros
print (bomba1.abastecervalor(5)) #mostra quantidade de litros quando abastecido com valor
#Chamar método precisa do fechamento dos parenteses
print (bomba1.atualizarcombustivelbomba()) #mostra quantiade de litros disponivel na bomba