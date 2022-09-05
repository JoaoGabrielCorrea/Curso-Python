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

comand.execute('INSERT INTO clientes(IDI,NOME,SALDO,NUMERO_CONTA,AGENCIA) VALUES("01","JOAO",100,001,12)')
conexao.commit()
comand.execute('SELECT * FROM clientes')
for linha in comand.fetchall():
    print(linha)