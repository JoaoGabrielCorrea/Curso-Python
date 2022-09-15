import sqlite3

class Conta:# Classe conta 

    def entrar_conta(self,email,senha): # Função criar conta, solicita email e senha com argumentos
        self.email=email
        self.senha=senha
        conexao=sqlite3.connect("NETFlix.db")
        comand=conexao.cursor()
        comand.execute('SELECT email, senha FROM CONTA WHERE email=? AND senha=?', [email, senha])
        dados = comand.fetchone()   # variavel que usa metodo para buscar no banco de dados e retornar valor
                                    #nesse caso caso retorne NONE significa que não possui no banco de dados.

        if dados == None: # explicado em dados, essa é a condição de retorno.
            print("--------------------------")
            print("Usuario ou senha invalidos")
            print("--------------------------")
            return "Usuario ou senha invalidos" 
            
        else:
            print("------------------------------------")
            print(f"Seja Bem Vindo á sua conta: {email}")
            print("------------------------------------")
        
    def criar_conta(self,email,senha): #função criar conta
        self.email=email
        self.senha=senha
        conexao=sqlite3.connect("NETFlix.db")
        conexao.execute("PRAGMA foreign_keys = 1")
        comand=conexao.cursor()
        comand.execute('CREATE TABLE IF NOT EXISTS NETFlix('
        'id INTEGER PRIMARY KEY AUTOINCREMENT,'
        'EMAIL TEXT,'
        'senha TEXT'')')
        comand.execute(f'INSERT INTO CONTA(EMAIL,senha) VALUES("{email}","{senha}")')
        conexao.commit()
        comand.execute('SELECT * FROM CONTA')
        for linha in comand.fetchall():
            print(linha)

    def ler_conta(self,pesquisa): #função mostrar todas contas cadastradas no bancos de dados.
        self.pesquisa=pesquisa
        conexao=sqlite3.connect("NETFlix.db")
        conexao.execute("PRAGMA foreign_keys = 1")
        comand=conexao.cursor()
        comand.execute (f'SELECT EMAIL FROM CONTA WHERE EMAIL = "{pesquisa}"')
        for linha in comand.fetchall():
            print(linha)

    def atualizar_conta(self,nova_senha,senha_atual): #Função atualizar dados no banco de dados.
        self.nova_senha=nova_senha 
        self.senha_atual=senha_atual
        conexao=sqlite3.connect("NETFlix.db")
        conexao.execute("PRAGMA foreign_keys = 1")
        comand=conexao.cursor()
        comand.execute(f'UPDATE CONTA SET senha = "{nova_senha}" WHERE senha = "{senha_atual}"')
        conexao.commit()
        # comand.execute('SELECT * FROM EMAIL') #caso queira pode printar o na tela o registro atualizado.
        # for linha in comand.fetchall():
        #     print(linha)

    def deletar_conta(self,deletar): # Função deletar conta especifica, passando apenas o email.
        self.deletar=deletar
        conexao=sqlite3.connect("NETFlix.db")
        conexao.execute("PRAGMA foreign_keys = 1")
        comand=conexao.cursor()
        comand.execute(f'DELETE FROM CONTA WHERE EMAIL = "{deletar}"')
        conexao.commit()
        comand.execute('SELECT * FROM CONTA')
        for linha in comand.fetchall():
            print(linha)

class Perfil: #Classe Perfil

    def entrar_perfil(self,nome,email_perfil): # Função entrar no perfil.
        self.nome=nome
        self.email_perfil=email_perfil
        conexao=sqlite3.connect("NETFlix.db")
        conexao.execute("PRAGMA foreign_keys = 1")
        comand=conexao.cursor()
        comand.execute('SELECT nome, email FROM Perfil WHERE nome=? AND email=?', [nome, email_perfil])
        dados = comand.fetchone()

        if dados == None:   #validação se existe perfil no banco de dados
            print("------------------")   
            print("Usuario não existe")
            print("------------------") 
        else:
            print("------------------------------------")
            print(f'Seja Bem Vindo ao seu Perfil: {nome}')
            print("------------------------------------")

    def criar_perfil(self,nome,email_perfil): #função criar perfil
        self.nome=nome
        self.email_perfil=email_perfil
        conexao=sqlite3.connect("NETFlix.db")
        conexao.execute("PRAGMA foreign_keys = 1")
        comand=conexao.cursor()
        comand.execute('CREATE TABLE IF NOT EXISTS NETFlix('
        'id INTEGER PRIMARY KEY AUTOINCREMENT,'
        'nome TEXT,'
        'email TEXT'')')
        comand.execute(f'INSERT INTO Perfil(nome,email) VALUES("{nome}","{email_perfil}")')
        conexao.commit()
        comand.execute('SELECT * FROM Perfil')
        for linha in comand.fetchall():
            print(linha)

    def atualizar_perfil(self,novo_nome,nome_atual):# Função editar perfil existente, aprenta todos perfil criados.
        self.novo_nome=novo_nome
        self.nome_atual=nome_atual
        conexao=sqlite3.connect("NETFlix.db")
        conexao.execute("PRAGMA foreign_keys = 1")
        comand=conexao.cursor()
        comand.execute(f'UPDATE Perfil SET nome = "{novo_nome}" WHERE nome = "{nome_atual}"')
        conexao.commit()
        comand.execute('SELECT * FROM Perfil')
        for linha in comand.fetchall():
            print(linha)

    def ver_perfil(self): #Função mostrar todos perfil criados.
        conexao=sqlite3.connect("NETFlix.db")
        conexao.execute("PRAGMA foreign_keys = 1")
        comand=conexao.cursor()
        comand.execute('SELECT * FROM Perfil')
        for linha in comand.fetchall():
            print(linha)
    
    def deletar_perfil(self,deletar): # Função deletar Perfil.
        self.deletar=deletar
        conexao=sqlite3.connect("NETFlix.db")
        conexao.execute("PRAGMA foreign_keys = 1")
        comand=conexao.cursor()
        comand.execute(f'DELETE FROM Perfil WHERE EMAIL = "{deletar}"')
        conexao.commit()
        comand.execute('SELECT * FROM Perfil')
        for linha in comand.fetchall():
            print(linha)

    def filme_favorito(self): # Função mostrar filmes favoritos, previamente cadastrado no banco de dados.
        conexao=sqlite3.connect("NETFlix.db")
        comand=conexao.cursor()
        comand.execute('SELECT * FROM Filme_Favorito')
        for linha in comand.fetchall():
            print(linha)

