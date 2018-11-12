import requests as Req

url = "http://127.0.0.1:7000/produtos"
descricao = input("Digite a descrição: ")
preco = float(input("Digite o preço: "))
dados = {"descricao": descricao, "preco": preco, "id": 3}
retorno = Req.api.put(url, json = dados).json()
print(retorno)
