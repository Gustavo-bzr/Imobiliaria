
from flask import Flask, jsonify, request, send_from_directory
import banco

app = Flask(__name__, static_folder="static")
banco.criar_tabelas()


@app.route("/")
def pagina_inicial():
    return send_from_directory("static", "index.html")




@app.route("/api/clientes", methods=["GET"])
def listar_clientes():
    return jsonify(banco.listar_clientes())


@app.route("/api/clientes", methods=["POST"])
def adicionar_cliente():
    d = request.json
    if not d.get("nome") or not d.get("cpf"):
        return jsonify({"erro": "Nome e CPF são obrigatórios"}), 400
    banco.adicionar_cliente(d["nome"], d["cpf"], d.get("telefone"), d.get("email"))
    return jsonify({"mensagem": "Cliente adicionado!"}), 201


@app.route("/api/clientes/<int:id>", methods=["PUT"])
def modificar_cliente(id):
    d = request.json
    if not d.get("nome") or not d.get("cpf"):
        return jsonify({"erro": "Nome e CPF são obrigatórios"}), 400
    banco.modificar_cliente(id, d["nome"], d["cpf"], d.get("telefone"), d.get("email"))
    return jsonify({"mensagem": "Cliente modificado!"})


@app.route("/api/clientes/<int:id>", methods=["DELETE"])
def excluir_cliente(id):
    banco.excluir_cliente(id)
    return jsonify({"mensagem": "Cliente excluído!"})



@app.route("/api/imoveis", methods=["GET"])
def listar_imoveis():
    return jsonify(banco.listar_imoveis())


@app.route("/api/imoveis", methods=["POST"])
def adicionar_imovel():
    d = request.json
    if not d.get("tipo") or not d.get("endereco") or not d.get("valor"):
        return jsonify({"erro": "Tipo, endereço e valor são obrigatórios"}), 400
    banco.adicionar_imovel(d["tipo"], d["endereco"], float(d["valor"]),
                           d.get("quartos") or 0, d.get("status", "Disponível"))
    return jsonify({"mensagem": "Imóvel adicionado!"}), 201


@app.route("/api/imoveis/<int:id>", methods=["PUT"])
def modificar_imovel(id):
    d = request.json
    if not d.get("tipo") or not d.get("endereco") or not d.get("valor"):
        return jsonify({"erro": "Tipo, endereço e valor são obrigatórios"}), 400
    banco.modificar_imovel(id, d["tipo"], d["endereco"], float(d["valor"]),
                           d.get("quartos") or 0, d.get("status", "Disponível"))
    return jsonify({"mensagem": "Imóvel modificado!"})


@app.route("/api/imoveis/<int:id>", methods=["DELETE"])
def excluir_imovel(id):
    banco.excluir_imovel(id)
    return jsonify({"mensagem": "Imóvel excluído!"})


if __name__ == "__main__":
    app.run(debug=True)
