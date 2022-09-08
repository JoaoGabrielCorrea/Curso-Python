# 2-	Nosso banco está muito cheio de clientes e precisamos deletar 
# todos os clientes que não pagam a assinatura de nosso produto a mais de 1 ano. 
# (Nesse você irá criar a tabela e inserir esses clientes por conta própria)
# DICA: variável do tipo booleana em SQLITE será do tipo INTEGER onde 0 será false e 1 será
# True.





import sqlite3

conexao=sqlite3.connect("dataBase2.db")

comando=conexao.cursor()
  


    
comando.execute('DELETE FROM clientes WHERE Atraso == 1')
conexao.commit()
comando=conexao.execute('SELECT * FROM clientes')
for linha in comando.fetchall():
    print(linha)


    
