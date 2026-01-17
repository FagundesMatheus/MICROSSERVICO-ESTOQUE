from src.model import Reserva


def getReservasPedido(pedido:int, session):
    reservas = session.query(Reserva).filter_by(id_pedido=pedido).all()
    return [
        {
            "id_produto": r.id_produto,
            "id_pedido": r.id_pedido,
            "quantidade": r.quantidade
        }
        for r in reservas
    ]

def getReservaPedidoProduto(pedido:int, produto:int, session):
    reserva = session.query(Reserva).filter_by(id_pedido=pedido, id_produto=produto).first()
    if reserva:
        return {
            "id_produto": reserva.id_produto,
            "id_pedido": reserva.id_pedido,
            "quantidade": reserva.quantidade
        }
    return None