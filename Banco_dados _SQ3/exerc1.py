import sqlite3

conexao=sqlite3.connect("Lista_de_clientes")

comand=conexao.cursor()

comand.execute('CREATE TABLE IF NOT EXISTS clientes('
'id INTEGER PRIMARY KEY AUTOINCREMENT,'
'IDI INTEGER,'
'NOME TEXT,'
'SALDO REAL,'
'NUMERO_CONTA INTEGER,'
'AGENCIA INTEGER'')')

id= (input("Insira ID: "))
nome= (input("Insira nome: "))
saldo= (input("Insira saldo: "))
numero_conta= (input("Insira numero da conta: "))
agencia= (input("Insira agencia: "))


comand.execute(f'INSERT INTO clientes(IDI,NOME,SALDO,NUMERO_CONTA,AGENCIA) VALUES("{id}","{nome}",{saldo},{numero_conta},{agencia})')
conexao.commit()
comand.execute('SELECT * FROM clientes')
for linha in comand.fetchall():
    print(linha)

comand.close() #NAO ESQUEÇA DE FECHAR O CURSOR E A CONEXAO NO FINAL DO CODIGO
conexao.close()