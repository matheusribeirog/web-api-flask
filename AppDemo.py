from flask import Flask
from flask import jsonify
from flask import request

produtos = [
    {"id": 1, "descricao": "furadeira", "preco": 125},
    {"id": 2, "descricao": "fresa", "preco": 350},
]

app = Flask(__name__)

@app.route("/ola", methods=["GET"])
def responder_ola():
    dados = {"mensagem": "Hello World!"}
    resposta = jsonify(dados)
    return resposta

@app.route("/produtos/<id>", methods = ["GET"])
def obter_produto(id):
    for i in range(len(produtos)):
        if produtos[i]["id"] == int(id):
            return jsonify({"dados": produtos[i], "status": "Sucesso", "mensagem": ""})
    return jsonify({"Status": "Não encontrado"})

@app.route("/produtos", methods = ["GET"])
def listar_produtos():
    resposta = {"dados": produtos, "status": "Sucesso", "mensagem": ""}
    return jsonify(resposta)

@app.route("/produtos", methods = ["PUT"])
def inserir_produto():
    dados = request.get_json()
    produtos.append(dados)
    return jsonify({"status": "Sucesso", "mensagem": ""})

@app.route("/produtos/<id>", methods=["DELETE"])
def excluir_produto(id):
    for i in range(len(produtos)):
        if produtos[i]["id"] == int(id):
            del produtos[i]
            return jsonify({"status": "Sucesso", "mensagem": ""})
    return jsonify({"status": "Não encontrado", "mensagem": ""})

if __name__ == "__main__":
    app.run(port = 7000, debug = True)
