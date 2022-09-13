import sqlite3

class Conta:

    def entrar_conta(self,email,senha):
        self.email=email
        self.senha=senha
        conexao=sqlite3.connect("NETFlix.db")
        conexao.execute("PRAGMA foreign_keys = 1")
        comand=conexao.cursor()

        comand.execute('SELECT email, senha FROM CONTA WHERE email=? AND senha=?', [email, senha])

        dados = comand.fetchone()

        if dados == None:
            print('Usuario ou senha invalidos')
        else:
            print(f'Seja Bem Vindo á sua conta: {email}')
        
    def criar_conta(self,email,senha):
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

    def ler_conta(self,pesquisa):
        self.pesquisa=pesquisa
        conexao=sqlite3.connect("NETFlix.db")
        conexao.execute("PRAGMA foreign_keys = 1")
        comand=conexao.cursor()
        comand.execute (f'SELECT EMAIL FROM CONTA WHERE EMAIL = "{pesquisa}"')
        for linha in comand.fetchall():
            print(linha)

        pass

    def atualizar_conta(self,novo_nome,nome_atual):
        self.novo_nome=novo_nome
        self.nome_atual=nome_atual
        conexao=sqlite3.connect("NETFlix.db")
        conexao.execute("PRAGMA foreign_keys = 1")
        comand=conexao.cursor()
        comand.execute(f'UPDATE CONTA SET senha = "{novo_nome}" WHERE senha = "{nome_atual}"')
        conexao.commit()
        comand.execute('SELECT * FROM EMAIL')
        for linha in comand.fetchall():
            print(linha)
            pass

    def deletar_conta(self,deletar):
        self.deletar=deletar
        conexao=sqlite3.connect("NETFlix.db")
        conexao.execute("PRAGMA foreign_keys = 1")
        comand=conexao.cursor()
        comand.execute(f'DELETE FROM CONTA WHERE EMAIL = "{deletar}"')
        conexao.commit()
        comand.execute('SELECT * FROM CONTA')
        for linha in comand.fetchall():
            print(linha)

class Perfil:

    def entrar_perfil(self,nome,email_perfil):
        self.nome=nome
        self.email_perfil=email_perfil
        conexao=sqlite3.connect("NETFlix.db")
        conexao.execute("PRAGMA foreign_keys = 1")
        comand=conexao.cursor()

        comand.execute('SELECT nome, email FROM Perfil WHERE nome=? AND email=?', [nome, email_perfil])

        dados = comand.fetchone()

        if dados == None:
            print('Usuario ou senha invalidos')
        else:
            print(f'Seja Bem Vindo ao seu Perfil: {nome}')

    def criar_perfil(self,nome,email_perfil):

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

    def atualizar_perfil(self,novo_nome,nome_atual):
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
            pass

    def ver_perfil(self):
        conexao=sqlite3.connect("NETFlix.db")
        conexao.execute("PRAGMA foreign_keys = 1")
        comand=conexao.cursor()
        comand.execute('SELECT * FROM Perfil')
        for linha in comand.fetchall():
            print(linha)
            pass
    
    def deletar_perfil(self,deletar):
        self.deletar=deletar
        conexao=sqlite3.connect("NETFlix.db")
        conexao.execute("PRAGMA foreign_keys = 1")
        comand=conexao.cursor()
        comand.execute(f'DELETE FROM Perfil WHERE EMAIL = "{deletar}"')
        conexao.commit()
        comand.execute('SELECT * FROM Perfil')
        for linha in comand.fetchall():
            print(linha)

    def filme_favorito(self):
        conexao=sqlite3.connect("NETFlix.db")
        conexao.execute("PRAGMA foreign_keys = 1")
        comand=conexao.cursor()
        comand.execute('SELECT * FROM Filme_Favorito')
        for linha in comand.fetchall():
            print(linha)
            pass
        pass


cadastro=Conta()
perfil=Perfil()
#cadastro.criar_conta("jo@gmail.com","2525")
#cadastro.ler_conta("jo@gmail.com")
# cadastro.deletar_conta("joa@gmail.com")
# cadastro.criar_perfil("João","joa@gmail.com")
# cadastro.atualizar_perfil("Tiago","João")
# perfil.ver_perfil()
cadastro.entrar_conta("tee","12")
perfil.entrar_perfil("jo","5")
perfil.filme_favorito()
#perfil.deletar_perfil("joa@gmail.com")
