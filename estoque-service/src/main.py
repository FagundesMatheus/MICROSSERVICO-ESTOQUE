from flask import Flask, request
from src.controllers.getReserva import getReservasPedido, getReservaPedidoProduto
from src.controllers.getProdutos import getProdutos
from src.controllers.getEstoqueProduto import getEstoqueProduto
from src.controllers.postProduto import postProduto
from src.controllers.postReserva import postReserva
from src.controllers.addEstoque import addEstoque
from src.controllers.removeEstoque import removeEstoque
from src.controllers.deleteReserva import deleteReservaPedidoProduto
from src.database import get_session

app = Flask(__name__)

@app.route('/produtos', methods=['GET'])
def listar_produtos():
    with get_session() as session:
        return getProdutos(session)

@app.route('/estoque/<int:id>', methods=['GET'])
def listar_estoque_produto(id):
    with get_session() as session:
        return getEstoqueProduto(id, session)

@app.route('/reserva/<int:id_pedido>', methods=['GET'])
def listar_reservas_pedido(id_pedido):
    with get_session() as session:
        return getReservasPedido(id_pedido, session)

@app.route('/reserva/<int:id_pedido>/<int:id_produto>', methods=['GET'])
def listar_reserva_pedido_produto(id_pedido, id_produto):
    with get_session() as session:
        return getReservaPedidoProduto(id_pedido, id_produto, session)

@app.route('/produto', methods=['POST'])
def criar_produto():
    with get_session() as session:
        return postProduto(request.json, session)

@app.route('/reserva', methods=['POST'])
def criar_reserva():
    with get_session() as session:
        return postReserva(request.json, session)

@app.route('/estoque/adicionar', methods=['POST'])
def adicionar_estoque():
    with get_session() as session:
        return addEstoque(request.json, session)

@app.route('/estoque/remover', methods=['POST'])
def remover_estoque():
    with get_session() as session:
        return removeEstoque(request.json, session)

@app.route('/reserva/<int:id_pedido>/<int:id_produto>', methods=['DELETE'])
def deletar_reserva(id_pedido, id_produto):
    with get_session() as session:
        return deleteReservaPedidoProduto(id_pedido, id_produto, session)

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)
