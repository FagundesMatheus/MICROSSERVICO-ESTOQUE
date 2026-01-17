from src.model import Reserva
from src.controllers.getReserva import getReservasPedido, getReservaPedidoProduto
from src.controllers.addEstoque import addEstoque


def deleteReservasPedido(idPedido:int, devolverEstoque:bool, session):
    reservas = getReservasPedido(idPedido, session)
    for reserva in reservas:
        if devolverEstoque:
            addEstoque(reserva.id_produto, reserva.quantidade, session)
        session.delete(reserva)

def deleteReservaPedidoProduto(idPedido:int, idProduto:int, session):
    reserva = getReservaPedidoProduto(idPedido, idProduto, session)
    session.delete(reserva)