while True: #Laço de repetição até o usuario digitar 3 para sair do programa.
    menu= int(input("MENU: \n1- Criar Conta\n2- Acessar Conta\n3- Sair\n-Sua Escolha: ")) #menu de escolha de opções.

    match menu:
        case 1:
            cadastro=Conta()
            criar_email=(input('Insira email para cadastro de conta: '))
            criar_senha=(input('Insira senha para cadastro de conta: '))
            cadastro.criar_conta(criar_email,criar_senha)

        case 2:
            cadastro=Conta()
            acessar_email=(input('Insira email para acessar sua conta: '))
            acessar_senha=(input('Insira senha para acessar sua conta: '))
            
            if cadastro.entrar_conta(acessar_email,acessar_senha)!= "Usuario ou senha invalidos":
                menu= int(input("MENU: \n1- Alterar Senha\n2- Excluir Conta\n3- Criar Perfil\n4- Alterar nome do Perfil\n"
                "5- Visualizar todos os perfis existentes\n"
                "6- Entrar em um perfil\n7- Ver Favoritos\n8- Excluir perfil\n9- Voltar para criar Conta\n-Sua Escolha: "))
            
                if menu == 1:
                    cadastro=Conta()
                    nova_senha=(input('Insira nova senha da conta: '))
                    senha_atual=(input('Insira senha atual confirmar nova senha da conta: '))
                    cadastro.atualizar_conta(nova_senha,senha_atual)

                elif menu == 2:
                    cadastro=Conta()
                    deletar=(input('Insira usuário para deletar: '))
                    cadastro.deletar_conta(deletar)
                    
                elif menu == 3:
                    cadastro=Perfil()
                    nome=(input('Insira nome para criar perfil: '))
                    email_perfil=(input('Insira email para criar perfil: '))
                    cadastro.criar_perfil(nome,email_perfil)

                elif menu == 4:
                    cadastro=Perfil()
                    novo_nome=(input('Insira nome para criar perfil: '))
                    nome_atual=(input('Insira nome para criar perfil: '))
                    cadastro.atualizar_perfil(novo_nome,nome_atual)

                elif menu == 5:
                    cadastro=Perfil()
                    print("-------------------")
                    print("Seus perfis Criados")
                    print("-------------------")
                    cadastro.ver_perfil()
                    
                elif menu == 6:
                    cadastro=Perfil()
                    nome=(input('Insira nome para criar perfil: '))
                    email_perfil=(input('Insira email para criar perfil: '))
                    cadastro.entrar_perfil(nome,email_perfil)

                elif menu == 7:
                    cadastro=Perfil()
                    cadastro.filme_favorito()

                elif menu == 8:
                    cadastro=Perfil()
                    deletar=(input('Insira usuário do perfil para deletar: '))
                    cadastro.deletar_perfil(deletar)
                
                elif menu == 9:
                    cadastro=Conta()
                    criar_email=(input('Insira email para cadastro de conta: '))
                    criar_senha=(input('Insira senha para cadastro de conta: '))
                    cadastro.criar_conta(criar_email,criar_senha)
                else:
                    print("Senha ou usuario inválidos")
                    
        case 3:
            print("------------------------")
            print("Você finalizou o Sistema")
            print("------------------------")
            exit()
            
        case _:
            print("--------------")
            print("Opção Inválida")
            print("--------------")