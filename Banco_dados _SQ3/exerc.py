# 1-	Um hacker invadiu o nosso banco de dados de clientes e acabou fazendo uma bagunça! 
# Tínhamos 16 clientes antes e agora temos mais de 5000!!!! 
# Infelizmente são apenas cópias dos clientes originais, preciso que você DELETE os clientes sobressalentes 
# (deixei apenas 1 nome de cada), e deixe apenas 1 de cada cliente original, apenas 
# lembro que seus pesos ficavam entre 50 e 100 quilos 
# (se tiver 2 nomes iguais com peso diferente você escolhe qual peso vai deletar), mas até isso o Hacker bagunçou….

# 2-	Nosso banco está muito cheio de clientes e precisamos deletar 
# todos os clientes que não pagam a assinatura de nosso produto a mais de 1 ano. 
# (Nesse você irá criar a tabela e inserir esses clientes por conta própria)
# DICA: variável do tipo booleana em SQLITE será do tipo INTEGER onde 0 será false e 1 será
# True.

# 3-	Crie um banco de dados chamado Produtos, nele vão estar contido os itens de um cardápio de um restaurante
# (sejam criativos ), pelo vscode ADICIONE, ALTERE, e DELETE alguns itens do cardápio, 
# e após cada uma dessas ações MOSTRE o cardápio para o usuário.
# Crie o banco de dados e a tabela no DB BROWSER e o CRUD façam pelo vscode. 
# Façam uma classe Cardápio onde tenha funções que façam cada um dos itens do CRUD.



import sqlite3

conexao=sqlite3.connect("dataBase.db")

comando=conexao.cursor()


#ver=(input("O que deseja deletar no banco de dados? "))
#filtro= (input("O que deseja Filtrar  para deletar no banco de dados? -->-- --<-- --==--  "))
#valor= (input("Qual valor quer Filtrar para deletar no banco de dados?  "))  

comando.execute('DELETE FROM clientes WHERE peso > 100 OR peso < 50')
conexao.commit()
comando=conexao.execute('SELECT * FROM clientes')
for linha in comando.fetchall():
    print(linha)
    
comando.execute('DELETE FROM clientes WHERE peso > 100 OR peso < 50')
conexao.commit()
comando=conexao.execute('SELECT * FROM clientes')
for linha in comando.fetchall():
    print(linha)

id= (input("ID para deletar no banco de dados?  "))
delete_nome=(input("Nome para deletar no banco de dados? "))
#filtro= (input("O que deseja Filtrar  para deletar no banco de dados? -->-- --<-- --==--  "))
 

comando.execute(f'DELETE FROM clientes WHERE id !={id} AND nome== "{delete_nome}"')
conexao.commit()
comando=conexao.execute('SELECT * FROM clientes')
for linha in comando.fetchall():
    print(linha)

    
