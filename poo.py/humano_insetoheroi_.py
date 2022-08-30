class Humano:
    def __init__(self,nomes,idade):
        self.nomes=nomes
        self.idade=idade
        

class Inseto:
    def __init__(self,nome,venenoso,alado):
        self.nome=nome
        self.venenoso=venenoso
        self.alado=alado
        

class Super_heroi(Humano,Inseto):
    def __init__(self,nomes,idade,venenoso,alado,poder):
        Inseto.__init__(self,nomes,venenoso,alado)
        super().__init__(nomes,idade)
        self.poder=poder
       

pessoa=Humano("João",31)
poder=Inseto("cigarra", False, True)
superhomem=Super_heroi("Super Cigarra",100,False,True,"Cantar até morrer")

print (f"Nome do humano {pessoa.nomes}, idade do humano {pessoa.idade}")
print (f"Nome do Inseto {poder.nome}, veneno {poder.venenoso}, voa {poder.alado} ")
print (f"Nome do Super Heroi {superhomem.nome}, idade heroi {superhomem.idade}, Poder {superhomem.poder} ")
print (superhomem.__dict__)
print (pessoa.__dict__)
print (poder.__dict__)