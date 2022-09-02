from abc import ABC, abstractmethod
# '''
# Exercicio com abstração, herança, encapsulamento
# Criar um sistema bancario(extremamente simple) que tem clientes, contas e um banco.
# A ideia é que o cliente tenha uma conta(poupança ou corrente) e que possa sacar/depositar nessa conta.
# Contas corrente tem um limite extra. Banco tem clientes e contas.

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

class Conta_Bancaria(Banco):
    def __init__ (self,nome_cliente, numero_agencia, tipo_de_conta, saldo_conta):
        self.cliente=nome_cliente
        self.agencia=numero_agencia
        self.conta=tipo_de_conta
        self.saldo=saldo_conta
        pass

    def numero_banco (self):
        return (1991)
        pass

    def conta_banco (self):
        pass

    def nome_banco (self):
        return ("Se Banco fosse bom se chamaria Sofá")
        pass
    
    def mostrar_tipo_conta (self):
        return self.conta
        pass

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

class Conta_Corrente (Conta_Bancaria): 
    def __init__(self, nome_cliente, numero_agencia, tipo_de_conta, saldo_conta):
        super().__init__(nome_cliente, numero_agencia, tipo_de_conta, saldo_conta)






#class Poupanca(Conta_Bancaria):

# add_cliente= Poupanca ("João","001",50) # inserir clinete
# print (add_cliente.cliente) #mostrar cliente
# print (add_cliente.conta) # mostrar conta
# print (add_cliente.saldo) #mostrar saldo
# add_cliente.depositar(112) #usa variavel cliente,usando função depositar com valor dentro de parenteses
# add_cliente.sacar(12) #usa variavel cliente,usando função sacar com valor dentro de parenteses
# print (add_cliente.saldo)
# add_cliente.rendimento_do_dia()
# print (add_cliente.saldo)