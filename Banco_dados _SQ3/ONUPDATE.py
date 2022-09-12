import sqlite3

conexao=sqlite3.connect("NETFlix.db")
comand=conexao.cursor()


comand.execute('CREATE TABLE IF NOT EXISTS NETFlix('
'id INTEGER PRIMARY KEY AUTOINCREMENT,'
'EMAIL TEXT,'
'senha TEXT'')')

escolha= (input("Insira sua escolha: 1 - CADASTRAR CONTA  / 2 - CRIAR PERFIL "))

if escolha=="1":
    email= (input("Insira EMAIL para cadastrar: "))
    senha= (input("Insira senha para cadastrar: "))

    comand.execute(f'INSERT INTO CONTA(EMAIL,senha) VALUES("{email}",{senha})')
    conexao.commit()
    comand.execute('SELECT * FROM NETFlix')
    for linha in comand.fetchall():
        print(linha)

elif escolha=="2":
    nome_perfil= (input("Insira nome para criar perfil: "))
    email= (input("Insira email para criar perfil: "))

    comand.execute(f'INSERT INTO Perfil(nome,email) VALUES("{nome_perfil}","{email}")')
    conexao.commit()
    comand.execute('SELECT * FROM NETFlix')
    print (f"Nome: {nome_perfil} adicionado ao Perfil! ")



comand.close() #NAO ESQUEÇA DE FECHAR O CURSOR E A CONEXAO NO FINAL DO CODIGO
conexao.close()