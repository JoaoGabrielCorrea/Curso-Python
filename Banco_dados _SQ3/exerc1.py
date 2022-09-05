import sqlite3

conexao = sqlite3.connect('tabelacliente.db') 
cursor = conexao.cursor()

#execute executa um comando SQL
cursor.execute('CREATE TABLE IF NOT EXISTS clientes('
'id INTEGER PRIMARY KEY AUTOINCREMENT,'
'nome TEXT,'
'saldo REAL,'
'numero_conta INT'
'Agencia INT'
