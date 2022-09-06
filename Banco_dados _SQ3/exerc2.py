# Crie um banco de dados com a tabela pessoas #feito#
# A tabela pessoas deve conter as colunas, nome, idade, peso, sexo e classe social #feito#
# Depois faca o codigo mostrar apenas as pessoas com peso acima de 60 ##
# Depois mostre apenas quem é do sexo feminino ##
# Depois mostre quem é de classe social Alta ##
# Depois mostre apenas quem tem peso acima de 60, idade que 18, sexo feminino e classe social alta ##
# Altere o peso e classe social de pelo menos 3 pessoas com idade acima de 60 anos. ##

import sqlite3

addbanco=(input("Você quer ADICIONAR ou VER banco de dados? --VER-- ou --ADICIONAR-- "))
conexao=sqlite3.connect("Banco_dados2")

comando=conexao.cursor()

if addbanco=="ADICIONAR":

    comando.execute('CREATE TABLE IF NOT EXISTS Pessoa('
    'ID INTEGER PRIMARY KEY AUTOINCREMENT,'
    'Nome TEXT,'
    'Email TEXT,'
    'Idade INTEGER,'
    'Sexo TEXT,'
    'Peso REAL,'
    'Classe_Social TEXT'')')


    id= (input("Insira ID: "))
    nome= (input("Insira nome: "))
    email1= (input("Insira email: "))
    idade= (input("Insira idade: "))
    sexo= (input("Insira sexo: "))
    peso= (input("Insira peso: "))
    classe_social= (input("Insira sua classe social: "))


    comando.execute(f'INSERT INTO Pessoa(ID,Nome,Email,Idade,Sexo,Peso,Classe_Social) VALUES({id},"{nome}","{email1}",{idade},"{sexo}",{peso},"{classe_social}")')
    conexao.commit()

    comando.close() #NAO ESQUEÇA DE FECHAR O CURSOR E A CONEXAO NO FINAL DO CODIGO
    conexao.close()

elif addbanco =="VER":

    ver=(input("O que deseja VER banco de dados? --VER--  "))
    filtro= (input("O que deseja Filtrar no banco de dados? -->-- --<-- --==--  "))
    valor= (input("Qual valore quer Filtrar no banco de dados?  "))
    

    comando.execute(f'SELECT * FROM Pessoa WHERE {ver} {filtro} {valor}')
    for linha in comando.fetchall():
        print(linha)


    comando.close() #NAO ESQUEÇA DE FECHAR O CURSOR E A CONEXAO NO FINAL DO CODIGO
    conexao.close()