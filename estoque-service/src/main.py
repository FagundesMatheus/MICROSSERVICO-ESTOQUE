from flask import Flask
from controllers.getReserva import getReservasPedido, getReservaPedidoProduto
from controllers.getProdutos import getProdutos
from controllers.getEstoqueProduto import getEstoqueProduto
from database import get_session


@app.route('/produtos', methods=['GET'])
def listar_produtos():
    with get_session() as session:
        return getProdutos(session)

@app.route('/estoque/<int:id>', methods=['GET'])
def listar_pedidos(id):
    with get_session() as session:
        return getEstoqueProduto(id, session)

@app.route('/reserva/<int:id_pedido>', methods=['GET'])
def listar_reservas(id_pedido):
    with get_session() as session:
        return getReservasPedido(id_pedido, session)

@app.route('/reserva/<int:id_pedido>/<int:id_produto>', methods=['GET'])
def listar_reservas(id_pedido, id_produto):
    with get_session() as session:
        return getReservaPedidoProduto(id_pedido, id_produto, session)
