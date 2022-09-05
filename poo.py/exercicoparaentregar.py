from abc import ABC, abstractmethod
# '''
# Exercicio com abstração, herança, encapsulamento
## Criar um sistema bancario(extremamente simple) que tem clientes, contas e um banco.
## A ideia é que o cliente tenha uma conta(poupança ou corrente) e que possa sacar/depositar nessa conta.
## Contas corrente tem um limite extra. Banco tem clientes e contas.

# Dicas:
# Criar classe Cliente que herda da classe Pessoa(Herança)
#     Pessoa tem nome e idade(com getters)
#     Cliente TEM conta(agregação de classe ContaCorrente ou ContaPoupança)
# Criar classes Conta_Bancaria Poupança e ContaCorrente que herdam de conta
#     ContaCorrente deve ter um limite extra.
#     Contas tem agência, numero de conta e saldo
#     Contas devem ter método para deposito
#     Contas(super classe) deve ter o método sacar abstrato(Abstração - as subclassesque implementam o método sacar)
# Criar classe Banco para AGREGAR classes de clientes e de contas(Agregação)
# Banco será responsável autenticar o cliente e as contas da seguinte maneira:
#     Banco tem contas e clientes(Agregação)
#     * Checar se a agência é daquele banco
#     * Checar se o cliente é daquele banco
#     * Checar se a conta é daquele banco
# Só sera possivel sacar se passar na autenticação do banco(descrita acima)
# '''

class Banco(ABC):

    @abstractmethod
    def numero_banco (self):
        pass

    @abstractmethod
    def conta_banco (self):
        pass

    @abstractmethod  
    def nome_banco (self):
        pass


class Pessoa:
    def __init__(self,nome,idade,sexo,raca) -> None:
        self.nome=nome
        self.idade=idade
        self.sexo=sexo
        self.raca=raca
        pass

class Cliente(Pessoa):
    def __init__(self,nome,idade) -> None:
        self.nome_cliente=nome
        self.idade=idade
        pass
class Conta_Bancaria(Banco,Cliente):
    def __init__ (self,nome_cliente, numero_agencia, tipo_de_conta, saldo_conta):
        self.nome=nome_cliente
        self.agencia=numero_agencia
        self.conta_bacaria=tipo_de_conta
        self.saldo=saldo_conta
        
    def mostrar_nome_cliente (self):
        return self.nome

    def numero_banco (self):
        numero_banco=(1991)
        return (f"Número Banco: {numero_banco}")
        pass
    def conta_banco (self):
        pass
    def nome_banco (self):
        nome_banco = ("Se Banco fosse bom se chamaria Sofá")
        return (f"Banco: {nome_banco}")
        pass
    
    def mostrar_tipo_conta (self):
        return self.conta_bacaria
        

    def depositar_conta(self,deposito):
        self.saldo+=deposito
        pass

    def mostrar_saldo_conta(self):
        return self.saldo
        pass

    def sacar_conta(self,saque):
        self.saldo-=saque
    pass

class Conta_Poupanca(Conta_Bancaria):
    def __init__(self, nome_cliente, numero_agencia, tipo_de_conta, saldo_conta):
        super().__init__(nome_cliente, numero_agencia, tipo_de_conta, saldo_conta)
        
class Conta_Corrente (Conta_Poupanca):
    def __init__(self, nome_cliente, numero_agencia, tipo_de_conta, saldo_conta):
        super().__init__(nome_cliente, numero_agencia, tipo_de_conta, saldo_conta)
        self.saldo_conta=saldo_conta

    def limite_extra(self):
        return self.saldo*0.3
        pass


add_cliente_corrente=Conta_Corrente ("João","001","Conta Corrente",1000) # inserir cliente

print (add_cliente_corrente.numero_banco()) #mostrar cliente corrente
print (add_cliente_corrente.nome_banco()) #mostrar cliente corrente
print (add_cliente_corrente.mostrar_nome_cliente()) #mostrar cliente corrente
print (add_cliente_corrente.mostrar_tipo_conta()) #mostrar cliente corrente
print (add_cliente_corrente.limite_extra()) #mostrar cliente corrente

