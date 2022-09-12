import sqlite3

class Conta:
        
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

    def deletar_conta(self,deletar):
        self.deletar=deletar
        conexao=sqlite3.connect("NETFlix.db")
        conexao.execute("PRAGMA foreign_keys = 1")
        comand=conexao.cursor()
        comand.execute(f'DELETE FROM CONTA WHERE Produto = "{deletar}"')
        conexao.commit()
        comand.execute('SELECT * FROM CONTA')
        for linha in comand.fetchall():
            print(linha)

class Perfil(Conta):
    def __init__(self,nome,email_perfil) -> None:
        super().__init__()
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




cadastro1=Perfil("joao","joao@gmail.com")

cadastro=Conta()
cadastro.criar_conta("joao@gmail.com","2525")
