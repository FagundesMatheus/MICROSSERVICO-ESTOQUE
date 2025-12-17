from src.database import get_session
from src.model import Reserva


def getReservasPedido(pedido:int, session):

    return session.query(Reserva).filter_by(id_pedido=pedido)

def getReservaPedidoProduto(pedido:int, produto:int, session):

    return session.query(Reserva).filter_by(id_pedido=pedido, id_produto=produto).first()