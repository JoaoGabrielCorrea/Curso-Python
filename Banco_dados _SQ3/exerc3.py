# 3-	Crie um banco de dados chamado Produtos, nele vão estar contido os itens de um cardápio de um restaurante #FEITO#
# (sejam criativos ), pelo vscode ADICIONE, ALTERE, e DELETE alguns itens do cardápio, 
# e após cada uma dessas ações MOSTRE o cardápio para o usuário.
# Crie o banco de dados e a tabela no DB BROWSER e o CRUD façam pelo vscode. 
# Façam uma classe Cardápio onde tenha funções que façam cada um dos itens do CRUD (CREATE,READ,UPDATE,DELETE).

import sqlite3

conexao=sqlite3.connect("Produtos")

comand=conexao.cursor()

comand.execute('CREATE TABLE IF NOT EXISTS Produtos('
'id INTEGER PRIMARY KEY AUTOINCREMENT,'
'Produto TEXT,'
'Preco REAL'')')


produto= (input("Insira nome produto: "))
preco= (input("Insira preço do produto: "))

comand.execute(f'INSERT INTO Produtos(Produto,Preco) VALUES("{produto}",{preco})')
conexao.commit()
comand.execute('SELECT * FROM Produtos')
for linha in comand.fetchall():
    print(linha)


comand.execute(f'UPDATE Produtos SET Produto = "Bolonhesa" WHERE Produto = "Bosta"')
conexao.commit()
comand.execute('SELECT * FROM Produtos')
for linha in comand.fetchall():
    print(linha)

comand.close() #NAO ESQUEÇA DE FECHAR O CURSOR E A CONEXAO NO FINAL DO CODIGO
conexao.close()