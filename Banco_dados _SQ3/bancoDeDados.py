import sqlite3

conexao = sqlite3.connect('bancoTeste.db')
cursor = conexao.cursor()

cursor.execute('CREATE TABLE IF NOT EXISTS pessoas('
'id INTEGER PRIMARY KEY AUTOINCREMENT,'
'nome TEXT NOT NULL,'
'peso REAL'
')')

#CREATE - PRECISA DE COMMIT
# cursor.execute('INSERT INTO pessoas (nome,peso) VALUES (?,?)',("Alencar",74))
# conexao.commit()

#UPDATE - PRECISA DE COMMIT
# cursor.execute('UPDATE pessoas SET peso = ?, nome = ? WHERE id = 1',(120,"José"))
# conexao.commit()

#DELETE - PRECISA DE COMMIT
# cursor.execute('DELETE FROM pessoas WHERE id = 2')
# conexao.commit()

#READ - NÃO PRECISA DE COMMIT
cursor.execute('SELECT nome,peso,id FROM pessoas')
for linha in cursor.fetchall():
    print(linha)

cursor.close()
conexao.close()