import sqlite3

conexao = sqlite3.connect('baseDeDados.db') # Extensão não é necessaria, mas é importante pra outros programadores saberem que é uma base de dados
cursor = conexao.cursor()

#execute executa um comando SQL
cursor.execute('CREATE TABLE IF NOT EXISTS clientes('
'id INTEGER PRIMARY KEY AUTOINCREMENT,'
'nome TEXT,'
'peso REAL'
')')#cria uma tabela se ela não existir, com algumas variaveis e seus tipos

# cursor.execute('INSERT INTO clientes(nome,peso) VALUES("Bruno",80)')
# cursor.execute('INSERT INTO clientes(nome,peso) VALUES(?,?)',('Aline',60))#DESSE JEITO VOCE EVITA SQLINJECTION
# conexao.commit()#Executa comandos que alteram a tabela de dados, sem o commit o INSERT nao funciona
# cursor.execute('UPDATE clientes SET peso = ? WHERE id =2',(58,))
# conexao.commit()
# cursor.execute('DELETE FROM clientes WHERE id =2')#CUIDADO AO FAZER DELETE SEM WHERE
cursor.execute('SELECT * FROM clientes')
for linha in cursor.fetchall():
    print(linha)

cursor.close() #NAO ESQUEÇA DE FECHAR O CURSOR E A CONEXAO NO FINAL DO CODIGO
conexao.close()