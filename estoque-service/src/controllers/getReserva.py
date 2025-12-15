from src.database import get_session
from src.model import Reserva


def getReservasPedido(pedido:int, session=None):
    if session is None:
        session = get_session()
        return getReservasPedido(pedido, session)

    return session.query(Reserva).filter_by(id_pedido=pedido)

def getReservaPedidoProduto(pedido:int, produto:int, session=None):
    if session is None:
        session = get_session()
        return getReservaPedidoProduto(pedido, produto, session)

    return session.query(Reserva).filter_by(id_pedido=pedido, id_produto=produto).first()