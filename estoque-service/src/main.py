from flask import Flask, jsonify
from pydantic import ValidationError

from src.controllers.getReserva import getReservasPedido, getReservaPedidoProduto
from src.controllers.getProdutos import getProdutos
from src.controllers.getEstoqueProduto import getEstoqueProduto
from src.controllers.postProduto import postProduto
from src.controllers.postReserva import postReserva
from src.controllers.addEstoque import addEstoque
from src.controllers.removeEstoque import removeEstoque
from src.controllers.deleteReserva import deleteReservaPedidoProduto
from src.schemas import ProdutoCreate, ReservaCreate, EstoqueChange
from src.utils import get_json_or_400, session_scope


app = Flask(__name__)

@app.route('/produtos', methods=['GET'])
def listar_produtos():
    with session_scope() as session:
        data = getProdutos(session)
        return jsonify(data)

@app.route('/estoque/<int:id>', methods=['GET'])
def listar_estoque_produto(id: int):
    with session_scope() as session:
        data = getEstoqueProduto(id, session)
        if data is None:
            return jsonify({"error": "not_found"}), 404
        return jsonify(data)

@app.route('/reserva/<int:id_pedido>', methods=['GET'])
def listar_reservas_pedido(id_pedido: int):
    with session_scope() as session:
        data = getReservasPedido(id_pedido, session)
        return jsonify(data)

@app.route('/reserva/<int:id_pedido>/<int:id_produto>', methods=['GET'])
def listar_reserva_pedido_produto(id_pedido: int, id_produto: int):
    with session_scope() as session:
        data = getReservaPedidoProduto(id_pedido, id_produto, session)
        if data is None:
            return jsonify({"error": "not_found"}), 404
        return jsonify(data)

@app.route('/produto', methods=['POST'])
def criar_produto():
    with session_scope() as session:
        payload = ProdutoCreate.parse_obj(get_json_or_400())
        postProduto(session, payload.nome, payload.descricao, payload.quantidade)
        return jsonify({"message": "produto_criado"}), 201

@app.route('/reserva', methods=['POST'])
def criar_reserva():
    with session_scope() as session:
        payload = ReservaCreate.parse_obj(get_json_or_400())
        postReserva(payload.idproduto, payload.idpedido, payload.quantidade, session)
        return jsonify({"message": "reserva_criada"}), 201

@app.route('/estoque/adicionar', methods=['POST'])
def adicionar_estoque():
    with session_scope() as session:
        payload = EstoqueChange.parse_obj(get_json_or_400())
        addEstoque(payload.id, payload.quantidade, session)
        return jsonify({"message": "estoque_atualizado"}), 200

@app.route('/estoque/remover', methods=['POST'])
def remover_estoque():
    with session_scope() as session:
        payload = EstoqueChange.parse_obj(get_json_or_400())
        removeEstoque(payload.id, payload.quantidade, session)
        return jsonify({"message": "estoque_atualizado"}), 200

@app.route('/reserva/<int:id_pedido>/<int:id_produto>', methods=['DELETE'])
def deletar_reserva(id_pedido: int, id_produto: int):
    with session_scope() as session:
        deleteReservaPedidoProduto(id_pedido, id_produto, session)
        return jsonify({"message": "reserva_deletada"}), 200


if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)
