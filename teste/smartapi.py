#https://pokeapi.co/api/v2/pokemon/{id or name}/
#passar nome ou id do pokemon
#nome do pokemon ou mensagem de erro
#imagem ou gif ou sprit geração 5
#tipo do pokemon
#tamanho 
#peso

from pip._vendor import requests

def linha():
    return('-'*40)


response_rewards=requests.get('http://explorer.smarts.cash:8080/v1/smartrewards/history').json()
print (response_rewards)

response_supply=requests.get('http://explorer.smarts.cash:8080/v1/blockchain/supply').json()
print (response_supply['CurrentSupply'])

