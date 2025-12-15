from src.database import get_session
from src.model import Reserva
from getReserva import getReservasPedido
from addEstoque import addEstoque


def deleteReservasPedido(idPedido:int, devolverEstoque:bool, session=None):
    if session is None:
        session = get_session()
        deleteReservasPedido(idPedido, devolverEstoque, session)

    reservas = getReservasPedido(idPedido, session)
    for reserva in reservas:
        if devolverEstoque:
            addEstoque(reserva.id_produto, reserva.quantidade, session)
        session.delete(reserva)
