import requests as Req

url = "http://127.0.0.1:7000/ola"
dados = Req.api.get(url).json()
print(dados)
